# Brownfield onboarding checklist

Follow the [onboarding guide](../spec/usage/onboarding.md). Each step is one reviewable change in the adopting repository.

1. **Install.** Pin a reviewed commit of `specified-development`, install the tools and copy the kit templates (see [README](README.md)).
2. **Choose one area.** Pick a bounded module, service or feature. Record its stable feature ID and source paths. Everything else stays explicitly unspecified.
3. **Characterize.** Draft a present-tense feature page (behavior only) and a plan with its implementation-targets section (current language, architecture, dependencies) from the code, docs, existing tests and observed behavior. Record the sources for every requirement in `onboarding.json`.
4. **Decide known defects.** For every behavior the reviewer does not intend, record either `specify-actual` with a follow-up change, or `specify-intended` and add the requirement to `initial_gaps`.
5. **Review and accept.** A human reviewer accepts the spec. Record the actor and time in `onboarding.json`. Characterization mode ends for this area.
6. **Author independent tests.** Write `build/<feature>/tests.md` and the matching tests from the accepted spec. Existing tests may be adopted only when they check spec-level behavior; record them as `adopted-existing-test` with a reference.
7. **Baseline.** Run the independent cases at the baseline commit. Requirements whose cases all pass are satisfied; the rest are the initial gaps.
8. **Validate.**

   ```sh
   specified-check-layout --root .
   specified-onboarding onboarding.json --root . --results results.json
   specified-gaps evidence.json --root . --output status.json
   ```

9. **Wire in agents and CI.** Add the `AGENTS.md` fragment and the CI workflow.
10. **Continue spec-first.** From now on, every change in this area starts as a spec edit. Onboard further areas one at a time.

For a project that already uses Spec Kit, map `specs/<feature>/` into `spec/features/<feature>/` and `build/<feature>/`, keep feature history and the constitution, convert prose to present tense, and record the mapping in `spec_kit_layout`.
