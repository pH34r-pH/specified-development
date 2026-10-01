---
document_id: specified-development/distribution-contract
delivery_status: designed-only
---

# Distribution data and interface contract

This contract refines plan.md without changing spec behavior. All examples are target interfaces, not installed capabilities. `ph34r-spec` is the proposed CLI name, not an upstream `specify` subcommand.

## Native manifests

The baseline upstream-native manifest shapes are:

```yaml
# presets/ph34r-lifecycle/preset.yml (all provided files must exist at build)
schema_version: "1.0"
preset:
  id: "ph34r-lifecycle"
  name: "pH34r mature specification lifecycle"
  version: "1.0.0"
  description: "Mature specifications, mandatory tests, and fixed-input tasks"
requires:
  speckit_version: "==1.0.13"
  extensions:
    - {id: ph34r-contracts, version: "==1.0.0", required: true}
provides:
  templates:
    - {type: template, name: spec-template, file: templates/spec-template.md, strategy: replace}
    - {type: template, name: plan-template, file: templates/plan-template.md, strategy: replace}
    - {type: template, name: tests-template, file: templates/tests-template.md, strategy: replace}
    - {type: template, name: tasks-template, file: templates/tasks-template.md, strategy: replace}
    - {type: command, name: speckit.tasks, file: commands/speckit.tasks.md, strategy: replace}
    - {type: script, name: ph34r-setup-tasks-sh, file: scripts/bash/setup-tasks.sh, strategy: replace}
    - {type: script, name: ph34r-setup-tasks-ps, file: scripts/powershell/setup-tasks.ps1, strategy: replace}
# The release manifest enumerates every command and both shell variants from plan.md.
```

```yaml
# extensions/ph34r-contracts/extension.yml
schema_version: "1.0"
extension:
  id: "ph34r-contracts"
  name: "pH34r artifact contracts"
  version: "1.0.0"
  description: "Tests authoring and deterministic artifact guards/projectors"
requires:
  speckit_version: "==1.0.13"
provides:
  commands:
    - name: speckit.ph34r.tests
      file: commands/speckit.ph34r.tests.md
      description: "Author the independent tests contract from accepted spec and plan"
    - name: speckit.ph34r.validate
      file: commands/speckit.ph34r.validate.md
      description: "Run deterministic artifact validation"
# Supporting Python files live under scripts/ph34r_contracts/; they are real
# packaged executable content, not an invented provides.scripts registration API.
```

```yaml
# bundles/ph34r-standard/bundle.yml
schema_version: "1.0"
bundle:
  id: "ph34r-standard"
  name: "pH34r repository standard"
  version: "1.0.0"
  role: "developer"
  description: "Pinned mature specification workflow and artifact tooling"
requires:
  speckit_version: "==1.0.13"
  tools: []
  mcp: []
provides:
  extensions:
    - {id: ph34r-contracts, version: "1.0.0"}
  presets:
    - {id: ph34r-lifecycle, version: "1.0.0", priority: 10, strategy: replace}
```

These skeleton examples omit release provenance/license/digests until actual approved payloads exist. The release lock, rather than unsupported manifest SHA fields, holds each archive's SHA-256. Distinct shell-specific script logical names avoid duplicate-name rejection and `.sh` fallback ambiguity. Replacement task command frontmatter sets `scripts.sh` and `scripts.ps` to the explicit installed preset wrapper paths. [Pinned frontmatter processing](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli/integrations/base.py), [script resolver](https://github.com/github/spec-kit/blob/f1a548a39dba4e5e8600de1d2e0d3ff0c468d2a9/src/specify_cli/presets/_resolver.py). Bash and PowerShell are qualified before release. No current all-agent registration claim is made; active integration is the verification target.

## CLI and failures

```text
ph34r-spec validate --feature PATH --profile native-contract-v1|kanban-v1
ph34r-spec project --feature PATH --output execution-contract.yaml
ph34r-spec issues plan --contract PATH --target OWNER/REPO --output PATH
ph34r-spec issues apply --plan PATH --authorization PATH
ph34r-spec verify-install --root PATH --release-lock PATH
ph34r-spec receipt validate --contract PATH --task QUALIFIED_ID --receipt PATH
ph34r-spec cache inspect --contract PATH --task QUALIFIED_ID --environment PATH
ph34r-spec cost --usage PATH --rate-card PATH --output PATH
ph34r-spec regeneration verify --trial PATH --contract PATH
```

Exit 0 means the specific validation/projection succeeded, never human approval or task completion. Exit 2 is invalid input/schema; 3 is stale/unaccepted authority; 4 is compatibility/runtime/permission block; 5 is scope/evidence rejection; 6 is interrupted/mutation/recovery failure. Structured errors identify code, artifact/task/field, bounded evidence reference and earliest repair authority. No secret/raw environment or unrestricted log body is emitted.

## Authoritative records

