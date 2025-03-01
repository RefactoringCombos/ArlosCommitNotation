# Extension Intentions

Each project can define a set of extension intentions. Each project should define which extension codes it uses. It is up to each project to define the approaches for each of the 4 risk levels.

These are some common intentions, each used in several projects. Each also lists alternatives used in projects that don't use the code.

| Intention | Name | Description | Alternatives |
| --- | --- | --- | --- |
| `M` | Merge | Merge branches.<br>Set risk level based on maximum for any individual commit in the branch. | Use `F`, `B`, or `R`, based on the primary intention of the branch. Optionally leave blank for merge from `main` to a feature branch. |
| `T` | Test-only | Alter automated tests without altering functionality. May include code-generating code that just throws a `NotImplementedException` or similar approaches. It is a `.` risk level.| Use `F` or `B`, depending on which kind of work this test is going to validate. Use `R` if this is a refactoring purely within test code. It is a `.` risk level unless you also change product code. |
| `E` | Environment | Environment (non-code) changes that affect development setup, and other tooling changes that don't affect program behavior (e.g. linting). It is a `.` risk level.| Consider the environment to be a product where the users are team members, and code it accordingly. |
| `A` | Auto | Automatic formatting, code generation, or similar tasks. It is typically a `.` risk level.| Use the intention that matches the reason you are performing the action. For example, code cleanup would be `R`, and generating code to make a test for a new feature compile would be `T` or `F`. |
| `C` | Comment | Changes comments only. Does not include comments that are visible to doc-generation tools. It is a `.` risk level.| Use `D`. |
| `C` | Content | Changes user-visible content, such as website copy. | Use `F`. |
| `P` | Process | Changes some team process or working agreement. It is a `.` risk level.| Any of: <ul><li>Use a tacit, informal process.</li><li>Use `D`.</li><li>Keep your process definition outside of source control.</li></ul> |
| `S` | Spec | Changes the spec or design. Used when team does formal specs or design reviews and keeps all such documents in the main product source, perhaps in the product code itself. It is usually a `.` risk level.| Any of: <ul><li>Use informal specs.</li><li>Use `D`.</li><li>Use your test suite as your only spec and use `T`.</li><li>Keep your spec / design outside of source control.</li></ul> |
| `N` | NOP | A commit with no changes (`--allow-empty`). It is a `.` risk level.| Use `R`. |
| `@` | Unknown | Made a bunch of changes and are just getting it checked in. No real way to validate safety, and may not even compile. Usually used at the highest risk level (`@ @`). | Don't allow this. Require each commit to do exactly one intention and document itself accordingly. |
