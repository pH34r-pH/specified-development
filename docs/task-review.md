# Current task review

Generated from the existing ph34r-task-authoring-v1 records. Edit reviewed authoring inputs, then regenerate this view.

This view does not schedule or accept work. The native execution contract remains the only executable dependency graph. Planned tasks and pending bindings remain unqualified for execution.

Native source SHA256: `0829ea48fd2801661956a3e1494cdd7416d78fbb3d685607fdc3cabacd2d5759`.

The frozen Markdown summaries remain historical. Expand a task below to inspect the exact structured scope, command declaration, tests and acceptance used by the checked native projection. The [existing lossless bundle review](../build/bundle-review/README.md) retains full frozen inputs.

## directory-specs

[Structured source](../build/directory-specs/tasks.md), SHA256 `4b42ac3124dbeba87e3ff5fd3e269078d7a143528508cb7c645ff0812f1bbfee`.

<details>
<summary>T039 — Freeze directory toolchain and baseline interfaces</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T001`.

Native parents: T038.

Independent tests: deterministic receipt.

Acceptance: Exact upstream/tool/dependency/approved baseline interface hashes frozen; renderer unknown stays blocked; zero inference.

Output scope:

- <code>locks/directory.lock.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_LOCK&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;tools/verify_directory_lock.py&quot;,
      &quot;--check&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;exact required fingerprints or explicit compatibility block&quot;
  }
}
</pre>

</details>

<details>
<summary>T040 — Author inventory and stable-ID oracles</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T002`.

Native parents: T039.

Independent tests: DIR-001, DIR-002.

Acceptance: Independent valid/invalid inventory/rename goldens have expected missing-behavior RED; no harness-error substitution.

Output scope:

- <code>tests/test_document_inventory.py</code>
- <code>tests/fixtures/documents/inventory/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_INVENTORY&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_inventory&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T041 — Implement inventory and schema validation</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T003`.

Native parents: T040.

Independent tests: DIR-001, DIR-002.

Acceptance: Complete whole-tree inventory/schema/identity/role validation and stable rename behavior pass unchanged T002 oracle.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_inventory.py</code>
- <code>schemas/document-manifest.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_INVENTORY&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_inventory&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T042 — Author closure and reference validation oracles</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T004`.

Native parents: T041.

Independent tests: DIR-003, DIR-004, DIR-005, DIR-006.

Acceptance: Handwritten normative closure/link/asset/anchor cases and pinned parser/renderer observations are reviewed before production implementation; expected RED retained.

Output scope:

- <code>tests/test_document_links.py</code>
- <code>tests/fixtures/documents/links/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_LINKS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_links&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T043 — Implement closure and parsed references</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T005`.

Native parents: T042.

Independent tests: DIR-003, DIR-004, DIR-005, DIR-006.

Acceptance: Dependency closure/parsed link/anchor/schema/asset validation preserves navigation boundary, confines paths and passes unchanged oracle without model calls.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_links.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_INVENTORY&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_inventory&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_LINKS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_links&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T044 — Author adapter source-map and hash goldens</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T006`.

Native parents: T043.

Independent tests: DIR-007, DIR-008.

Acceptance: Exact bytes/order/ranges/canonical hash independently fixed, invalid encoding and unknown fingerprint cases RED for contractual cause.

Output scope:

- <code>tests/test_document_compile.py</code>
- <code>tests/fixtures/documents/compile/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMPILE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_compile&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T045 — Implement deterministic adapter assembly</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T007`.

Native parents: T044.

Independent tests: DIR-007, DIR-008.

Acceptance: Two isolated runs byte-identical; every source range exactly matches original; lock root has no self-cycle and selected closure only.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_compile.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMPILE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_compile&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_LINKS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_links&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T046 — Author freshness and change-effect tests</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T008`.

Native parents: T045.

Independent tests: DIR-009, DIR-010.

Acceptance: Each required hash/version/input change blocks stale use; unrelated change preservation requires full revalidation; native changed-descendant expectations independently fixed.

Output scope:

- <code>tests/test_document_freshness.py</code>
- <code>tests/fixtures/documents/freshness/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_FRESHNESS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_freshness&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T047 — Implement freshness and artifact invalidation</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T009`.

Native parents: T046.

Independent tests: DIR-009, DIR-010.

Acceptance: Every entrypoint verifies accepted closure/tool/source-map hashes; changed contracts and native descendants stale; historical receipts/unaffected validated contracts retained.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_freshness.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMPILE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_compile&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_FRESHNESS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_freshness&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T048 — Author command and active-asset compatibility tests</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T010`.

Native parents: T047.

Independent tests: DIR-011, DIR-012, DIR-013.

Acceptance: Disposable upstream path/no-persist and every canonical/adapter semantic command independently exercised for both integrations; tamper/stale direct writes RED.

Output scope:

