# Arlo's Commit Notation

## Upper case: May change behavior

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| F       | Feature (<= 8 LoC<sup>[4]</sup>)                        |
| B       | Bug (<= 8 LoC<sup>[4]</sup>)                              |
| R       | Test-supported Procedural Refactoring<sup>[3]</sup>                      |

## Lower case: Low risk

| Prefix  | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| t       | Test only                                                    |
| d       | Developer documentation changes (not end-user facing<sup>[1]</sup>)        |
| a       | Automated formatting / generation                               |
| r       | Provable Refactoring<sup>[2]</sup>                 |
| c       | Comments (add/delete)                                        |
| e       | Environment (non-code) changes that affect development setup |

## Three characters: The danger zone!

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| F!!     | Feature (> 8 LoC<sup>[4]</sup>)                             |
| B!!     | Bug (> 8 LoC<sup>[4]</sup>)                                   |
| R!!     | Non-provable refactoring                                  |
| ***     | Does not compile intermediate step                        |

# Description

[Arlo's](https://twitter.com/arlobelshee) Commit Notation is a way of making small commits that show the risk involved in each step. It is particulary useful in legacy systems. 

# Provable Refactorings
[2]:#provable-refactorings

If you can get a series of commits that is all lowercase commits, you can deploy without the need for Regression Testing, or lengthy conversations about accepting the pull request to trunk.

A provable refactoring requires a burden of proof. The main methods of proof are
* automated refactoring via tool, with knowledge of tool bugs.
* Scripted manual refactoring, using the compiler to verify each step. [Recipes Here](https://github.com/InnovatingTeams/provable-refactorings)

With discipline these can prove bug-for-bug compatibility. They demonstrate safety for unknown bugs, even guaranteeing that you do not accidentally fix a bug you don't know exists (but your customers may be depending on).

All of these recipes use static analysis to demonstrate safety. As such, they work equally well on code that lacks tests. They can be a good way to make code testable. Their downside is that they are language-specific.

# Test-supported Procedural Refactorings
[3]:#test-supported-refactorings

These are refactorings with a lower standard of proof:
1. Commit contains only a single refactoring.
2. Refactoring is named and published (e.g., in [Fowler's refactoring catalog](https://refactoring.com/catalog/)).
3. Your entire product is very highly tested or you are working on new code that is not yet called.
4. You followed the published recipe, including running full-suite test runs when indicated.

Note that this can not prove bug-for-bug compatibility. It can only demonstrate that you didn't cause any problems that have been thought of before; it does not demonstrate safety for novel bugs.

Requirement 3 is there because many refactorings can have non-local effects. It is not sufficient to have great tests on the code you are changing. You also need great tests on the code that you are not intending to change, to demonstrate that you didn't. Therefore, until your entire codebase is very highly tested, you will only be able to use the `R` commit designation on new code that is uncalled by your product.

# End-User Documentation
[1]:#end-user-documentation

End user documentation is a feature, bugfix, or refactoring, depending on its nature. Use those codes (including levels of risk) accordingly.

# Small Features and Bug Fixes
[4]:#small-features-and-bug-fixes

Features and bug fixes intentionally change behavior. This makes them much riskier than refactorings. It is not possible to prove that they have only the intended effect. However, small changes are much lower risk for three reasons:

1. It's only possible when the code is well-organized already.
2. It's easy to see the possible side effects of small chunks of code.
3. It's easy to code review, so you are likely to get good reviews.

Therefore, we treat any feature or bug fix as high risk if it changes more than 8 LoC in one commit. This includes test changes.

One good approach to enable small features is to refactor until the feature change is easy, then add it. Then add the feature one piece at a time, with a test for each.

# Living Documentation

We invite you to submit pull requests to help evolve this notation and methodology.
