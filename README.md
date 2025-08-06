# Risk-Aware Commit Notation

This commit notation allows developers to convey 2 critical pieces of metadata about each commit:

1. How risky is it? What has the original author done to mitigate risk?
2. What was the intention? When the original author changed the code, what was s/he attempting to accomplish?

This information is conveyed in the first 3 characters of the commit summary line. That way a receiving developer can quickly scan the commit log in order to determine risk and intent for any incoming change set.

This is particularly useful when:

1. As a reviewer, deciding whether to approve a pull request
2. As a developer, getting your pull request approved faster and more easily
4. Reading `main` &mdash; use [Movement-oriented branches](Movement%20Branches.md) and read just the merge commits.

## The Four Risk Levels

We divide all behaviors of the system into 3 sets (intended change, known invariants, and unknown invariants). The change is intended to alter the *Intended Change* while not altering any of the *Invariants*. The *Risk Levels* are based on correctness guarantees: which invariants can this commit guarantee did not change, and can this commit guarantee that it made the intended change in the way the authors intended?

| Risk Level            | Code | Example                                    | Meaning                                | Correctness Guarantees                                |
|-----------------------|------|--------------------------------------------|----------------------------------------|-------------------------------------------------------|
| **(Proven) Safe**     | `.`  | `. r Extract method`                       | Addresses all known and unknown risks. | Intended Change, Known Invariants, Unknown Invariants |
| **Validated**         | `^`  | `^ r Extract method`                       | Addresses all known risks.             | Intended Change, Known Invariants                     |
| **Risky**             | `!`  | `! r Extract method`                       | Some known risks remain unverified.    | Intended Change                                       |
| **(Probably) Broken** | `@`  | `@ r Start extracting method with no name` | No risk attestation.                   |                                                       |

Behavior categories:

* **Intended Change:** The 0 or 1 behavior change intended in the commit. Could be verified by one test assertion. By default, a commit with more than 1 behavior change cannot be represented at any risk level better than *Probably Broken*.
* **Known Invariants:** All behaviors known to the development team at the time the change was made. Automated tests can greatly increase the size of this set, thus enhancing safety when commits are at a risk level that guarantees correctness for Known Invariants. However, this set also includes behaviors that are known but not tested.
* **Unknown Invariants:** All behaviors not known to the development team at the time the change was made, including behaviors that were once known but have been forgotten. These behaviors are guaranteed to be untested and untestable, as the development team does not know they exist.

Risk levels:

* **Safe:** Developer performed the task in a way that prevents all potential risks, even to invariants that developer is not aware of.
* **Validated:** Developer performed the task in some way that includes validation for the intended change and all invarants the developer thought of. The most common technique is developer-written automated tests.
* **Risky:** Developer is aware of risks and attempted to mitigate them as much as possible, but only the intended change is formally verified. Commonly this includes a manual change that the developer could not fully verify.
* **Broken:** Either known to be broken, or developer couldn't even check to see if it works. May not compile. Used when the developer cannot see the results of the work without checking in, or as a savepoint when the developer is about to switch tasks or direction.

## Core Intentions

These developer intentions exist on every project. They are always allowed in commits that use this notation.

Each intention can appear at any of the 4 risk levels. Each intention's full details section includes the potential risks inherent in that kind of change, as well as common approaches to attain each risk level.

| Prefix     | Name          | Intention                                                                                 |
|------------|---------------|-------------------------------------------------------------------------------------------|
| `F` or `f` | Feature       | Change or extend one aspect of program behavior without altering others.                  |
| `B` or `b` | Bugfix        | Repair one existing, undesirable program behavior without altering any others.            |
| `R` or `r` | Refactoring   | Change implementation without changing program behavior.                                  |
| `D` or `d` | Documentation | Change something which communicates to team members and does not impact program behavior. |

### Casing

Each intention may be expressed in UPPERCASE or lowercase. The team uses this distinction to mean roughly "pay more attention to the ones in uppercase". Teams commonly use this for one of 2 different meanings.