- <code>tests/test_directory_commands.py</code>
- <code>tests/fixtures/documents/commands/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMMANDS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_commands&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T049 — Implement wrappers and replacement command assets</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T011`.

Native parents: T048.

Independent tests: DIR-011, DIR-012, DIR-013.

Acceptance: Canonical-edit and guarded build commands resolve verified overrides/no-persist/sibling paths; no source symlinks, hooks-only freshness or invented flags.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_commands.py</code>
- <code>presets/ph34r-lifecycle/commands/**</code>
- <code>extensions/ph34r-contracts/extension.yml</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMMANDS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_commands&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_FRESHNESS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_freshness&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T050 — Author stage recovery and retention tests</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T012`.

Native parents: T045.

Independent tests: DIR-014, DIR-015, DIR-016.

Acceptance: Independent byte/mode/sentinel/accepted-history inventory and every interruption/cleanup/cas fixture show contractual RED; code and accepted records protected.

Output scope:

- <code>tests/test_document_retention.py</code>
- <code>tests/fixtures/documents/retention/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_RETENTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_retention&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T051 — Implement staged promotion snapshots and bounded cleanup</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T013`.

Native parents: T047, T050.

Independent tests: DIR-014, DIR-015, DIR-016.

Acceptance: Journal/before-hash recovery proves exact prior state; accepted snapshots append-only; only declared disposable managed paths cleanable; no deletion of code/history.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_retention.py</code>
- <code>.gitignore</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_FRESHNESS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_freshness&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_RETENTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_retention&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T052 — Author optional site/wiki parity and drift tests</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T014`.

Native parents: T043, T045.

Independent tests: DIR-017, DIR-018, DIR-019.

Acceptance: Exact pinned renderer evidence fixes repository/site/wiki maps/prose/assets; fake remote exercises unauthorized/missing/drift; no live publish.

Output scope:

- <code>tests/test_document_views.py</code>
- <code>tests/fixtures/documents/views/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_VIEWS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_views&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T053 — Implement optional documentation projections</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T015`.

Native parents: T051, T052.

Independent tests: DIR-017, DIR-018, DIR-019.

Acceptance: Optional locked site source config and deterministic injective one-way wiki mapping pass parity/drift oracles; dry default and authorization/access/current-base gates; no rewrite/reverse sync.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/document_views.py</code>
- <code>templates/mkdocs.yml</code>
- <code>templates/wiki/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_RETENTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_retention&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_VIEWS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_document_views&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T054 — Author directory install/upgrade compatibility tests</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T016`.

Native parents: T049, T051.

Independent tests: DIR-020.

Acceptance: Wrong-version/active-asset/tamper/interruption cases use baseline verified installer with unchanged consumer/domain authority; absent support yields explicit RED/block.

Output scope:

- <code>tests/test_directory_upgrade.py</code>
- <code>tests/fixtures/documents/upgrade/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_UPGRADE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_upgrade&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T055 — Integrate directory assets into verified releases</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T017`.

Native parents: T053, T054.

Independent tests: DIR-020.

Acceptance: Pinned component identities/digests/effective generated assets and rollback inventory include directory guards/views; compatibility verified, no release publication.

Output scope:

- <code>presets/ph34r-lifecycle/preset.yml</code>
- <code>extensions/ph34r-contracts/extension.yml</code>
- <code>bundles/ph34r-standard/bundle.yml</code>
- <code>tools/verify_directory_assets.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMMANDS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_commands&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  },
  &quot;C_UPGRADE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_upgrade&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T056 — Author complete pilot native-identity and public-boundary tests</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T018`.

Native parents: T055.

Independent tests: DIR-021, DIR-022, DIR-023, DIR-024.

Acceptance: Complete two-feature lifecycle and native-only edges, private sentinel/content provenance/status boundaries independently fixed; no projection-derived oracle or consumer writes.

Output scope:

- <code>tests/test_directory_pilot.py</code>
- <code>tests/fixtures/documents/pilot/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_PILOT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_pilot&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T057 — Run isolated complete directory compatibility pilot</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T019`.

Native parents: T056.

Independent tests: DIR-021, DIR-022, DIR-023, DIR-024.

Acceptance: All deterministic cases pass in clean synthetic/isolated installation fixtures with exact lock; optional unqualified target explicitly blocked; no inference/publication/consumer mutation.

Output scope:

- <code>build/directory-specs/accepted/pilot-candidate/qualification.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required baseline/directory product tests GREEN with exact environment&quot;
  },
  &quot;C_PILOT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_directory_pilot&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared contractual RED for independent test leaf; GREEN and focused regressions for successor&quot;
  }
}
</pre>

</details>

<details>
<summary>T058 — Review directory authority and command correctness independently</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T020`.

Native parents: T057.

Independent tests: DIR-001, DIR-002, DIR-003, DIR-004, DIR-005, DIR-006, DIR-007, DIR-008, DIR-009, DIR-010, DIR-011, DIR-012, DIR-013, DIR-014, DIR-015, DIR-016, DIR-017, DIR-018, DIR-019, DIR-020, DIR-021, DIR-022, DIR-023, DIR-024.

Acceptance: Independent reviewer checks full traces/closures/source parity/native semantics/retention/recovery/settings and reports remaining blockers; findings create separate repair, not silent behavior change.

Output scope:

