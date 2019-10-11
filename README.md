# Arlo's Commit Notation

## Upper case: Deliberate behavior changes

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| F       | Feature (<= 8 LoC<sup>[4]</sup>)                        |
| B       | Bug (<= 8 LoC<sup>[4]</sup>)                              |

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
| F!!       | Feature (> 8 LoC<sup>[4]</sup>)                             |
| B!!       | Bug (> 8 LoC<sup>[4]</sup>)                                   |
| ***     | does not compile intermediate step                        |

# Description

[Arlo's](https://twitter.com/arlobelshee) Commit Notation is a way of making small commits that show the risk involved in each step. It is particulary useful in legacy systems. 

# Provable Refactorings

If you can get a series of commits that is all lowercase commits, you can deploy without the need for Regression Testing, or lengthy conversations about accepting the pull request to trunk.
[Recipes Here](https://github.com/InnovatingTeams/provable-refactorings)

A provable refactoring requires the burden of proof. The main methods of proof are
* automated refactoring via tool
* Scripted manual refactoring, using the compiler to verify each step
* DANGER: Very Highly tested code, with the tests providing proof

Note that only the first two levels can prove bug-for-bug copmatability. The last can only demonstrate that you didn't cause any problems that have been thought of before; it does not demonstrate safety for novel bugs.

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
