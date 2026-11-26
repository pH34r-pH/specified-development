# Bundle review

State: **structurally validated candidate with reviewed command identities; target acceptance not granted**.

Feature: hermetic-add-fixture.

Native bytes: `c642501f40201002e862fbf87d4f056e84a642424bde603c398fc7a9793910f6`. Machine detail: [lossless object](objects/4bcd9eb5d4341fca8d65a6c36adfc7a620af5c8fe291a522ff492a2fd14fd49e.json).

The native task contract remains the sole dependency graph. This view executes no command, accepts no result, and grants no publication or deployment authority. Long descriptions are shortened here; the object retains every input byte.

Risks to review: commands are unexecuted declarations; broad write scopes need target sandbox enforcement; frozen or accepted inputs cannot be silently replaced; structural conformance cannot establish source rights or independent target acceptance.

| Task / intent | Parents | Observable acceptance | Tests | Write boundary |
| --- | --- | --- | --- | --- |
| T1 | none | All three fixed arithmetic cases pass for the exact candidate; target owner reviews independently. | CASE1 | src/add.py |

Source and authority review remains required. Structural conformance does not prove that prose is correct, tests are sufficient, commands obey their declared scope, or a legacy task is ready to execute.