- <code>build/directory-specs/accepted/review-candidate/review.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required baseline/directory product tests GREEN with exact environment&quot;
  }
}
</pre>

</details>

<details>
<summary>T059 — Prepare scoped consumer adoption and publication handoff</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T021`.

Native parents: T058.

Independent tests: DIR-020, DIR-021, DIR-023.

Acceptance: Existing canonical rollout/authority contracts compiled into concrete owner-scoped migration, rollback/history/public destination checks and remaining gates; no new semantics, application changes or external activation.

Output scope:

- <code>build/directory-specs/accepted/adoption-candidate/handoff.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required baseline/directory product tests GREEN with exact environment&quot;
  }
}
</pre>

</details>

<details>
<summary>T060 — Assemble reviewed directory compatibility evidence</summary>

Qualified identity: `pH34r-pH/specified-development/directory-specs/T022`.

Native parents: T058, T059.

Independent tests: DIR-001, DIR-002, DIR-003, DIR-004, DIR-005, DIR-006, DIR-007, DIR-008, DIR-009, DIR-010, DIR-011, DIR-012, DIR-013, DIR-014, DIR-015, DIR-016, DIR-017, DIR-018, DIR-019, DIR-020, DIR-021, DIR-022, DIR-023, DIR-024.

Acceptance: Exact artifact/test/source/lock/model history inventory and pending release/adoption/renderers evidence accurate; zero missing-field substitution and no universal disposability claim.

Output scope:

- <code>build/directory-specs/accepted/release-candidate/evidence.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required baseline/directory product tests GREEN with exact environment&quot;
  }
}
</pre>

</details>

## distribution

[Structured source](../build/distribution/tasks.md), SHA256 `48baea57dce561116b0997727d4f52850b9dd2f5d58bd242ed02820817f9e686`.

<details>
<summary>T003 — Freeze the toolchain and execution policy</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T001`.

Native parents: T002.

Independent tests: deterministic receipt.

Acceptance: Pinned upstream commit/version and resolved dependency artifact hashes are recorded; Python/uv are observed; fixed-model-v3 records approved low-cost gpt-6-luna default, preserved reasoning/speed tiers and immutable historical attribution; future dispatch requires exact selected-model admission, declared capability evidence and authority acceptance.

Output scope:

- <code>pyproject.toml</code>
- <code>uv.lock</code>
- <code>policies/execution.json</code>
- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/__init__.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ENV&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;--version&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;observed Python 3.12 and separately recorded uv/runtime/upstream fingerprint&quot;
  },
  &quot;C_LOCK&quot;: {
    &quot;argv&quot;: [
      &quot;uv&quot;,
      &quot;sync&quot;,
      &quot;--frozen&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;exact resolved lock; no runtime/model/provider fallback&quot;
  }
}
</pre>

</details>

<details>
<summary>T004 — Author independent mature-workflow template tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T002`.

Native parents: T003.

Independent tests: TST-001, TST-002.

Acceptance: Golden complete-product/status fixtures are independently authored from spec/contract; stock instructions exhibit the expected MVP/tests/status mismatch; RED cause is contractual, not a broken harness.

Output scope:

- <code>tests/test_templates.py</code>
- <code>fixtures/mature-feature/spec.md</code>
- <code>fixtures/mature-feature/plan.md</code>
- <code>fixtures/mature-feature/tests.md</code>
- <code>fixtures/mature-feature/tasks.md</code>
- <code>fixtures/mature-feature/artifact-state.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_TEMPLATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_templates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T005 — Implement the mature lifecycle preset</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T003`.

Native parents: T004.

Independent tests: TST-001, TST-002.

Acceptance: Replacement instructions describe complete mature products in past tense with separate evidence status, mandate independent tests before tasks and complete structured records, redirect both GitHub issue commands, and preserve domain constitutions; targeted GREEN uses T002 oracle unchanged.

Output scope:

- <code>presets/ph34r-lifecycle/preset.yml</code>
- <code>presets/ph34r-lifecycle/templates/spec-template.md</code>
- <code>presets/ph34r-lifecycle/templates/plan-template.md</code>
- <code>presets/ph34r-lifecycle/templates/tests-template.md</code>
- <code>presets/ph34r-lifecycle/templates/tasks-template.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.specify.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.plan.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.tasks.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.analyze.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.implement.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.taskstoissues.md</code>
- <code>presets/ph34r-lifecycle/commands/speckit.github.taskstoissues.md</code>
- <code>presets/ph34r-lifecycle/scripts/bash/setup-tasks.sh</code>
- <code>presets/ph34r-lifecycle/scripts/powershell/setup-tasks.ps1</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_TEMPLATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_templates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T006 — Author artifact gate, revision and repair tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T004`.

Native parents: T003.

Independent tests: TST-003, TST-004, TST-017.

Acceptance: Independent missing/candidate/stale tests, changed-descendant and deduplicated repair fixtures have expected RED against absent behavior; preserved unrelated receipts are asserted.

Output scope:

- <code>tests/test_gates.py</code>
- <code>fixtures/mature-feature/revisions.json</code>
- <code>fixtures/mature-feature/repair-packets.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_GATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_gates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T007 — Implement immutable authority gates and repair handoff</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T005`.

