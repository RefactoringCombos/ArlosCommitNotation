# Arlo's Commit Notation

## Upper case: Deliberate behavior changes

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| F       | Feature                                                   |
| B       | Bug                                                       |
| R       | Test-supported Refactoring<sup>[3]</sup>                      |

## Lower case: Low risk

| Prefix  | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| c       | comments (add/delete)                                        |
| d       | developer documentation changes (not end-user facing)        |
| e       | environment (non-code) changes that affect development setup |
| t       | Test only                                                    |
| r       | Provable Refactoring                                         |
| a       | Automated formatting                                         |

## Three characters: The danger zone!

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| !!!     | non-provable refactoring                                  |
| ***     | does not compile intermediate step                        |

# Description

[Arlo's](https://twitter.com/arlobelshee) Commit Notation is a way of making small commits that show the risk involved in each step. It is particulary useful in legacy systems. 

# Provable Refactorings

If you can get a series of commits that is all lowercase commits, you can deploy without the need for Regression Testing, or lengthy conversations about accepting the pull request to trunk.

A provable refactoring requires a burden of proof. The main methods of proof are
* automated refactoring via tool, with knowledge of tool bugs.
* Scripted manual refactoring, using the compiler to verify each step. [Recipes Here](https://github.com/InnovatingTeams/provable-refactorings)

With discipline these can prove bug-for-bug compatibility. They demonstrate safety for unknown bugs, even guaranteeing that you do not accidentally fix a bug you don't know exists (but your customers may be depending on).

All of these recipes use static analysis to demonstrate safety. As such, they work equally well on code that lacks tests. They can be a good way to make code testable. Their downside is that they are language-specific.

# Test-supported Refactorings
[3]:#test-supported-refactorings

These are refactorings with a lower standard of proof:
1. Commit contains only a single refactoring.
2. Refactoring is named and published (e.g., in [Fowler's refactoring catalog](https://refactoring.com/catalog/))
3. Your entire product is very highly tested
4. You followed the published recipe, including running full-suite test runs when indicated

Note that this can not prove bug-for-bug compatibility. It can only demonstrate that you didn't cause any problems that have been thought of before; it does not demonstrate safety for novel bugs.

Requirement 3 is there because many refactorings can have non-local effects. It is not sufficient to have great tests on the code you are changing. You also need great tests on the code that you are not intending to change, to demonstrate that you didn't. Therefore, until your entire codebase is very highly tested, you will not be able to use the `R` commit designation.

# Living Documentation

We invite you to submit pull requests to help evolve this notation and methodology.
