#!/usr/bin/env python3
"""Validate the published specification scaffold using only Python's stdlib.

This checks structural consistency and public-payload hygiene. It does not build,
render, install, or qualify the proposed product.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
TASK_SOURCES = {
    "foundation": "build/foundation/tasks.md",
    "distribution": "build/distribution/tasks.md",
    "directory-specs": "build/directory-specs/tasks.md",
}
NAMESPACES = {
    "foundation": "pH34r-pH/specified-development/foundation",
    "distribution": "pH34r-pH/spec-kit-distribution/001-reusable-distribution",
    "directory-specs": "pH34r-pH/specified-development/directory-specs",
}
DENIED_PATH_PARTS = {
    "archive", "archives", "credential", "credentials", "private", "research",
    "runtime", "secret", "secrets", "snapshot", "snapshots", "temp", "tmp",
}
DENIED_JSON_KEYS = {
    "access_token", "api_key", "api_token", "authorization", "bearer_token",
    "client_secret", "cookie", "credential", "credentials", "gh_token", "github_token",
    "oauth_token", "password", "passwd", "private_key", "raw_prompt", "refresh_token",
    "sas_token", "secret", "secret_key", "session_token", "signed_url", "token",
    "webhook_secret",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
TASK_BLOCK_RE = re.compile(r"```task-metadata\s*\n(.*?)\n```", re.DOTALL)
TASK_MARKER_RE = re.compile(r"^\s*- \[[ xX]\] (T\d{3})\b", re.MULTILINE)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
HTML_ID_RE = re.compile(r"\b(?:id|name)=[\"']([^\"']+)[\"']")


class ValidationError(ValueError):
    """A stable, user-facing validation failure."""


def require(condition: bool, code: str, message: str) -> None:
    if not condition:
        raise ValidationError(f"{code}: {message}")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"JSON_INVALID: {path}: {exc}") from exc


def safe_relative_path(value: Any, *, code: str = "PATH_INVALID") -> PurePosixPath:
    require(isinstance(value, str) and value != "", code, "path must be a nonempty string")
    require("\\" not in value and "\x00" not in value, code, f"unsafe path {value!r}")
    require(not value.startswith("/") and not re.match(r"^[A-Za-z]:", value), code, f"absolute path {value!r}")
    parts = value.split("/")
    require(all(part not in {"", ".", ".."} for part in parts), code, f"traversal or empty component in {value!r}")
    return PurePosixPath(value)


def confined_file(root: Path, relative: str, *, code: str = "PATH_ESCAPE") -> Path:
    rel = safe_relative_path(relative)
    candidate = root.joinpath(*rel.parts)
    cursor = root
    for part in rel.parts:
        cursor = cursor / part
        require(not cursor.is_symlink(), code, f"symlink is not allowed: {relative}")
    resolved_root = root.resolve()
    resolved = candidate.resolve(strict=False)
    require(resolved == resolved_root or resolved_root in resolved.parents, code, f"path escaped root: {relative}")
    return candidate


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def allowed_public_path(value: str) -> bool:
    try:
        path = safe_relative_path(value)
    except ValidationError:
        return False
    parts = tuple(part.lower() for part in path.parts)
    if any(part in DENIED_PATH_PARTS for part in parts):
        return False
    if path.name.lower() in {".env", "credentials.json", "secrets.json", "id_rsa", "id_ed25519"}:
        return False
    if path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}:
        return False
    if value in {".gitignore", "LICENSE", "README.md", "payload-inventory.json"}:
        return True
    if value in {
        "build/execution-contract.yaml", "build/native-bindings.json",
        "tools/validate_foundation.py", "tests/test_foundation.py",
        ".github/workflows/foundation.yml",
    }:
        return True
    if value.startswith("spec/"):
        return True
    if value in {
        "build/foundation/design-validation.json", "build/foundation/handoff.md",
        "build/foundation/plan.md", "build/foundation/tasks.md", "build/foundation/tests.md",
    }:
        return True
    if value in {
        f"build/{feature}/{name}"
        for feature in ("distribution", "directory-specs")
        for name in ("plan.md", "tests.md", "tasks.md")
    }:
        return True
    if value.startswith("tests/fixtures/foundation/"):
        return True
    return False


def check_public_inventory(root: Path) -> None:
    inventory_path = confined_file(root, "payload-inventory.json")
    inventory = read_json(inventory_path)
    require(isinstance(inventory, dict), "INVENTORY_INVALID", "inventory root must be an object")
    require(inventory.get("schema_version") == 1, "INVENTORY_VERSION", "schema_version must be 1")
    require(inventory.get("destination") == "pH34r-pH/specified-development", "INVENTORY_DESTINATION", "unexpected repository destination")
    require(inventory.get("license") == "Apache-2.0", "INVENTORY_LICENSE", "license must remain Apache-2.0")
    require(inventory.get("private_inputs_included") is False, "PRIVACY_PRIVATE_INPUTS", "private inputs must not be included")
    require(inventory.get("product_implementation_claimed") is False, "SCOPE_PRODUCT_CLAIM", "scaffold must not claim product implementation")
    entries = inventory.get("files")
    require(isinstance(entries, list), "INVENTORY_FILES", "files must be a list")
    by_path: dict[str, str] = {}
    folded: dict[str, str] = {}
    for entry in entries:
        require(isinstance(entry, dict) and set(entry) == {"path", "sha256"}, "INVENTORY_ENTRY", "each entry requires path and sha256 only")
        relative = entry["path"]
        safe_relative_path(relative)
        require(relative != "payload-inventory.json", "INVENTORY_SELF_REFERENCE", "the inventory cannot hash itself")
        require(allowed_public_path(relative), "PUBLIC_PATH_DENIED", f"path is private or outside T002 output scope: {relative}")
        require(relative not in by_path, "INVENTORY_DUPLICATE", f"duplicate path: {relative}")
        key = relative.casefold()
        require(key not in folded, "INVENTORY_CASE_COLLISION", f"case-fold collision: {folded.get(key)} and {relative}")
        require(isinstance(entry["sha256"], str) and SHA256_RE.fullmatch(entry["sha256"]) is not None, "INVENTORY_DIGEST", f"invalid SHA-256 for {relative}")
        file_path = confined_file(root, relative)
        require(file_path.is_file(), "INVENTORY_MISSING", f"listed file does not exist: {relative}")
        actual = sha256_file(file_path)
        require(actual == entry["sha256"], "INVENTORY_HASH", f"SHA-256 mismatch for {relative}")
        if relative.endswith(".json") or relative == "build/execution-contract.yaml":
            validate_public_json_privacy(read_json(file_path), relative)
        by_path[relative] = entry["sha256"]
        folded[key] = relative

    # The inventory omits itself to avoid a recursive digest. Git supplies the
    # exact public tracked/untracked file set while honoring the repo's ignores.
    if (root / ".git").exists() or (root / ".git").is_file():
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            check=False, capture_output=True,
        )
        require(result.returncode == 0, "GIT_INVENTORY", result.stderr.decode("utf-8", "replace").strip() or "git ls-files failed")
        visible = {item.decode("utf-8") for item in result.stdout.split(b"\0") if item}
        visible.discard("payload-inventory.json")
        listed = set(by_path)
        require(visible == listed, "INVENTORY_COVERAGE", f"unlisted={sorted(visible-listed)}; absent={sorted(listed-visible)}")


def _document_targets(manifest: dict[str, Any]) -> set[str]:
    docs = manifest.get("documents")
    require(isinstance(docs, dict) and docs, "MANIFEST_DOCUMENTS", "documents must be a nonempty object")
    return set(docs)


def validate_manifest_shape(manifest: Any, available_paths: set[str] | None = None) -> None:
    require(isinstance(manifest, dict), "MANIFEST_ROOT", "manifest must be an object")
    require(manifest.get("schema_version") == 1, "MANIFEST_VERSION", "schema_version must be 1")
    docs = manifest.get("documents")
    require(isinstance(docs, dict) and docs, "MANIFEST_DOCUMENTS", "documents must be a nonempty object")
    paths: dict[str, str] = {}
    ids: dict[str, str] = {}
    for doc_id, item in docs.items():
        require(isinstance(doc_id, str) and re.fullmatch(r"[a-z0-9][a-z0-9-]*(?:/[a-z0-9][a-z0-9-]*)+", doc_id) is not None, "DOCUMENT_ID", f"invalid document id {doc_id!r}")
        folded_id = doc_id.casefold()
        require(folded_id not in ids, "DOCUMENT_ID_COLLISION", f"document id collision: {doc_id}")
        ids[folded_id] = doc_id
        require(isinstance(item, dict), "DOCUMENT_ENTRY", f"document entry must be an object: {doc_id}")
        relative = item.get("path")
        rel = safe_relative_path(relative, code="DOCUMENT_PATH")
        require(rel.suffix.lower() == ".md", "DOCUMENT_PATH", f"document must be Markdown: {relative}")
        folded_path = relative.casefold()
        require(folded_path not in paths, "DOCUMENT_PATH_COLLISION", f"document path collision: {paths.get(folded_path)} and {relative}")
        paths[folded_path] = relative
        if available_paths is not None:
            require(relative in available_paths, "DOCUMENT_MISSING", f"document file missing: {relative}")
        require(item.get("visibility") == "public", "DOCUMENT_VISIBILITY", f"document is not public: {doc_id}")
        require(isinstance(item.get("role"), str) and item["role"], "DOCUMENT_ROLE", f"missing role: {doc_id}")
        deps = item.get("normative_dependencies")
        assets = item.get("assets")
        require(isinstance(deps, list) and len(deps) == len(set(deps)), "DOCUMENT_DEPENDENCIES", f"invalid dependencies: {doc_id}")
        require(isinstance(assets, list) and len(assets) == len(set(assets)), "DOCUMENT_ASSETS", f"invalid assets: {doc_id}")
        require(all(dep in docs for dep in deps), "DOCUMENT_DEPENDENCY_UNKNOWN", f"unknown dependency from {doc_id}")
    assets = manifest.get("assets")
    require(isinstance(assets, dict), "MANIFEST_ASSETS", "assets must be an object")
    asset_paths: dict[str, str] = {}
    for asset_id, item in assets.items():
        require(isinstance(asset_id, str) and asset_id.startswith("specified-development/"), "ASSET_ID", f"invalid asset id {asset_id!r}")
        require(isinstance(item, dict) and item.get("visibility") == "public", "ASSET_ENTRY", f"asset must be public: {asset_id}")
        path = item.get("path")
        safe_relative_path(path, code="ASSET_PATH")
        require(path.startswith("assets/"), "ASSET_PATH", f"asset must remain under assets/: {path}")
        require(path not in asset_paths.values(), "ASSET_PATH_COLLISION", f"duplicate asset path: {path}")
        asset_paths[asset_id] = path
        if available_paths is not None:
            require(path in available_paths, "ASSET_MISSING", f"asset file missing: {path}")
    for doc_id, item in docs.items():
        require(all(asset in assets for asset in item["assets"]), "DOCUMENT_ASSET_UNKNOWN", f"unknown asset in {doc_id}")
    document_graph = {doc_id: item["normative_dependencies"] for doc_id, item in docs.items()}
    _check_acyclic(document_graph, "DOCUMENT_DEPENDENCY_CYCLE")
    features = manifest.get("features")
    require(isinstance(features, dict), "MANIFEST_FEATURES", "features must be an object")
    for feature, item in features.items():
        require(isinstance(feature, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", feature) is not None, "FEATURE_ID", f"invalid feature id {feature!r}")
        require(isinstance(item, dict), "FEATURE_ENTRY", f"feature entry must be an object: {feature}")
        root_id = item.get("root")
        require(root_id in docs, "FEATURE_ROOT", f"feature root is unknown: {feature}")
        require(docs[root_id]["path"] == f"features/{feature}/index.md", "FEATURE_ROOT_PATH", f"feature root path mismatch: {feature}")


def validate_navigation_shape(navigation: Any, document_ids: set[str]) -> None:
    require(isinstance(navigation, dict) and navigation.get("schema_version") == 1, "NAV_VERSION", "navigation schema_version must be 1")
    items = navigation.get("items")
    require(isinstance(items, list) and items, "NAV_ITEMS", "navigation items must be a nonempty list")
    seen: set[str] = set()
    labels: set[str] = set()
    for item in items:
        require(isinstance(item, dict), "NAV_ENTRY", "navigation entries must be objects")
        doc_id = item.get("document")
        label = item.get("label")
        require(doc_id in document_ids, "NAV_DOCUMENT_UNKNOWN", f"unknown document: {doc_id}")
        require(doc_id not in seen, "NAV_DUPLICATE_DOCUMENT", f"document appears more than once: {doc_id}")
        require(isinstance(label, str) and label.strip(), "NAV_LABEL", "navigation label must be nonempty")
        require(label.casefold() not in labels, "NAV_DUPLICATE_LABEL", f"duplicate navigation label: {label}")
        seen.add(doc_id)
        labels.add(label.casefold())
    require(seen == document_ids, "NAV_COVERAGE", f"navigation omits documents: {sorted(document_ids-seen)}")


def _check_acyclic(graph: dict[str, list[str]], error_code: str) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        require(node not in visiting, error_code, f"cycle includes {node}")
        if node in visited:
            return
        visiting.add(node)
        for parent in graph[node]:
            require(parent in graph, error_code, f"unknown graph node {parent}")
            visit(parent)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)


def _slug_heading(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.lower()
    text = re.sub(r"[^\w -]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text.strip())


def _anchors(markdown: str) -> set[str]:
    anchors = set(HTML_ID_RE.findall(markdown))
    seen: defaultdict[str, int] = defaultdict(int)
    for heading in HEADING_RE.findall(markdown):
        base = _slug_heading(heading)
        suffix = seen[base]
        seen[base] += 1
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
    return anchors


def validate_markdown_links(spec_root: Path, documents: dict[str, str]) -> None:
    """Check simple local Markdown links; this is not a renderer implementation."""
    sources: dict[str, str] = {}
    for doc_id, relative in documents.items():
        safe_relative_path(relative, code="DOCUMENT_PATH")
        path = confined_file(spec_root, relative, code="DOCUMENT_PATH")
        require(path.is_file(), "DOCUMENT_MISSING", f"{doc_id}: {relative}")
        try:
            sources[relative] = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise ValidationError(f"DOCUMENT_READ: {relative}: {exc}") from exc
    for source_rel, content in sources.items():
        source_path = PurePosixPath(source_rel)
        for raw_target in LINK_RE.findall(content):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>\"'")
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")) or target.startswith("//"):
                continue
            path_text, sep, fragment = target.partition("#")
            if path_text:
                require(not path_text.startswith("/") and "\\" not in path_text and "\x00" not in path_text, "LINK_ESCAPE", f"{source_rel} -> {target}")
                parent = source_path.parent
                combined = PurePosixPath(parent, path_text)
                stack: list[str] = []
                escaped = False
                for part in combined.parts:
                    if part in {"", "."}:
                        continue
                    if part == "..":
                        if not stack:
                            escaped = True
                            break
                        stack.pop()
                    else:
                        stack.append(part)
                require(not escaped, "LINK_ESCAPE", f"{source_rel} -> {target}")
                destination = PurePosixPath(*stack).as_posix()
            else:
                destination = source_rel
            # Resolve and reject symlinks before testing existence or opening a
            # fragment target. Path.is_file()/read_text() alone follows links.
            destination_path = confined_file(spec_root, destination, code="LINK_ESCAPE")
            require(destination_path.is_file(), "LINK_MISSING", f"{source_rel} -> {target}")
            if sep and fragment:
                if destination in sources:
                    target_text = sources[destination]
                else:
                    try:
                        target_text = destination_path.read_text(encoding="utf-8")
                    except (OSError, UnicodeError) as exc:
                        raise ValidationError(f"LINK_FRAGMENT_READ: {source_rel} -> {target}: {exc}") from exc
                require(fragment in _anchors(target_text), "LINK_FRAGMENT_MISSING", f"{source_rel} -> {target}")


def validate_spec(root: Path) -> None:
    manifest_path = confined_file(root, "spec/manifest.json")
    manifest = read_json(manifest_path)
    spec_root = confined_file(root, "spec")
    available: set[str] = set()
    folded_paths: dict[str, str] = {}
    for entry in spec_root.rglob("*"):
        relative = entry.relative_to(spec_root).as_posix()
        safe_relative_path(relative, code="SPEC_PATH")
        require(not entry.is_symlink(), "SPEC_SYMLINK", f"symlinks are not allowed in the specification tree: {relative}")
        if entry.is_file():
            folded = relative.casefold()
            require(folded not in folded_paths, "SPEC_CASE_COLLISION", f"case-fold collision: {folded_paths.get(folded)} and {relative}")
            folded_paths[folded] = relative
            available.add(relative)
        else:
            require(entry.is_dir(), "SPEC_ENTRY_TYPE", f"unsupported filesystem entry: {relative}")
    validate_manifest_shape(manifest, available)
    listed_documents = {item["path"] for item in manifest["documents"].values()}
    listed_assets = {item["path"] for item in manifest["assets"].values()}
    allowed_controls = {"manifest.json", "navigation.json"}
    registered = listed_documents | listed_assets | allowed_controls
    require(available == registered, "SPEC_SOURCE_CLOSURE", f"unregistered={sorted(available-registered)}; missing={sorted(registered-available)}")
    navigation = read_json(confined_file(root, "spec/navigation.json"))
    doc_ids = _document_targets(manifest)
    validate_navigation_shape(navigation, doc_ids)
    mapping = {doc_id: item["path"] for doc_id, item in manifest["documents"].items()}
    validate_markdown_links(root / "spec", mapping)


def _task_metadata(markdown: str, source: str) -> dict[str, Any]:
    matches = TASK_BLOCK_RE.findall(markdown)
    require(len(matches) == 1, "TASK_METADATA_BLOCK", f"expected one task-metadata block in {source}")
    try:
        metadata = json.loads(matches[0])
    except json.JSONDecodeError as exc:
        raise ValidationError(f"TASK_METADATA_JSON: {source}: {exc}") from exc
    require(metadata.get("metadata_schema") == "ph34r-task-authoring-v1", "TASK_METADATA_SCHEMA", f"unexpected metadata schema in {source}")
    return metadata


def _case_ids(markdown: str) -> set[str]:
    return set(re.findall(r"^\|\s*((?:FND|TST|DIR)-\d{3})\s*\|", markdown, re.MULTILINE))


def load_authoring_tasks(root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    metadata_by_feature: dict[str, Any] = {}
    records: list[dict[str, Any]] = []
    all_qids: set[str] = set()
    for feature, relative in TASK_SOURCES.items():
        path = confined_file(root, relative)
        content = path.read_text(encoding="utf-8")
        metadata = _task_metadata(content, relative)
        require(metadata.get("namespace") == NAMESPACES[feature], "TASK_NAMESPACE", f"namespace mismatch in {relative}")
        authored = metadata.get("tasks")
        require(isinstance(authored, list) and authored, "TASK_LIST", f"task list missing in {relative}")
        markers = TASK_MARKER_RE.findall(content)
        ids = [task.get("local_id") for task in authored if isinstance(task, dict)]
        require(len(ids) == len(set(ids)) == len(markers), "TASK_MARKERS", f"task markers/metadata differ in {relative}")
        require(set(ids) == set(markers), "TASK_MARKERS", f"task marker IDs differ from metadata in {relative}")
        cases = _case_ids(confined_file(root, f"build/{feature}/tests.md").read_text(encoding="utf-8"))
        for task in authored:
            local_id = task.get("local_id")
            qualified_id = task.get("qualified_id")
            require(isinstance(local_id, str) and re.fullmatch(r"T\d{3}", local_id), "TASK_ID", f"invalid local task id in {relative}")
            expected_qid = f"{NAMESPACES[feature]}/{local_id}"
            require(qualified_id == expected_qid, "TASK_QUALIFIED_ID", f"{local_id} has unexpected qualified id")
            require(qualified_id not in all_qids, "TASK_DUPLICATE_IDENTITY", f"duplicate qualified id: {qualified_id}")
            all_qids.add(qualified_id)
            require(isinstance(task.get("tests"), list), "TASK_TESTS", f"tests must be a list: {qualified_id}")
            unknown_cases = set(task["tests"]) - cases
            require(not unknown_cases, "TASK_TEST_UNKNOWN", f"unknown tests for {qualified_id}: {sorted(unknown_cases)}")
            marker = f"<!-- spec-task:{qualified_id} -->"
            require(content.count(marker) == 1, "TASK_ISSUE_MARKER", f"expected one stable task marker for {qualified_id}")
            issue_identity = task.get("issue_identity")
            require(isinstance(issue_identity, dict) and issue_identity.get("marker") == marker, "TASK_ISSUE_IDENTITY", f"structured issue marker differs for {qualified_id}")
            frozen = task.get("frozen_inputs", {}).get("authoritative", [])
            require(isinstance(frozen, list), "TASK_FROZEN_INPUTS", f"frozen authoritative inputs must be a list: {qualified_id}")
            frozen_paths: set[str] = set()
            for input_record in frozen:
                require(isinstance(input_record, dict) and set(input_record) == {"path", "sha256"}, "TASK_FROZEN_INPUT", f"invalid frozen input record: {qualified_id}")
                input_path = input_record["path"]
                safe_relative_path(input_path, code="TASK_FROZEN_PATH")
                require(input_path not in frozen_paths, "TASK_FROZEN_DUPLICATE", f"duplicate frozen input for {qualified_id}: {input_path}")
                frozen_paths.add(input_path)
                require(isinstance(input_record["sha256"], str) and SHA256_RE.fullmatch(input_record["sha256"]) is not None, "TASK_FROZEN_DIGEST", f"invalid frozen hash for {qualified_id}: {input_path}")
                frozen_file = confined_file(root, input_path, code="TASK_FROZEN_PATH")
                require(frozen_file.is_file(), "TASK_FROZEN_MISSING", f"missing frozen input for {qualified_id}: {input_path}")
                require(sha256_file(frozen_file) == input_record["sha256"], "TASK_FROZEN_HASH", f"frozen input hash mismatch for {qualified_id}: {input_path}")
            copy = dict(task)
            copy["source_feature"] = feature
            records.append(copy)
        metadata_by_feature[feature] = metadata
    return metadata_by_feature, records


def _graph_cycle(tasks: dict[str, Any]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        require(node not in visiting, "NATIVE_CYCLE", f"dependency cycle includes {node}")
        if node in visited:
            return
        visiting.add(node)
        for parent in tasks[node]["parents"]:
            require(parent in tasks, "NATIVE_PARENT_UNKNOWN", f"{node} depends on unknown native task {parent}")
            visit(parent)
        visiting.remove(node)
        visited.add(node)

    for node in tasks:
        visit(node)


def validate_native_projection(
    metadata_by_feature: dict[str, Any],
    authored_records: list[dict[str, Any]],
    bindings: Any,
    contract: Any,
) -> None:
    require(isinstance(bindings, dict) and bindings.get("schema_version") == 1, "BINDINGS_SCHEMA", "native bindings schema mismatch")
    qualified_to_native = bindings.get("qualified_to_native")
    require(isinstance(qualified_to_native, dict), "BINDINGS_MAP", "qualified_to_native must be an object")
    qid_records = {record["qualified_id"]: record for record in authored_records}
    require(len(qid_records) == len(authored_records), "TASK_DUPLICATE_IDENTITY", "qualified task identities are not unique")
    require(set(qualified_to_native) == set(qid_records), "BINDINGS_COVERAGE", "native bindings do not match the authored task identities")
    native_ids = list(qualified_to_native.values())
    require(len(native_ids) == len(set(native_ids)), "BINDINGS_DUPLICATE_NATIVE", "native task IDs must be unique")
    require(set(native_ids) == set(contract.get("tasks", {})), "NATIVE_TASK_COVERAGE", "native graph nodes do not match native bindings")

    graph_tasks = contract.get("tasks")
    require(isinstance(graph_tasks, dict), "NATIVE_TASKS", "native tasks must be an object")
    feature_by_qid = {record["qualified_id"]: record["source_feature"] for record in authored_records}
    for qid, record in qid_records.items():
        native_id = qualified_to_native[qid]
        feature = feature_by_qid[qid]
        metadata = metadata_by_feature[feature]
        authored_local = {task["local_id"]: task["qualified_id"] for task in metadata["tasks"]}
        parents: list[str] = []
        for local_parent in record.get("parents", []):
            require(local_parent in authored_local, "TASK_PARENT_UNKNOWN", f"{qid} has unknown authored parent {local_parent}")
            parents.append(qualified_to_native[authored_local[local_parent]])
        external = metadata.get("external_native_parents", {}).get(record["local_id"], [])
        require(isinstance(external, list), "TASK_EXTERNAL_PARENTS", f"invalid external parents for {qid}")
        for parent_qid in external:
            require(parent_qid in qualified_to_native, "TASK_PARENT_UNKNOWN", f"{qid} has unknown external parent {parent_qid}")
            parents.append(qualified_to_native[parent_qid])
        native = graph_tasks[native_id]
        require(isinstance(native, dict), "NATIVE_TASK", f"native record must be object: {native_id}")
        expected_tests = record.get("tests", [])
        expected_paths = record.get("output_scope", [])
        prefix = feature.upper().replace("-", "_") + "_"
        expected_commands = [prefix + item for item in record.get("commands", [])]
        require(native.get("parents") == parents, "NATIVE_EDGE_MISMATCH", f"native parents differ for {native_id}")
        require(native.get("tests") == expected_tests, "NATIVE_TEST_MISMATCH", f"native tests differ for {native_id}")
        require(native.get("paths") == expected_paths, "NATIVE_PATH_MISMATCH", f"native output scope differs for {native_id}")
        require(native.get("commands") == expected_commands, "NATIVE_COMMAND_MISMATCH", f"native commands differ for {native_id}")
        require(native.get("expected") == record.get("acceptance"), "NATIVE_ACCEPTANCE_MISMATCH", f"native acceptance differs for {native_id}")
        projected = contract.get("x_distribution", {}).get("task_metadata", {}).get(native_id)
        require(isinstance(projected, dict), "NATIVE_METADATA_MISSING", f"projected metadata missing for {native_id}")
        expected_projection = dict(record)
        expected_projection.pop("parents", None)
        expected_projection["local_id"] = native_id
        expected_projection["source_local_id"] = record["local_id"]
        expected_projection["source_feature"] = feature
        expected_projection["commands"] = expected_commands
        require(projected == expected_projection, "NATIVE_METADATA_MISMATCH", f"projected metadata differs for {native_id}")
    for feature, metadata in metadata_by_feature.items():
        local_ids = {task["local_id"] for task in metadata["tasks"]}
        external_map = metadata.get("external_native_parents", {})
        require(isinstance(external_map, dict), "TASK_EXTERNAL_PARENTS", f"invalid external parent map for {feature}")
        require(set(external_map).issubset(local_ids), "TASK_EXTERNAL_PARENTS", f"external parent map has unknown task in {feature}")
        for local_id, parent_qids in external_map.items():
            require(isinstance(parent_qids, list) and all(parent in qualified_to_native for parent in parent_qids), "TASK_PARENT_UNKNOWN", f"invalid external parent mapping for {feature}/{local_id}")
    projection = contract.get("x_distribution", {}).get("task_metadata", {})
    require(set(projection) == set(graph_tasks), "NATIVE_METADATA_COVERAGE", "projected metadata includes omitted or extra native IDs")
    _graph_cycle(graph_tasks)


def _path_value(document: dict[str, Any], path: str) -> Any:
    value: Any = document
    for part in path.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def validate_capability_record(record: Any) -> str:
    """Check profile admission shape; never infer hidden runtime observations."""
    require(isinstance(record, dict), "CAPABILITY_RECORD", "capability record must be an object")
    selection = record.get("selection")
    require(isinstance(selection, dict), "CAPABILITY_SELECTION", "selection evidence is required")
    require(selection.get("exact_model") == "gpt-6-luna", "CAPABILITY_MODEL", "selected model must be the admitted exact model")
    require(selection.get("admission_status") == "accepted", "CAPABILITY_ADMISSION", "selection was not admitted")
    require(selection.get("requested_reasoning_effort") == "xhigh", "CAPABILITY_REASONING", "requested reasoning setting changed")
    require(isinstance(selection.get("requested_speed_tier"), str) and selection["requested_speed_tier"], "CAPABILITY_SPEED", "requested speed tier must be retained")
    require(selection.get("evidence_kind") in {"parent-service-admission", "synthetic-fixture"}, "CAPABILITY_EVIDENCE", "selection evidence kind is missing")
    require(isinstance(selection.get("evidence_ref"), str) and selection["evidence_ref"], "CAPABILITY_EVIDENCE", "selection evidence reference is required")
    profile = record.get("profile")
    require(profile in {"ordinary-implementation-v1", "hard-limit-required-v1", "measurement-qualified-experiment-v1"}, "CAPABILITY_PROFILE", f"unknown profile {profile!r}")
    required_caps = record.get("required_capabilities", [])
    require(isinstance(required_caps, list), "CAPABILITY_REQUIREMENTS", "required_capabilities must be a list")
    for item in required_caps:
        require(isinstance(item, dict) and isinstance(item.get("name"), str) and item["name"] and item.get("status") == "verified" and item.get("evidence_ref"), "CAPABILITY_UNKNOWN", f"required capability is unknown or unverified: {item}")
    constraints = record.get("required_constraints", [])
    require(isinstance(constraints, list), "CAPABILITY_CONSTRAINTS", "required_constraints must be a list")
    if constraints:
        require(profile != "ordinary-implementation-v1", "CAPABILITY_DOWNGRADE", "an explicit hard constraint cannot be downgraded to ordinary implementation")
        controls = record.get("verified_controls", [])
        require(isinstance(controls, list), "CAPABILITY_CONTROLS", "verified_controls must be a list")
        for constraint in constraints:
            require(isinstance(constraint, dict) and isinstance(constraint.get("name"), str) and constraint["name"] and isinstance(constraint.get("operation"), str) and constraint["operation"], "CAPABILITY_CONSTRAINT", f"invalid declared hard constraint: {constraint}")
            require("value" in constraint and isinstance(constraint.get("unit"), str) and constraint["unit"], "CAPABILITY_CONSTRAINT", f"hard constraint must bind a value and unit: {constraint['name']}")
            name = constraint["name"]
            matching = [control for control in controls if isinstance(control, dict) and control.get("constraint") == name]
            require(len(matching) == 1, "CAPABILITY_CONTROL_MISSING", f"no unique enforcing control for {name}")
            control = matching[0]
            require(control.get("status") == "verified" and control.get("operation") == constraint.get("operation") and control.get("value") == constraint.get("value") and control.get("unit") == constraint.get("unit") and control.get("evidence_ref"), "CAPABILITY_CONTROL_UNVERIFIED", f"hard constraint is not enforced for its declared value, unit and operation: {name}")
    if profile == "ordinary-implementation-v1":
        budget = record.get("requested_budgets", record.get("budget"))
        require(isinstance(budget, dict), "CAPABILITY_BUDGET", "ordinary profile requires a typed budget")
        require(budget.get("wall_kind") == "requested-advisory", "CAPABILITY_BUDGET_KIND", "wall budget must be explicitly advisory")
        require(budget.get("output_kind") == "requested-advisory", "CAPABILITY_BUDGET_KIND", "output budget must be explicitly advisory")
        require(isinstance(budget.get("parent_stop_conditions"), str) and budget["parent_stop_conditions"], "CAPABILITY_STOP_PLAN", "best-effort parent stop plan is required")
        effective = record.get("effective")
        reasons = record.get("effective_unavailable_reasons", record.get("unavailable_reasons"))
        require(isinstance(effective, dict) and isinstance(reasons, dict), "CAPABILITY_EFFECTIVE", "effective values and unavailability reasons must be separate")
        runtime_field = "inference_runtime_version" if "inference_runtime_version" in effective else "runtime_version"
        for field in ("model_identity", "reasoning_effort", "speed_tier", "context_limit", runtime_field):
            if effective.get(field) is None:
                require(reasons.get(field) == "unexposed-by-interface", "CAPABILITY_UNEXPLAINED_NULL", f"missing unavailability reason for effective.{field}")
        usage = record.get("usage")
        if usage is None:
            require(record.get("usage_unavailable_reason") == "unexposed-by-interface", "CAPABILITY_USAGE", "unreported usage requires a reason")
        elif isinstance(usage, dict):
            counters = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_tokens")
            missing = [field for field in counters if usage.get(field) is None]
            if missing:
                require(usage.get("reason") == "unexposed-by-interface", "CAPABILITY_USAGE", "null usage counters require an explicit unavailability reason")
        else:
            raise ValidationError("CAPABILITY_USAGE: usage must be an object or null")
        return "ordinary-behavior-eligible"
    if profile == "hard-limit-required-v1":
        require(bool(constraints), "CAPABILITY_NO_HARD_CONSTRAINT", "hard-limit profile must declare a constraint")
        return "hard-limits-verified-for-declared-operations"
    measurement = record.get("measurement")
    require(isinstance(measurement, dict), "CAPABILITY_MEASUREMENT", "measurement claim is required")
    required_fields = measurement.get("required_fields")
    require(isinstance(required_fields, list) and required_fields, "CAPABILITY_MEASUREMENT_FIELDS", "required measurement fields must be declared")
    require(isinstance(measurement.get("provenance_ref"), str) and measurement["provenance_ref"], "CAPABILITY_MEASUREMENT_PROVENANCE", "measurement provenance is required")
    missing = [field for field in required_fields if _path_value(record, field) in (None, "")]
    require(not missing, "CAPABILITY_MEASUREMENT_INCOMPLETE", f"missing required observations: {', '.join(missing)}")
    return "measurement-fields-complete-for-declared-claim"


def validate_retention(root: Path) -> None:
    gitignore = confined_file(root, ".gitignore").read_text(encoding="utf-8")
    require("/build/*/runtime/" in gitignore, "RETENTION_RUNTIME_RULE", "private runtime logs must be ignored")
    require("/build/" not in gitignore.splitlines(), "RETENTION_BUILD_RULE", "build tree must not be broadly ignored")
    for path in (
        "build/foundation/accepted/receipts/T001/bootstrap-20261001T232906Z/bootstrap.json",
        "build/foundation/accepted/receipts/T002/t002-20261002T002335Z/completion.json",
        "build/foundation/accepted/receipts/T002/t002-20261002T002335Z/completion-revision1.json",
    ):
        result = subprocess.run(["git", "-C", str(root), "check-ignore", "--no-index", "-q", "--", path], check=False)
        require(result.returncode == 1, "RETENTION_RECEIPT_IGNORED", f"accepted receipt would be ignored: {path}")
    runtime = "build/foundation/runtime/T002/t002-20261002T002335Z/private.log"
    result = subprocess.run(["git", "-C", str(root), "check-ignore", "--no-index", "-q", "--", runtime], check=False)
    require(result.returncode == 0, "RETENTION_RUNTIME_PUBLIC", "runtime logs must remain ignored")


SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"(?i)(?:[?&](?:token|sig|signature|x-amz-signature|x-goog-signature)=|x-goog-signature\s*[:=])"),
    re.compile(r"(?i)gh[pousr]_[A-Za-z0-9]{24,}"),
    re.compile(r"(?i)github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


def validate_public_json_privacy(value: Any, path: str = "$", denied_keys: set[str] | None = None) -> None:
    """Reject named sensitive fields and known credential/signature forms.

    This is a bounded public-payload check, not a universal secret detector.
    """
    denied = denied_keys or DENIED_JSON_KEYS
    if isinstance(value, dict):
        for key, child in value.items():
            normalized_key = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(key)).lower().replace("-", "_")
            sensitive_segments = {"password", "passwd"}
            require(normalized_key not in denied and not (set(normalized_key.split("_")) & sensitive_segments), "PRIVACY_FIELD", f"sensitive field at {path}.{key}")
            validate_public_json_privacy(child, f"{path}.{key}", denied)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_public_json_privacy(child, f"{path}[{index}]", denied)
    elif isinstance(value, str):
        require(not any(pattern.search(value) for pattern in SENSITIVE_VALUE_PATTERNS), "PRIVACY_VALUE", f"known credential or signed URL pattern at {path}")


def validate_completion_evidence(receipt: Any, expected: dict[str, Any], observed_store: dict[str, Any]) -> str:
    """Fail closed on the canonical T002 receipt, current PR/checks and store readback.

    `expected` and `observed_store` are read-only task-owner/GitHub observations,
    kept separate from the receipt's claims so stale or missing evidence cannot
    validate itself.
    """
    require(isinstance(receipt, dict) and receipt.get("schema_version") == 1, "RECEIPT_SCHEMA", "completion receipt schema_version 1 is required")
    require(isinstance(expected, dict) and isinstance(observed_store, dict), "RECEIPT_CONTEXT", "independent expected values and store readback are required")
    required_context = (
        "repository", "qualified_task_id", "native_id", "task_issue_number", "issue_marker",
        "accepted_design_commit", "accepted_design_tree", "head_sha", "head_tree",
        "parent_issue_number", "parent_receipt_commit", "parent_receipt_path",
        "parent_receipt_sha256", "issue_dependency_readback", "pr_number", "base_branch",
        "required_check_name", "evidence_ref", "receipt_path",
    )
    require(all(expected.get(key) not in (None, "") for key in required_context), "RECEIPT_CONTEXT_MISSING", "independent expected context is incomplete")
    for key in ("accepted_design_commit", "head_sha", "parent_receipt_commit"):
        require(isinstance(expected[key], str) and re.fullmatch(r"[0-9a-f]{40}", expected[key]) is not None, "RECEIPT_CONTEXT_HASH", f"invalid expected {key}")
    for key in ("accepted_design_tree", "head_tree"):
        require(isinstance(expected[key], str) and re.fullmatch(r"[0-9a-f]{40}", expected[key]) is not None, "RECEIPT_CONTEXT_HASH", f"invalid expected {key}")
    require(SHA256_RE.fullmatch(expected["parent_receipt_sha256"]) is not None, "RECEIPT_CONTEXT_HASH", "invalid expected parent receipt digest")
    safe_relative_path(expected["parent_receipt_path"], code="RECEIPT_CONTEXT_PATH")
    safe_relative_path(expected["receipt_path"], code="RECEIPT_CONTEXT_PATH")
    require(expected["issue_marker"] == f"<!-- spec-task:{expected['qualified_task_id']} -->", "RECEIPT_CONTEXT_MARKER", "expected issue marker is inconsistent")
    task = receipt.get("task")
    require(isinstance(task, dict), "RECEIPT_TASK", "task identity is missing")
    require(task.get("qualified_id") == expected.get("qualified_task_id") and task.get("native_id") == expected.get("native_id"), "RECEIPT_TASK_IDENTITY", "task identity differs from the assigned leaf")
    issue = task.get("issue")
    require(isinstance(issue, dict) and issue.get("number") == expected.get("task_issue_number") and issue.get("state") == "open" and issue.get("marker") == expected.get("issue_marker"), "RECEIPT_ISSUE", "assigned task issue identity/state/marker mismatch")

    source = receipt.get("source")
    require(isinstance(source, dict), "RECEIPT_SOURCE", "source evidence is missing")
    require(source.get("accepted_design_commit") == expected.get("accepted_design_commit") and source.get("accepted_design_tree") == expected.get("accepted_design_tree") and source.get("base_commit") == expected.get("accepted_design_commit"), "RECEIPT_SOURCE_BASE", "implementation is not based on the accepted design commit/tree")
    require(source.get("implementation_commit") == expected.get("head_sha") and source.get("implementation_tree") == expected.get("head_tree"), "RECEIPT_SOURCE_HEAD", "implementation source head/tree is missing or stale")
    require(source.get("working_tree_clean") is True, "RECEIPT_DIRTY_TREE", "tested source tree was not clean")

    parent = receipt.get("parent_evidence")
    require(isinstance(parent, dict), "RECEIPT_PARENT", "native parent evidence is missing")
    require(parent.get("receipt_status") == "accepted" and parent.get("receipt_commit") == expected.get("parent_receipt_commit") and parent.get("receipt_sha256") == expected.get("parent_receipt_sha256") and parent.get("receipt_path") == expected.get("parent_receipt_path"), "RECEIPT_PARENT_EVIDENCE", "accepted T001 receipt reference/hash mismatch")
    require(parent.get("issue_number") == expected.get("parent_issue_number") and parent.get("issue_dependency_readback") == expected.get("issue_dependency_readback"), "RECEIPT_PARENT_ISSUE", "native T001 issue/dependency evidence mismatch")

    capability = receipt.get("capability_profile")
    require(isinstance(capability, dict), "RECEIPT_CAPABILITY", "capability profile is missing")
    require(validate_capability_record(capability) == "ordinary-behavior-eligible", "RECEIPT_CAPABILITY", "ordinary implementation profile did not qualify")

    validation = receipt.get("validation")
    require(isinstance(validation, dict), "RECEIPT_LOCAL_CHECKS", "validation command evidence is missing")
    local_runs = validation.get("local_commands")
    require(isinstance(local_runs, list), "RECEIPT_LOCAL_CHECKS", "local command evidence must be a list")
    passed_commands = {item.get("command") for item in local_runs if isinstance(item, dict) and item.get("result") == "passed" and item.get("head") == expected.get("head_sha")}
    required_commands = {"python tools/validate_foundation.py", "python -m unittest tests.test_foundation -v"}
    require(required_commands.issubset(passed_commands), "RECEIPT_LOCAL_CHECKS", f"missing passing local checks: {sorted(required_commands-passed_commands)}")

    pr = receipt.get("pull_request")
    require(isinstance(pr, dict), "RECEIPT_PR", "draft PR evidence is missing")
    require(pr.get("number") == expected.get("pr_number") and pr.get("state") == "open" and pr.get("draft") is True and pr.get("merged") is False, "RECEIPT_PR_STATE", "expected an open, unmerged draft PR")
    require(pr.get("base_branch") == expected.get("base_branch") and pr.get("base_sha") == expected.get("accepted_design_commit"), "RECEIPT_PR_BASE", "PR base is not the accepted design head")
    require(pr.get("head_sha") == expected.get("head_sha") and pr.get("head_sha") == source.get("implementation_commit"), "RECEIPT_PR_HEAD", "PR head differs from the tested implementation head")

    ci = receipt.get("continuous_integration")
    require(isinstance(ci, dict), "RECEIPT_CI_MISSING", "expected CI check evidence is missing")
    require(ci.get("check_name") == expected.get("required_check_name") and ci.get("status") == "completed" and ci.get("conclusion") == "success", "RECEIPT_CI_RESULT", "expected CI check did not complete successfully")
    require(ci.get("head_sha") == expected.get("head_sha") and ci.get("head_sha") == pr.get("head_sha"), "RECEIPT_CI_STALE", "CI result is missing or belongs to a stale head")
    require(type(ci.get("run_id")) is int and ci["run_id"] > 0 and isinstance(ci.get("url"), str) and ci["url"].startswith("https://github.com/"), "RECEIPT_CI_REFERENCE", "CI run reference is missing")

    store = receipt.get("evidence_store")
    require(isinstance(store, dict), "RECEIPT_STORE", "durable receipt store evidence is missing")
    require(store.get("repository") == expected.get("repository") and store.get("ref") == expected.get("evidence_ref"), "RECEIPT_STORE_REF", "receipt store repository/ref mismatch")
    require(store.get("append_only_branch") is True and store.get("write_permission_observed") is True and store.get("write_allowed") is True, "RECEIPT_STORE_PERMISSION", "append-only write permission was not observed")
    require(store.get("path") == expected.get("receipt_path") and store.get("path_was_absent_before_write") is True, "RECEIPT_STORE_OVERWRITE", "receipt path was wrong or existed before write")
    require(store.get("previous_ref_sha") == observed_store.get("previous_ref_sha"), "RECEIPT_STORE_PARENT", "receipt ref did not append to the observed previous ref")
    require(observed_store.get("repository") == expected.get("repository") and observed_store.get("ref") == expected.get("evidence_ref") and observed_store.get("path") == expected.get("receipt_path"), "RECEIPT_STORE_REF", "independent receipt store path/ref readback mismatch")
    require(observed_store.get("permission_observed") is True and observed_store.get("write_allowed") is True, "RECEIPT_STORE_PERMISSION", "independent store permission readback failed")
    require(observed_store.get("path_absent_before_write") is True and observed_store.get("path_exists_after_write") is True, "RECEIPT_STORE_OVERWRITE", "receipt path existence/overwrite readback failed")
    require(observed_store.get("receipt_commit_parent_sha") == observed_store.get("previous_ref_sha"), "RECEIPT_STORE_NON_APPEND", "receipt commit is not a fast-forward append")
    require(observed_store.get("ref_head_sha") == observed_store.get("receipt_commit_sha"), "RECEIPT_STORE_HEAD", "receipt commit is not the current evidence ref head")
    for key in ("receipt_commit_sha", "receipt_commit_parent_sha", "previous_ref_sha", "ref_head_sha"):
        require(isinstance(observed_store.get(key), str) and re.fullmatch(r"[0-9a-f]{40}", observed_store[key]) is not None, "RECEIPT_STORE_REFERENCE", f"invalid store {key}")
    require(isinstance(observed_store.get("receipt_blob_sha"), str) and re.fullmatch(r"[0-9a-f]{40}", observed_store["receipt_blob_sha"]) is not None, "RECEIPT_STORE_BLOB", "receipt blob reference is missing")
    require(isinstance(observed_store.get("receipt_sha256"), str) and SHA256_RE.fullmatch(observed_store["receipt_sha256"]) is not None, "RECEIPT_STORE_DIGEST", "receipt content digest is missing")

    verdict = receipt.get("verdict")
    require(isinstance(verdict, dict) and verdict.get("accepted") is False, "RECEIPT_VERDICT", "this candidate receipt must not infer T002 owner acceptance")
    return "candidate-evidence-current; owner-acceptance-pending"


def validate_frozen_design_hashes(root: Path, contract: dict[str, Any]) -> None:
    expected = contract.get("authority", {}).get("sha256")
    require(isinstance(expected, dict), "FROZEN_HASH_TABLE", "authority sha256 table is required")
    for relative, digest in expected.items():
        path = confined_file(root, relative)
        require(path.is_file(), "FROZEN_INPUT_MISSING", relative)
        require(sha256_file(path) == digest, "FROZEN_INPUT_CHANGED", relative)


def validate_workspace(root: Path = ROOT) -> None:
    check_public_inventory(root)
    contract = read_json(confined_file(root, "build/execution-contract.yaml"))
    validate_frozen_design_hashes(root, contract)
    validate_spec(root)
    metadata_by_feature, records = load_authoring_tasks(root)
    bindings = read_json(confined_file(root, "build/native-bindings.json"))
    validate_native_projection(metadata_by_feature, records, bindings, contract)
    t002 = next(record for record in metadata_by_feature["foundation"]["tasks"] if record["local_id"] == "T002")
    t002_inputs = {record["path"]: record["sha256"] for record in t002["frozen_inputs"]["authoritative"]}
    contract_inputs = contract["authority"]["sha256"]
    contract_inputs = {path: digest for path, digest in contract_inputs.items() if path != "build/foundation/tasks.md"}
    require(t002_inputs == contract_inputs, "T002_FROZEN_INPUT_BINDING", "T002 task input hashes differ from the accepted native authority table")
    validate_retention(root)
    print("FOUNDATION scaffold checks passed; renderer and product qualification are not claimed.")


def main(argv: Iterable[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    root = Path(args[0]).resolve() if args else ROOT
    try:
        validate_workspace(root)
    except ValidationError as exc:
        print(f"FOUNDATION validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
