# Incremental learning and adoption path

For a team that has never tried disciplined refactoring there is a steep learning curve to adopt this system.

To reduce that challenge, here we describe the tiniest increments to learning and adopting Arlo's Commit Notation. This way you can get used to one idea before getting overwhelmed by the next idea, and get a quicker return on the learning investment.

Expect some disagreement and confusion in the team throughout this process, as people shift their thinking. As you find agreement, write down your new norms in your team agreements. Give feedback to Arlo's Commit Notation about how it could be been clearer for you.

Hint: this all goes much more smoothly with Mob/Ensemble Programming ([Promiscuious Pairing](https://csis.pace.edu/~grossman/dcs/XR4-PromiscuousPairing.pdf) is also pretty good) to share knowledge, increase "insights per hour", and shift norms more quickly.

Hint: a good technical coach can be a huge help for your team to learn and adopt these skills.

## 1. Working in a short-lived branch

While Trunk-Based Development directly in `main` is good for keeping everyone's work in sync and reducing merges, a short-lived branch lets you document the steps in your development process, telling a story to reviewers and future readers of your changes. 1 day is a good maximum lifetime for a branch (shorter is better), enabling incremental commits without incurring most of the risks of long-lived branches.

If you're in a context where code review is part of the flow of work, teach reviewers how to look at the individual branch commits as an option that may be easier than viewing the whole change all at once. Mention this option in the description of the final Merge Request, e.g. "see the individual commits in the branch for more details".

Depending on your VCS solution, you will need to find a way to keep these details visible after merging to main, such as `rebase` + `merge --no-ff`.

### Example commit history

```
Implement automatic log-off
Clean up the login module
```

One benefit of working this way is that it's easier to provide rich, detailed descriptions for the smaller increments in a branch than for the whole ball of changes.

In legacy code, we often see code that looks "weird" but we don't know if was deliberately made this way for a subtle reason, or the dev just didn't get around to cleaning it up. Incremental work with rich descriptions can be really helpful for future readers trying to understand why the code ended up like this. 

## 2. Tag refactorings with `@ r`

If a change contains only refactoring, indicate that by prefixing the change description with `@ r `.

The refactoring need not be especially disciplined. This is just about separating refactoring from non-refactoring in your commit history.

Folks on your team probably have [multiple working defintions of refactoring](https://jay.bazuzi.com/DefinitionsOfRefactoring/), and this is an invitation to examine those defintions and find a shared understanding.

Refactorings often have a large diff even though they don't change behavior and are out of proportion with the conceptual size of the change. For example "rename A to B" is one small idea but every line that references `A` will be affected. If combined with deliberate behavior changes that will make reading the total diff difficult. Separating refactorings into their own commits will make code review easier. You should be able to scan the commit history and easily see which are refactorings and which are not.

### Example commit history

```
Implement automatic log-off
@ r Remove duplication in login module
@ r Rename a bunch of stuff for clarity
```

For a future reader of the code trying to understand how the code got this way, if you're looking for a deliberate behavior change you know you can ignore `@ r` changes; if you see a behavior change in a commit marked `@ r` you know it was accidental.

## 3. Pick up easy wins

Once the team has learned the above practices, the following tags are easy to adopt.

- `. t` for test-only changes
- `. a` for auto-formatting
- `! R` for named refactorings

### Example commit history

```
. t - fill in missing tests for existing login code
! R Extract Method
. a - autoformat with prettier
```

If you haven't already, this is a good time to add automatic code formatting to your CI checks, and bring all existing code in to compliance with that formatting.

## 4. Tag Features and Bug Fixes with `@ F` and `@ B`.

Make a team agreement to categorize commits and tag with one of the above.

It may be a good idea to allow `@ @` (uncategorized) in certain contexts. One example is "checkpointing", where you have some in-progress experimental changes on one machine and want to try them on another machine or share them with a coworker. 

At this point you can considering adopting a regex check to ensure that all commits are tagged. See https://github.com/RefactoringCombos/ArlosCommitNotation/issues/29.

### Example commit history

```
@ F Implement automatic log-off
@ r Remove duplication in login module
@ r Rename a bunch of stuff for clarity
```

## 5. Refactor to prepare code for behavior change

> Make the change easy (warning: this may be hard), then make the easy change. -- Kent Beck

For each feature or bug fix, practice replacing "how can I get this behavior change to fit in to the current design?" with "what design would make it really easy to implement this feature in a natural way?" and "what small refactorings would it take to get from here to there?". You're looking for `! r`-style, single named refactorings. Commit histories will start to look like a series of refactorings followed by a deliberate behavior change.

### Example commit history

```
@ F Automatically log-off when idle
! r Introduce parameter
! r Import nodatime
! r Merge duplicate code
! r Extract Method
```

This also gives you the option of merging to `main` before your feature or bug fix is complete. For example, on one day you might do a bunch of `! r` refactorings, get them approved and merged quickly thanks to the above practices, then continue towards your feature or bug fix the next day.

## 6. Safe Refactoring

Can your IDE safely execute a refactoring? If so, you can use `. r`. This is great for code review, as reviewers can now skim some changes instead of examining them carefully for correctness issues. This means means you can get your code review results back even more quickly.

Where your IDE is unable to provide the required level of safety, look at [recipe-based refactorings](https://github.com/InnovatingTeams/provable-refactorings). 

Once your team has gotten comfortable with `. r`, consider changing your code review and delivery protocols to allow lower-case (safe) changes to skip some/most/all of those requirements. This has several benefits, including creating an incentive for developers to work in this safe way.

Note that this level of safety is hard to get in dynamic languages. If that's your context, you may need to instead make the investment in comprehensive test coverage to unlock `^ r`.

### Example commit history

```
. r Merge identical methods
. r Rename local variables
. r Extract Method
```

## 7. Small features and bug fixes

Once you get in familiar with refactoring in preparation for a feature, you can further reduce risk by refactoring to the point where a feature or bug fix only requires a small code change. That unlocks `^ F` and `^ B`.

### Example commit history

```

^ F Automatically log-off when idle
. r <more refactorings>
. t <fill in a missing test>
. r <more refactorings>
. r <more refactorings>
! r <a refactoring we couldn't make safe>
. r <more refactorings>
. t <fill in a missing test>
. r <more refactorings>
! r <a refactoring we couldn't make safe>
. r Merge duplicate code
. r Extract Method
```

# TDD with ACN

In a strict Test-Driven Development cycle almost all commits are either a new test or a refactoring. When using ACN:

1. Write a new failing test (Red)
1. Make it pass (Green)
1. Commit with `. t <name of the new test>`.
1. Refactor.
1. Commit each refactoring.
    - If the refactoring is executed with a known safe tool or recipe, use `. r`.
    - If this is new, un-called code and you have been doing TDD since the start, you probably have the test coverage to use `^ r`.
    - If you are "triangulating", converting special-case code to a generalized algorithm, use may need to use `@ R`.

### Example commit history

```
^ r replace algorithm
^ F FizzBuzz of 3 is "Fizz"
^ F FizzBuzz of 2 is "2"
. r rename parameter
^ F FizzBuzz of 1 is "1"
```

# Alternatives

## All-at-once

If working as an ensemble with a highly skilled and capable technical coach, then bring in all of the practices at once and let the coach guide the team to use them as the work requires.

## Safety First

Start by introducing `. r` and suggesting incremental work in a branch. Allow these kinds of changes a fast track through review and release. Build from there.

## Categorize first

This approach scales up to larger multi-team organizations where there's not enough hands-on coaching capacity to do it all at once.

Make the requirement that all changes must be categorized in to one of Feature (`@ F`), Bug Fix (`@ B`), or Refactoring (`@ r`) and tagged as such. No other change to developer behavior is required. `@ @` is an escape valve, e.g. for checkpointing work to move it to another machine.

If a change contains both feature and bug fix work, use `@ F`.

If a change contains both refactoring and non-refactoring work, use the appropriate non-refactoring tag.

Invite developers/pairs/ensembles to use other risk and intent annotations as they see fit, and praise when that is done, but don't require it at first.

Roll out in these increments:

1. Categorize (`@ F` / `@ B` / `@ r` / `@ @`)
2. Corral Risk (`! F`, `! B` / `! r`)
3. Validated (`^ F` / `^ B` / `^ r`)
4. Safe (`. r`)
