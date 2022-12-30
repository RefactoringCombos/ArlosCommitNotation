# Extension Intentions

Each project can define a set of extension intentions. Each project should define which extension codes it uses. It is up to each project to define the approaches for each of the 4 risk levels.

These are some common intentions, each used in several projects. Each also lists alternatives used in projects that don't use the code.

| Prefix | Name | Intention | Alternatives |
| --- | --- | --- | --- |
| `M`/`m` | Merge | Merge branches | Use `F`, `B`, or `R`, based on the main intention of the branch, with risk level based on maximum for any individual commit in the branch. Optionally leave blank for merge from main to a feature branch. |
| `t` | Test-only | Alter automated tests without altering functionality. May include code-generating code that just throws a `NotImplementedException` or similar approaches. | Use `f` or `b`, depending on which kind of work this test is going to validate. Use `r` if this is a refactoring purely within test code. It is a lower-case letter unless you also change product code. |
| `e` | Environment | Environment (non-code) changes that affect development setup, and other tooling changes that don't affect program behavior (e.g. linting) | Consider the environment to be a product where the users are team members, and code it accordingly. |
| `a` | Auto | Automatic formatting, code generation, or similar tasks. | Use the intention that matches the reason you are performing the action, almost-certainly as a lower-case level of risk. For example, code cleanup would be `r`, and generating code to make a test for a new feature compile would be `t` or `f`. |
| `c` | Comment | Changes comments only. Does not include comments that are visible to doc-generation tools. | Use `d`. |
| `p` | Process | Changes some team process or working agreement. | Any of: <ul><li>Use a tacit, informal process.</li><li>Use `d`.</li><li>Keep your process definition outside of source control.</li></ul> |
| `s` | Spec | Changes the spec or design. Used when team does formal specs or design reviews and keeps all such documents in the main product source, perhaps in the product code itself. | Any of: <ul><li>Use informal specs.</li><li>Use `d`.</li><li>Use your test suite as your only spec.</li><li>Keep your spec / design outside of source control.</li></ul> |
| `n` | NOP | A commit with no changes (`--allow-empty`) | `r` |
| `*` | Unknown / multiple | Made a bunch of changes and are just getting it checked in. No real way to validate safety, and may not even compile. Usually used at the highest risk level (`***`). | Don't allow this. Require each commit to do exactly one intention and document itself accordingly. |