Native parents: T006.

Independent tests: TST-003, TST-004, TST-017.

Acceptance: Exact hash/acceptance prerequisites gate progression; history is retained, only changed contracts and descendants stale, repair packets hand off one bounded leaf to the existing owner without scheduling or model switches; targeted GREEN/regression passes.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/gate.py</code>
- <code>schemas/artifact.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_GATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_gates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T008 — Author metadata and traceability tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T006`.

Native parents: T003.

Independent tests: TST-009, TST-010.

Acceptance: Every required field, missing trace, unknown parent, cycle, ambiguous scope and parallel overlap fixture has an independently specified rejection; no semantic field is synthesized by validation.

Output scope:

- <code>tests/test_metadata.py</code>
- <code>fixtures/mature-feature/invalid-metadata.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_METADATA&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_metadata&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T009 — Implement structured task parsing and validation</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T007`.

Native parents: T007, T008.

Independent tests: TST-009, TST-010.

Acceptance: Single embedded metadata block matches checklist prose; full traces, command/path/budget/policy requirements and acyclic native dependencies validate; missing semantics returns earliest-authority error; no model calls.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/metadata.py</code>
- <code>schemas/task.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_GATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_gates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_METADATA&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_metadata&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T010 — Author native-contract projection tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T008`.

Native parents: T009.

Independent tests: TST-011, TST-012.

Acceptance: Handwritten native-edge/qualified-ID goldens distinguish local T001 collisions, non-executable groups and legacy aggregate gates; missing projector has expected RED.

Output scope:

- <code>tests/test_projection.py</code>
- <code>fixtures/native-contract-v1/execution-contract.yaml</code>
- <code>fixtures/native-contract-v1/expected-edges.json</code>
- <code>fixtures/kanban-v1/execution-contract.yaml</code>
- <code>fixtures/kanban-v1/aggregate-bindings.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_PROJECTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_projection&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T011 — Implement the deterministic execution-contract projector</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T009`.

Native parents: T010.

Independent tests: TST-011, TST-012.

Acceptance: existing native-contract native fields retain meanings, extensions are namespaced, legacy aggregate bindings remain intact and ambiguous imports reject; two projections are byte-stable and have exactly the golden native edge set.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/projection.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_METADATA&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_metadata&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_PROJECTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_projection&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T012 — Author scope, fixed-model and receipt tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T010`.

Native parents: T009.

Independent tests: TST-015, TST-016, TST-018.

Acceptance: Independent selection/admission-vs-effective telemetry, advisory-vs-required-hard limits, measurement qualification, no-fallback, RED/GREEN/regression, changed hash/scope/commands and permission fixtures distinguish contractual rejection from harness error.

Output scope:

- <code>tests/test_receipts.py</code>
- <code>fixtures/mature-feature/receipts.json</code>
- <code>fixtures/mature-feature/model-observations.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_RECEIPTS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_receipts&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T013 — Implement preflight and completion receipt guards</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T011`.

Native parents: T012.

Independent tests: TST-015, TST-016, TST-018.

Acceptance: One exact selected model/service admission per task, profile-specific required capability and actual permission/input/scope gates, nullable effective observations and requested/advisory parent stop plan validate; explicit hard limits fail closed without verified controls; actual acceptance predicates and unchanged-oracle regression pass; no silent fallback, false enforcement or completion side effect.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/receipts.py</code>
- <code>schemas/receipt.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_GATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_gates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_RECEIPTS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_receipts&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T014 — Author cache eligibility and revalidation tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T012`.

Native parents: T009.

Independent tests: TST-020.

Acceptance: Each authoritative/prerequisite/oracle/tool/policy/environment difference or unknown is a miss/block; the exact hit requires provenance and current acceptance rather than treating a hash as completion.

Output scope:

- <code>tests/test_cache.py</code>
- <code>fixtures/mature-feature/cache-cases.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_CACHE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_cache&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T015 — Implement scoped artifact cache validation</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T013`.

Native parents: T013, T014.

Independent tests: TST-020.

Acceptance: Canonical key covers all contract inputs and compatibility fingerprints; valid output reuse retains origin and reruns required validation with no inference; failed/stale/secret/permission entries cannot be reused.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/cache.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_CACHE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_cache&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_RECEIPTS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_receipts&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T016 — Author independent token-price accounting goldens</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T014`.

Native parents: T003.

Independent tests: TST-021, TST-022, TST-023.

Acceptance: Exact Decimal goldens include 0.0057, incomplete 0.0056 subtotal, C0 vs unknown, exclusive-to-inclusive adapters, duplicate attempts/retries and subscription distinctions; rates are labeled synthetic and not live prices.

Output scope:

- <code>tests/test_cost.py</code>
- <code>fixtures/usage/inclusive.json</code>
- <code>fixtures/usage/exclusive-native.json</code>
- <code>fixtures/usage/missing.json</code>
- <code>fixtures/usage/attempts.json</code>
- <code>fixtures/usage/rate-card.fixture.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COST&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_cost&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T017 — Implement observed token-price equivalent accounting</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T015`.