* **Intended behavior change**. UPPERCASE means the commit intended to change 1 behavior; lowercase means it intended to change 0 behaviors. With this approach, functionality changes would always be `F`, bugfixes `B`, refactorings `r`, and documentation `d`.
* **User-visibility**. UPPERCASE means the commit altered something user-visible. It should appear in the changelog or other documentation (perhaps in summarized for combined with other uppercase changes); lowercase means the behavior change is entirely internal. With this approach all letters can have both forms. Even a refactoring could be `R` if, for example, it adds to an internal API and you want to communicate that to other development teams.

### Feature or Functionality

**Intended Change:** 1 behavior. Could be described by a single unit test assertion.

**Known Risks**

* May alter unrelated feature (spooky action at a distance).
* May alter a piece of this feature that you intended to remain unchanged.
* May implement the intended change in a way different than intended.

| Code  | Known Approaches                                                                                                                                                                                                                                        |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `. F` | Meets all criteria for `^ F` and developers are the only users of the feature. For example, extends build tooling for your own build or adds debug logging.                                                                                             |
| `^ F` | Meets all of:<ul><li>Change is <= 8 <abbr title="lines of code">LoC</abbr><sup>[5]</sup></li><li>Feature was fully unit tested prior to this change.</li><li>Change includes new or changed unit tests to match intended behavior alteration.</li></ul> |
| `! F` | Change includes unit tests for new behavior.                                                                                                                                                                                                            |
| `@ F` | No automatic tests, or unfinished implementation.                                                                                                                                                                                                       |

### Bugfix

A bugfix is a lot like a feature. However, the intention is to change an undesired &mdash; and usually unintentional &mdash; behavior of the current system. The risk profile is similar but the intention is different, so there are often more operational risks.

**Intended Change:** 1 behavior. Could be described by a single unit test assertion.

**Known Risks**

* Intended change may have unintended consequences in the market. For example, customers may be depending on the bug.
* May alter unrelated feature (spooky action at a distance).
* May alter a piece of this feature that you intended to remain unchanged.
* May implement the intended change in a way different than intended.

| Code  | Known Approaches                                                                                                                                                                                                                                                                                                                                         |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `. B` | Meets all criteria for `^ B` and developers are the only users of the changed functionality. For example, fixes build tooling for your own build or corrects debug logging format.                                                                                                                                                                       |
| `^ B` | Meets all of:<ul><li>Reviewed current and new behavior with customer representative.</li><li>Change is <= 8 <abbr title="lines of code">LoC</abbr><sup>[5]</sup></li><li>Bug's original (buggy) behavior was captured in a unit test prior to this change.</li><li>Change includes 1 changed unit test, matching intended behavior alteration.</li></ul> |
| `! B` | Change includes unit tests for new behavior.                                                                                                                                                                                                                                                                                                             |
| `@ B` | No automatic tests, or unfinished implementation.                                                                                                                                                                                                                                                                                                        |

### Refactoring or Remodeling

A Refactoring or Remodeling intends to alter the program in some way without changing any behavior. The risk levels indicate the probability of the commit living up to that intention, based on how the code change was executed.

**Intended Change:** 0 runtime behaviors; 1 code structure.

**Known Risks**

* May cause a bug.
* May fix a bug.
* May change a behavior in a way that doesn't impact a user.
* May force a test update.

| Code  | Known Approaches                                                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `. r` | One of: <ul><li>Provable refactoring<sup>[2]</sup></li><li>Test-supported Procedural Refactoring<sup>[3]</sup> entirely within test code</li></ul> |
| `^ r` | Test-supported Procedural Refactoring<sup>[3]</sup>                                                                                                |
| `! r` | Identified single, named refactoring, but executed by editing code or without whole-project test coverage.                                         |
| `@ r` | Remodeled by editing code, even in small chunks.                                                                                                   |

### Documentation

**Intended Change:** 0 behaviors.

Changes that don't impact the code, but do change documentation around the code. The team should decide whether end-user documentation changes are `D` or `F`<sup>[1]</sup>.

**Known Risks**

* May mislead future developers.
* May mislead other stakeholders.
* May alter team processes in ways that have unintended consequences.

| Code  | Known Approaches in source files                                                 | Known Approaches in other files                                                             |
|-------|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| `. d` | Developer-visible documentation verified to generate byte-identical compilation. | Any developer-visible documentation that does not change a process                          |
| `^ d` | Verified by running tests, or things like changing text on a dev-only screen.    | Dev-impacting only, but changes compilation or process. E.g. changes code-review checklist. |
| `! d` | Verified only by compiling and launching the application.                        | Alters an important process.                                                                |
| `@ d` | Not verified.                                                                    | Trying out a process change that is intended to gain info, not to necessarily work.         |

