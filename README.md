# Arlo's Commit Notation

## Upper case: Deliberate behavior changes

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| F       | Feature                                                   |
| B       | Bug                                                       |

## Lower case: Low risk

| Prefix  | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| c       | comments (add/delete)                                        |
| d       | developer documentation changes (not end-user facing<sup>[1]</sup>)        |
| e       | environment (non-code) changes that affect development setup |
| t       | Test only                                                    |
| r       | Provable Refactoring<sup>[2]</sup>                 |
| a       | Automated formatting                                         |

## Three characters: The danger zone!

| Prefix  | Meaning                                                   |
| ------- | --------------------------------------------------------- |
| !!!     | non-provable refactoring                                  |
| ***     | does not compile intermediate step                        |

# Description

[Arlo's](https://twitter.com/arlobelshee) Commit Notation is a way of making small commits that show the risk involved in each step. It is particulary useful in legacy systems. 

# Provable Refactorings
[2]:#provable-refactorings

If you can get a series of commits that is all lowercase commits, you can deploy without the need for Regression Testing, or lengthy conversations about accepting the pull request to trunk.
[Recipes Here](https://github.com/InnovatingTeams/provable-refactorings)

A provable refactoring requires the burden of proof. The main methods of proof are
* automated refactoring via tool
* Scripted manual refactoring, using the compiler to verify each step
* DANGER: Very Highly tested code, with the tests providing proof

Note that only the first two levels can prove bug-for-bug copmatability. The last can only demonstrate that you didn't cause any problems that have been thought of before; it does not demonstrate safety for novel bugs.

# End-User Documentation
[1]:#end-user-documentation

End user documentation is a feature, bugfix, or refactoring, depending on its nature. Use those codes (including levels of risk) accordingly.

# Living Documentation

We invite you to submit pull requests to help evolve this notation and methodology.