Native parents: T016.

Independent tests: TST-021, TST-022, TST-023.

Acceptance: Inclusive counts avoid overlap double counting, source/date/tier applicability is enforced, all unique attempts count, missing fields remain null with explicit subtotal, comparable cohorts only; no billing route or model calls.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/cost.py</code>
- <code>schemas/rate-card.schema.json</code>
- <code>schemas/usage.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COST&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_cost&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T018 — Author pinned installation and hostile-input tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T016`.

Native parents: T005.

Independent tests: TST-006, TST-026.

Acceptance: Disposable fixtures prove stock wrong-version skipping, tamper/unknown digest, unsafe archive/catalog/path inputs and secret-sentinel rejection independently of the wrapper; expected missing-guard RED is retained.

Output scope:

- <code>tests/test_installation.py</code>
- <code>fixtures/legacy-installation-a/installation-inventory.json</code>
- <code>fixtures/legacy-native-contract/installation-inventory.json</code>
- <code>fixtures/mature-feature/hostile-archives.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_INSTALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_installation&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T019 — Implement verified bootstrap and executable extension packaging</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T017`.

Native parents: T007, T011, T013, T015, T017, T018.

Independent tests: TST-006, TST-026.

Acceptance: Approved source digests and manifest identities are verified before extraction/mutation; upstream primitive install is reused, independent ownership conflicts reject, active generated assets are checked; six namespaced command paths resolve; no credential/model inference from deterministic verbs.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/installation.py</code>
- <code>schemas/installation.schema.json</code>
- <code>tools/bootstrap.py</code>
- <code>extensions/ph34r-contracts/extension.yml</code>
- <code>extensions/ph34r-contracts/commands/speckit.ph34r.tests.md</code>
- <code>extensions/ph34r-contracts/commands/speckit.ph34r.validate.md</code>
- <code>extensions/ph34r-contracts/commands/speckit.ph34r.project.md</code>
- <code>extensions/ph34r-contracts/commands/speckit.ph34r.verify.md</code>
- <code>extensions/ph34r-contracts/commands/speckit.ph34r.cost.md</code>
- <code>extensions/ph34r-contracts/commands/speckit.ph34r.regenerate.md</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_INSTALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_installation&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_TEMPLATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_templates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T020 — Author staged upgrade and interruption recovery tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T018`.

Native parents: T019.

Independent tests: TST-008.

Acceptance: Failure injection covers every declared stage/promotion boundary; independent before-byte/mode/sentinel inventory defines recovery; failed replacement cannot be reported as rollback success.

Output scope:

- <code>tests/test_upgrade.py</code>
- <code>fixtures/mature-feature/upgrade-journal.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_UPGRADE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_upgrade&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T021 — Implement staged upgrade, journaled promotion and rollback</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T019`.

Native parents: T020.

Independent tests: TST-008, TST-026.

Acceptance: Stage operates outside consumer root, before-hash compare-and-swap detects concurrent edits, verified rollback artifacts/journal restore exact prior managed bytes/modes and sentinels; newly introduced installation files only reconciled from journal; application code/history preserved.

Output scope:

- <code>tools/stage_upgrade.py</code>
- <code>tools/promote_upgrade.py</code>
- <code>tools/rollback_upgrade.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_INSTALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_installation&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_UPGRADE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_upgrade&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T022 — Author issue projection authorization and crash tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T020`.

Native parents: T011.

Independent tests: TST-013, TST-014.

Acceptance: Fake paginated issue/native-edge API covers &gt;100 items, numeric IDs, duplicate markers/extra edges, user vs App creator, permissions/wrong target and partial replay; default dry plan makes zero mutations.

Output scope:

- <code>tests/test_issues.py</code>
- <code>fixtures/github/pages.json</code>
- <code>fixtures/github/partial-projection.json</code>
- <code>fixtures/github/creator-policy.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ISSUES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_issues&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T023 — Implement idempotent native GitHub issue operations</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T021`.

Native parents: T013, T022.

Independent tests: TST-013, TST-014.

Acceptance: Plan/apply preserves 1:1 leaf identity and exact native edges; complete remote readback precedes readiness, creator/target/permission/drift gates fail closed, partial replay converges without duplicates, grouping creates no scheduler dependency; no existing executor workflow change.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/issues.py</code>
- <code>schemas/issue-binding.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ISSUES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_issues&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_PROJECTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_projection&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_RECEIPTS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_receipts&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T024 — Author existing-installation and execution-owner compatibility tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T022`.

Native parents: T019.

Independent tests: TST-007, TST-024.

Acceptance: Sanitized observed installations/authority histories, Claude/Codex active/inactive assets, existing executor creator/allowlist/selected-model admission and capability profiles alongside native execution semantics are exercised; incompatibility is an explicit block rather than synthetic support.

Output scope:

- <code>tests/test_compatibility.py</code>
- <code>fixtures/legacy-installation-a/local-authority.json</code>
- <code>fixtures/legacy-native-contract/local-authority.json</code>
- <code>fixtures/github/existing-executor-capability.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMPAT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_compatibility&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T025 — Implement compatibility policy and checks</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T023`.

