# Movement-Oriented Branches

This branch model is designed to clarify intention and speed up code review. It also improves safety by separating goals.

Consider our code history like a piece of classical music. It is long, but there are themes. It explores one idea for a period of time, then moves on to the next idea. These ideas are called movements in classical music. In code, we convey them using branches.

We convey movements by using the following 3 behaviors.

1. Make a new branch for each idea. Keep the ideas small.
2. Use the Risk Aware Commit Notation on the branch.
3. Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) in the merge commit. Convey the core idea for the movement.

There is also one optional behavior:

* (optional) Indicate risky commits in the merge commit, using a `Risky changes` commit trailer. 

## Example

Commit history looking at main with side branches collapsed (only shows merge commits):
```
feat: authenticate with multiple social auth providers.
feat: calculate sales tax using third-party service
chore: update dependencies
refactor: isolate payment processing from checkout flow
```

Merge commit details:
```
feat: authenticate with multiple social auth providers.

Authorization now prompts the user in two phases. First we ask for
their username or email, which we use to find the right provider.
Then we send them through that provider's auth mechanism.

Risky changes:
  a5de73: ! r Switched algorithm for email categorization.
  e67c8e: ! F Split login UX into 2 steps.
```

Commit history for a side branch:
```
feat: authenticate with multiple social auth providers.
^ F Add Github and Facebook OAuth providers
^ F Add Microsft OAuth provider
^ F Allow / require the user to choose which provider to use when creating a new account - still only one option.
. r convert 1 to many-of-one for providers
! r Switched algorithm for email categorization
. t add tests for email categorization
. r extract method
. r rename
. r extract method
! F Split login UX into 2 steps.
. t test account creation failure
. t test account creation success
. t test login failure
. t test login success
. f LocalMemoryAuthenticator allows easy testing for code that uses auth providers (simulator)
. t extract commonalities to test providers through an interface
. t test the default provider (Google). Add these to the platform test suite.
. r extract method; move method
. r extract method; move method
. r introduce parameter object (oauth provider)
. r extract method
. r extract method
```