| Record | Required fields and invariants |
| --- | --- |
| Artifact revision | `artifact_kind`, `revision`, logical/canonical path, `sha256`, upstream revision/hash set, `acceptance={state,actor,at,directive_ref}`, `target_status`, separate `delivery_evidence[]`. States candidate/accepted/stale/rejected are artifact states, not scheduler statuses. |
| Task leaf | Local/qualified ID, kind, story, title/goal, inputs with hashes + prerequisite-output binding rule, parents, allowed outputs, protected paths, test traces, named commands, expected acceptance, reasoning class, fixed-model policy, runtime/permission needs, budgets, issue identity. Complete metadata is embedded under exactly one `task-metadata` fenced JSON block in tasks.md. |
| Execution projection | Existing native top-level/command/task fields plus namespaced `x_distribution` metadata, profile, source hashes, and acceptance state. The task graph's edges are only `tasks.<id>.parents`. Metadata cannot carry different edges. |
| Issue binding | Qualified ID, contract hash, target repo, numeric issue ID/number, exact marker, observed immutable creator, source URL; null IDs are allowed only in a dry plan. No task/dependency state. |
| Model binding | Provider, exact model identifier, runtime version, observed identity receipt, requested/effective reasoning and speed/service tier configuration or explicit unavailable state, authorization/profile reference, versioned role default; fixed for one attempt. Low-cost Luna defaults to explicitly approved gpt-6-luna under fixed-model-v3; unavailable aliases are rejected, and historical model/tier/rate attribution is immutable. `deterministic` leaves forbid model calls. No provider flag translation absent a supported adapter. |
| Receipt | Existing artifact/contract/path/diff/commands/red/green/regression/review predicates plus qualified ID, attempt ID, actual model/runtime fingerprint, frozen-input set hash, outcome and local evidence references. Evidence never expands permitted paths/commands. |
| Release lock | Exact upstream version+peeled commit, resolved dependency lock hash, component IDs/versions/archive hashes/URLs, approved catalogs and digests, active integration targets, asset inventory, compatibility matrix. Unknown required fields block installation/release. |
| Usage | Provider/model/runtime/attempt, observed input/cache/output/reasoning counts (nullable individually), native counting semantics, normalized inclusive counts, evidence refs, duration and billing-route class. Cached <= input and reasoning <= output. |
| Rate card | ID, currency, dated effective/retrieval times, source URL/digest, provider/model/applicable tier/context/service, input/cache/output per-million rates (nullable explicitly), normalization policy, synthetic-fixture indicator. |
| Regeneration trial | Frozen authoritative input inventory, denied retained/prior-trial source scope, independent workspace/context IDs, allowed reads, model/tool/dependency/environment fingerprints, generation command receipt, oracle/regression receipts, normalized behavior digest, all attempts/costs and scoped claim/verdict. The two qualification trials within T032 use the same exact fixed model binding throughout that task attempt. |

`budget` fields bound runtime, turns, output, and retries; their consumption is enforced by the existing executor or produces a compatibility block. Scripts do not add an execution loop. The contract policy's default attempt budget is 90 minutes, max 1 initial attempt before existing-owner escalation; a retry is a distinct retained attempt. A model leaf's numeric output budget is bound before claim; the design does not pretend to know an unavailable runtime's context limit.

## Native scheduling semantics

For a new feature, authors decompose tests, implementation, and required review into distinct executable leaves. Production depends on its test leaf; dependent work depends on the appropriate verified/reviewed leaf. Each leaf receives exactly one GitHub issue; epics/feature summaries are optional non-executable groups. Sub-issue membership is never a hard dependency. Native GitHub `blocked by` edges express prerequisites. All dependency reads are paginated.

Legacy legacy Kanban contracts retain their aggregate/test/implementation/review interpretation and board-local receipts. A legacy aggregate may map to a grouping reference, but the distribution never fans out or assigns new executable identity without upstream-approved leaf decomposition. The existing execution system controls claiming, retry, completion, and resume. Normalized identity metadata is not a second graph.

## Cost oracle

For inclusive observed counts `I=1000`, `C=200`, `O=500`, `R=100` and **synthetic fixture rates** `input=2`, `cache=0.5`, `output=8` per million, equivalent cost is **0.0057 USD**. Reasoning is included in `O`. If cache rate is null with `C>0`, known subtotal is 0.0056 and total is null, with `cached_input_rate` missing. If `C=0` is observed, a missing cache rate does not prevent a complete total. A missing cache count never means zero. If native fields exclude cached input or reasoning output, the adapter first constructs inclusive totals and records that transformation; absence of a reliable definition blocks normalization.

Exact arithmetic uses Decimal; serialized amounts are decimal strings. No float rounding, zero substitution, or summation of overlapping counters is accepted. Cache-hit savings are reported only against an observed comparable cold attempt or clearly labeled estimate; they are never invented as measured savings.