Native parents: T021, T023, T024.

Independent tests: TST-007, TST-024.

Acceptance: Both materialized installations and active integration transitions preserve local domain constitutions/history; existing owner contracts are supported only at positively qualified versions; existing executor limitations and existing infrastructure ownership ownership remain unchanged.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/compatibility.py</code>
- <code>policies/compatibility.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_COMPAT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_compatibility&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_INSTALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_installation&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_PROJECTION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_projection&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T026 — Author regeneration oracle and frozen generation instructions</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T024`.

Native parents: T007, T013.

Independent tests: TST-005, TST-019.

Acceptance: Independent gate behavior oracle covers the declared gate.py interface; retained implementation exclusion, missing input inventory, two trial identity and failed-trial retention rules are defined; generation instructions freeze approved inputs/model/runtime and no new agent runner.

Output scope:

- <code>tests/test_regeneration.py</code>
- <code>fixtures/regeneration/input-inventory.json</code>
- <code>fixtures/regeneration/expected-behavior.json</code>
- <code>generation/instructions.md</code>
- <code>generation/packet.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_REGEN_CONTRACT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_regeneration&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T027 — Implement scoped regeneration evidence verification</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T025`.

Native parents: T026.

Independent tests: TST-005, TST-019.

Acceptance: Verifier accepts only the complete allowlisted-input evidence, two independent clean workspaces, fixed exact selection/admission and profile-required evidence, with any missing measurements explicitly unqualified and passing independent behavior/regression receipts; all attempts retained and claims limited to gate.py; it launches no model and deletes no code.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/regeneration.py</code>
- <code>schemas/regeneration.schema.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_GATES&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_gates&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_RECEIPTS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_receipts&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  },
  &quot;C_REGEN_CONTRACT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_regeneration&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T028 — Author upstream manifest, packaging and release-lock tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T026`.

Native parents: T019.

Independent tests: TST-027.

Acceptance: Actual upstream-native validators and source fixtures test exact component versions/IDs, supplied-file paths, source digests, positive reference resolution and identical-source packaging; offline/unreachable warning is insufficient for release.

Output scope:

- <code>tests/test_release.py</code>
- <code>fixtures/mature-feature/release-cases.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_RELEASE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_release&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T029 — Implement local bundle build and release integrity tooling</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T027`.

Native parents: T025, T027, T028.

Independent tests: TST-027.

Acceptance: Candidate-local build pins actual component/dependency/upstream/archive/asset digests and positively resolves local sources; deterministic package output is reproducible; unpublished destination URLs cannot be fabricated or marked release-ready; full online publication remains gated.

Output scope:

- <code>bundles/ph34r-standard/bundle.yml</code>
- <code>bundles/ph34r-standard/README.md</code>
- <code>catalogs/presets.json</code>
- <code>catalogs/extensions.json</code>
- <code>catalogs/bundles.json</code>
- <code>tools/build_release.py</code>
- <code>release-lock.json</code>
- <code>assets-manifest.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_BUILD&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;tools/build_release.py&quot;,
      &quot;--mode&quot;,
      &quot;candidate-local&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;local verified candidate only; no publish/install into consumers&quot;
  },
  &quot;C_RELEASE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_release&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T030 — Author documented CLI behavior and no-model tests</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T028`.

Native parents: T009, T011, T013, T015, T017, T019, T023, T025, T027.

Independent tests: TST-028.

Acceptance: Every documented verb/exit class rejects missing/stale authority and shell-like untrusted command input; instrumented model/mutation adapter proves deterministic verbs do not invoke inference or unintended writes.

Output scope:

- <code>tests/test_cli.py</code>
- <code>fixtures/mature-feature/cli-cases.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_CLI&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_cli&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T031 — Integrate the deterministic CLI entry point</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T029`.

Native parents: T029, T030.

Independent tests: TST-028.

Acceptance: All contract verbs delegate to approved guards/projectors, emit bounded typed results, preserve default-dry semantics and shell-free named argv execution; CLI suite and full focused regression pass with no model calls.

Output scope:

- <code>extensions/ph34r-contracts/scripts/ph34r_contracts/cli.py</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  },
  &quot;C_CLI&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_cli&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T032 — Author complete isolated pilot test</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T030`.

Native parents: T031.

Independent tests: TST-025.

Acceptance: Oracle exercises complete mature chain, revision rejection, dry issue plan, missing selected-model admission/profile policy, cache/cost, staged failure recovery and adoption gate states in an isolated first legacy installation installation; absent proof never becomes delivery.

Output scope:

- <code>tests/test_pilot.py</code>
- <code>fixtures/mature-feature/pilot-expectations.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_PILOT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_pilot&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T033 — Qualify the complete deterministic pilot in disposable copies</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T031`.

Native parents: T032.

Independent tests: TST-007, TST-023, TST-024, TST-025.

