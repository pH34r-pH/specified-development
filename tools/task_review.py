"""Render a checked review of existing structured authoring tasks without dispatch."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING or __package__:
    from .bundle_common import ValidationError, confined_file, read_json, require
    from .bundle_review import write_or_check
    from .validate_foundation import load_authoring_tasks, validate_native_projection
else:
    from bundle_common import ValidationError, confined_file, read_json, require
    from bundle_review import write_or_check
    from validate_foundation import load_authoring_tasks, validate_native_projection

OUTPUT = "docs/task-review.md"


def _text(value: Any) -> str:
    # These are display fields, never HTML or executable Markdown supplied by a task.
    return html.escape(str(value)).replace("|", "&#124;").replace("`", "&#96;")


def generate(root: Path) -> bytes:
    metadata, records = load_authoring_tasks(root)
    bindings = read_json(confined_file(root, "build/native-bindings.json"))
    contract_path = confined_file(root, "build/execution-contract.yaml")
    contract = read_json(contract_path)
    validate_native_projection(metadata, records, bindings, contract)
    lines = [
        "# Current task review", "",
        "Generated from the existing ph34r-task-authoring-v1 records. Edit reviewed authoring inputs, then regenerate this view.", "",
        "This view does not schedule or accept work. The native execution contract remains the only executable dependency graph. Planned tasks and pending bindings remain unqualified for execution.", "",
        f"Native source SHA256: `{hashlib.sha256(contract_path.read_bytes()).hexdigest()}`.", "",
        "The frozen Markdown summaries remain historical. Expand a task below to inspect the exact structured scope, command declaration, tests and acceptance used by the checked native projection. The [existing lossless bundle review](../build/bundle-review/README.md) retains full frozen inputs.", "",
    ]
    for feature in sorted(metadata):
        source = f"build/{feature}/tasks.md"
        source_hash = hashlib.sha256(confined_file(root, source).read_bytes()).hexdigest()
        lines += [f"## {_text(feature)}", "", f"[Structured source](../{source}), SHA256 `{source_hash}`.", ""]
        for record in sorted((item for item in records if item["source_feature"] == feature), key=lambda item: item["local_id"]):
            qid = record["qualified_id"]
            native_id = bindings["qualified_to_native"][qid]
            native = contract["tasks"][native_id]
            require(set(record["commands"]) <= metadata[feature]["commands"].keys(),
                    "TASK_REVIEW_COMMAND_MISSING", qid)
            commands = {name: metadata[feature]["commands"][name] for name in record["commands"]}
            prefix = feature.upper().replace("-", "_") + "_"
            for name, command in commands.items():
                require(contract["commands"].get(prefix + name) == command,
                        "TASK_REVIEW_COMMAND_MISMATCH", prefix + name)
            command_json = json.dumps(commands, sort_keys=True, ensure_ascii=False, indent=2, allow_nan=False)
            lines += [
                "<details>",
                f"<summary>{_text(native_id)} — {_text(record['title'])}</summary>", "",
                f"Qualified identity: `{_text(qid)}`.", "",
                f"Native parents: {_text(', '.join(native['parents']) or 'none')}.", "",
                f"Independent tests: {_text(', '.join(record['tests']) or 'deterministic receipt')}.", "",
                f"Acceptance: {_text(record['acceptance'])}", "",
                "Output scope:", "",
                *[f"- <code>{_text(path)}</code>" for path in record["output_scope"]], "",
                "Unexecuted command declarations:", "",
                "<pre>", html.escape(command_json), "</pre>", "",
                "</details>", "",
            ]
    return "\n".join(lines).encode("utf-8")


def check(root: Path) -> None:
    expected = generate(root)
    output = confined_file(root, OUTPUT)
    require(output.is_file() and output.read_bytes() == expected,
            "TASK_REVIEW_DRIFT", f"{OUTPUT}: regenerate with python -m tools.task_review")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        if args.check:
            check(args.root)
        else:
            write_or_check(args.root, {OUTPUT: generate(args.root)}, check=False)
        print("Task review passed; native graph unchanged and no work dispatched.")
        return 0
    except (ValidationError, OSError) as exc:
        print(f"TASK REVIEW invalid: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