## Extension Intentions

The basic intention annotations are comprehensive to describe any kind of change, but it may be useful to extend the notation to your project to provide additional detail that is useful in your context. Read more about [Extension Intensions](Extension%20Intentions.md).

# Provable Refactorings
[2]:#provable-refactorings

If you can get a series of commits that is all lowercase commits, you can deploy without the need for Regression Testing or lengthy conversations about accepting the pull request to trunk.

A provable refactoring requires a burden of proof. The main methods of proof are
* automated refactoring via tool, with knowledge of tool bugs.
* scripted manual refactoring, using the compiler to verify each step. [Recipes Here](https://github.com/InnovatingTeams/provable-refactorings)
* use formal methods to prove the before state and after state are equal.

With discipline these can prove bug-for-bug compatibility. They demonstrate safety for unknown bugs, even guaranteeing that you do not accidentally fix a bug you don't know exists (but your customers may be depending on).

All of these recipes use static analysis to demonstrate safety. As such, they work equally well on code that lacks tests. They can be a good way to make code testable. Their downside is that they are language-specific.

# Test-supported Procedural Refactorings
[3]:#test-supported-procedural-refactorings

These are refactorings with a lower standard of proof:
1. Commit contains only a single refactoring.
2. Refactoring is named and published (e.g., in [Fowler's refactoring catalog](https://refactoring.com/catalog/)).
3. Either:
    1. Your entire product is very highly tested, or
    2. you are working on new code that is not yet called.
4. You followed the published steps, including running full-suite test runs when indicated.

Note that this cannot prove bug-for-bug compatibility. It can only demonstrate that you didn't cause any problems that have been thought of before; it does not demonstrate safety for novel bugs.

Requirement 3 is there because many refactorings can have non-local effects. It is not sufficient to have great tests on the code you are changing. You also need great tests on the code that you are not intending to change, to demonstrate that you didn't. Therefore, until your entire codebase is very highly tested, you will only be able to use the `.` risk level on new code that is uncalled by your product.

# End-User Documentation
[1]:#end-user-documentation

Changing end user documentation changes behaviors, so can be considered a feature, bugfix, or refactoring, depending on its nature. Most teams use those codes (including levels of risk) accordingly.

However, teams that use case to distinguish user-visible and user-invisible behavior changes may wish to use `D` for end user documentation changes instead. This loses the ability to see the full intention of the change, but highlights that it was focused on documentation. Do whatever is most expressive for that commit.

# Small Features and Bug Fixes
[4]:#small-features-and-bug-fixes

Features and bug fixes intentionally change behavior. This makes them much riskier than refactorings. It is not possible to prove that they have only the intended effect. However, small changes are much lower risk for three reasons:

1. It's easy to see the possible side effects of small chunks of code.
2. It's easy to code review, so you are likely to get good reviews.
3. It's only possible when the code is well-organized already.

Therefore, we treat any feature or bug fix as high risk if it changes more than 8 lines of code in one commit. This includes test changes.

One good approach to enable small features is to refactor until the feature change is easy. Then add the feature one piece at a time, with a test for each.

# Tool Support
## Git CLI
Git allows you to specify a user-specific commit message template that shows up
when you run `git commit`. [`.gitmessage`](./.gitmessage) contains a plaintext
version of this document formatted for use as a git commit template. You can use
it by following these steps:

1. Download `.gitmessage`
2. Move `.gitmessage` to your home directory (`mv path/to/your/Downloads/.gitmessage ~/.gitmessage`)
3. Configure `git` to look for this message: `git config --global commit.template ~/.gitmessage`
4. Try it out -- in any git repo, make some change, stage it, then run `git
   commit`. You'll know it's working if you see the contents of `.gitmessage` in
   your commit message editor.

Note that you won't see this template when you are `--amend`ing a commit, when
you provide `-m` to `git commit`, during interactive rebases, and any other time
where the commit message already exists or is provided by another tool.

# Living Documentation

We invite you to submit pull requests to help evolve this notation and methodology.

<a id="lines-of-code">LoC: Lines of Code</a>

[5]:#lines-of-code