Acceptance: Synthetic feature and isolated sanitized first legacy installation copy pass all deterministic compatibility/recovery/lifecycle checks with zero model/external writes; E3 regeneration and publication/model activation remain accurately pending until separate prerequisites pass.

Output scope:

- <code>evidence/pilot/receipts.json</code>
- <code>evidence/pilot/input-inventory.json</code>
- <code>evidence/pilot/compatibility.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  },
  &quot;C_PILOT&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_pilot&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T034 — Prove two scoped behavioral regeneration trials</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T032`.

Native parents: T027, T033.

Independent tests: TST-019.

Acceptance: After confirmed available model binding and authorized inference, two independent clean source-excluded generation trials pass the unchanged gate behavior/regression oracle; observations, all failures/costs/input fingerprints retained; no deletion or broader disposability claim.

Output scope:

- <code>evidence/regeneration/trials.json</code>
- <code>evidence/regeneration/run-1/gate.py</code>
- <code>evidence/regeneration/run-2/gate.py</code>
- <code>evidence/regeneration/receipts.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  },
  &quot;C_REGEN_VERIFY&quot;: {
    &quot;argv&quot;: [
      &quot;ph34r-spec&quot;,
      &quot;regeneration&quot;,
      &quot;verify&quot;,
      &quot;--trial&quot;,
      &quot;evidence/regeneration/trials.json&quot;,
      &quot;--contract&quot;,
      &quot;specs/001-reusable-distribution/execution-contract.yaml&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;two real independently isolated fixed-model trials satisfy unchanged behavioral oracle&quot;
  }
}
</pre>

</details>

<details>
<summary>T035 — Review independent oracle and cross-artifact boundaries</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T033`.

Native parents: T033, T034.

Independent tests: TST-001, TST-002, TST-009, TST-012, TST-014, TST-016, TST-019, TST-022, TST-026.

Acceptance: Independent review validates complete-product intent, oracle provenance, contract/identity/native edges, fixed-model/permission enforcement, rollback and billing/regeneration claim limits; verdict cites current inputs and actual receipts rather than substituting for human artifact acceptance.

Output scope:

- <code>evidence/review.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  }
}
</pre>

</details>

<details>
<summary>T036 — Write repository adoption and operator handoff documentation</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T034`.

Native parents: T025, T033.

Independent tests: TST-024, TST-025.

Acceptance: Existing canonical ownership/rollout/generation contracts compiled into owner-scoped adoption/operator handoff; local authority/model/runtime/upgrade/rollback/cost/regeneration/publication gates remained explicit. Missing behavior created a separate spec repair, never invented documentation authority; no consumer/executor change.

Output scope:

- <code>build/distribution/accepted/operator-handoff/ownership.md</code>
- <code>build/distribution/accepted/operator-handoff/migration.md</code>
- <code>build/distribution/accepted/operator-handoff/operator.md</code>
- <code>build/distribution/accepted/operator-handoff/regeneration.md</code>
- <code>build/distribution/accepted/operator-handoff/release.md</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  }
}
</pre>

</details>

<details>
<summary>T037 — Assemble verified local release-candidate evidence</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T035`.

Native parents: T029, T031, T035, T036.

Independent tests: TST-025, TST-027.

Acceptance: Clean-source candidate build and exact component/generated-asset/digest/reference matrix, complete pilot/two regeneration/review receipts and rollback proof are present; public destination/license and mutation authorization are separate explicit states, never invented or bypassed.

Output scope:

- <code>evidence/release-candidate.json</code>
- <code>evidence/release-manifest.sha256</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  },
  &quot;C_BUILD&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;tools/build_release.py&quot;,
      &quot;--mode&quot;,
      &quot;candidate-local&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;local verified candidate only; no publish/install into consumers&quot;
  },
  &quot;C_RELEASE&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_release&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;declared expected RED for test-authoring; GREEN for implementation/qualification&quot;
  }
}
</pre>

</details>

<details>
<summary>T038 — Emit gated rollout handoff and identity bindings</summary>

Qualified identity: `pH34r-pH/spec-kit-distribution/001-reusable-distribution/T036`.

Native parents: T037.

Independent tests: TST-014, TST-024, TST-025.

Acceptance: Every repository and execution owner has explicit candidate/accepted/blocked adoption state and proof refs; dry identities preserve 1:1 leaves with null remote IDs; all actual repository/issue/publication/deployment mutations wait for their authorized owner and qualified runtime policy.

Output scope:

- <code>policies/rollout.json</code>
- <code>evidence/rollout-handoff.json</code>
- <code>evidence/issue-bindings.json</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_ALL&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;discover&quot;,
      &quot;-s&quot;,
      &quot;tests&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;all required behavioral/regression tests pass; E3 gate explicitly accounted&quot;
  }
}
</pre>

</details>

## foundation

[Structured source](../build/foundation/tasks.md), SHA256 `be71b34da72e5ba831d7ab42921a60ae81bd8ddb9c2a2dee5aa4b2cbe32e2aca`.

<details>
<summary>T001 — Establish minimal empty-repository PR base</summary>

Qualified identity: `pH34r-pH/specified-development/foundation/T001`.

Native parents: none.

Independent tests: FND-001.

Acceptance: Verify/preserve observed main seed with exactly README/LICENSE, or minimally seed only a truly empty approved target; retain actual repository/base/seed/file/permission/disclosure/issue/creator facts and actual accepted bootstrap verdict in immutable sanitized durable receipt; publication facts alone do not close the leaf; no ready label or history reset.

Output scope:

- <code>README.md</code>
- <code>LICENSE</code>
- <code>build/foundation/accepted/receipts/T001/*/bootstrap.json</code>
- <code>build/foundation/runtime/T001/*/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_BOOTSTRAP&quot;: {
    &quot;argv&quot;: [
      &quot;gh&quot;,
      &quot;api&quot;,
      &quot;repos/pH34r-pH/specified-development&quot;,
      &quot;--jq&quot;,
      &quot;{full_name: .full_name, default_branch: .default_branch, private: .private, size: .size, permissions: .permissions}&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;exact target/empty-or-current-base/permissions observed before minimal seed; remote authorization observed&quot;
  },
  &quot;C_SEED&quot;: {
    &quot;argv&quot;: [
      &quot;git&quot;,
      &quot;push&quot;,
      &quot;origin&quot;,
      &quot;HEAD:refs/heads/main&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;only empty-main seed README/LICENSE; never force; skip if main exists and preserve actual base&quot;
  }
}
</pre>

</details>

<details>
<summary>T002 — Publish sanitized specification foundation as draft PR</summary>

Qualified identity: `pH34r-pH/specified-development/foundation/T002`.

Native parents: T001.

Independent tests: FND-002, FND-003, FND-004, FND-005, FND-006, FND-007, FND-008, FND-009.

Acceptance: Bounded stdlib validator, independent fixtures and read-only officially pinned CI pass in isolated branch at exact accepted design inputs using only available published interfaces; one issue/native accepted T001 parent, draft PR and exact-head checks verified; sanitized durable completion receipt retains parent/service exact selected gpt-6-luna/requested-xhigh evidence, nullable effective observations, requested/advisory budgets/parent stop plan and actual permissions/input/scope/issue/parent/PR/check evidence and authorized verdict on separate append-only evidence ref. Candidate/source/parent/permission/selection/correctness or required hard-cap/missing acceptance/stale gates block; optional unexposed telemetry alone does not; no invented acceptance, merge, release, deployment or consumer change.

Output scope:

- <code>spec/**</code>
- <code>build/distribution/plan.md</code>
- <code>build/distribution/tests.md</code>
- <code>build/distribution/tasks.md</code>
- <code>build/directory-specs/plan.md</code>
- <code>build/directory-specs/tests.md</code>
- <code>build/directory-specs/tasks.md</code>
- <code>build/foundation/plan.md</code>
- <code>build/foundation/tests.md</code>
- <code>build/foundation/tasks.md</code>
- <code>README.md</code>
- <code>.gitignore</code>
- <code>tools/validate_foundation.py</code>
- <code>tests/test_foundation.py</code>
- <code>tests/fixtures/foundation/**</code>
- <code>.github/workflows/foundation.yml</code>
- <code>build/execution-contract.yaml</code>
- <code>build/native-bindings.json</code>
- <code>payload-inventory.json</code>
- <code>build/foundation/accepted/receipts/T002/*/completion.json</code>
- <code>build/foundation/runtime/T002/*/**</code>

Unexecuted command declarations:

<pre>
{
  &quot;C_CI_CHECKS&quot;: {
    &quot;argv&quot;: [
      &quot;gh&quot;,
      &quot;pr&quot;,
      &quot;checks&quot;,
      &quot;--repo&quot;,
      &quot;pH34r-pH/specified-development&quot;,
      &quot;--watch&quot;,
      &quot;--fail-fast&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;expected foundation CI succeeded at the exact separately observed PR head; empty or stale checks cannot qualify&quot;
  },
  &quot;C_CI_HEAD&quot;: {
    &quot;argv&quot;: [
      &quot;gh&quot;,
      &quot;pr&quot;,
      &quot;view&quot;,
      &quot;--repo&quot;,
      &quot;pH34r-pH/specified-development&quot;,
      &quot;--json&quot;,
      &quot;number,headRefOid,isDraft,statusCheckRollup&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;actual current branch draft PR head equals recorded passing check-run head; issue/parent/model receipt&quot;
  },
  &quot;C_FOUNDATION&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;tools/validate_foundation.py&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;bounded scaffold structural/privacy validation GREEN; product behavior not claimed&quot;
  },
  &quot;C_FOUNDATION_TESTS&quot;: {
    &quot;argv&quot;: [
      &quot;python&quot;,
      &quot;-m&quot;,
      &quot;unittest&quot;,
      &quot;tests.test_foundation&quot;,
      &quot;-v&quot;
    ],
    &quot;cwd&quot;: &quot;.&quot;,
    &quot;expect&quot;: &quot;independent malformed fixtures rejected and valid fixture passes&quot;
  }
}
</pre>

</details>
