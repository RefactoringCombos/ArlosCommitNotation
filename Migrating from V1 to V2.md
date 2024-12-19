# Migrating from V1 to V2

Where `x`/`X` is an intention code:

| V1     | V2    |
|--------|-------|
| `x - ` | `. X` |
| `X - ` | `^ X` |
| `X!!`  | `! X` |
| `X**`  | `@ X` |

## Notes

- We now split risk and intention into 2 different characters.
- The new system uses consistent casing for the intention.
  * The old system's lower case becomes `.` and upper case becomes `^` (or higher).
- Risk is always before intention
- Risk is a single character
- `*` becomes `@`
- There are no more doubled characters, so we avoid shell interactions (old `!!`) and the appearance of cursing (old `**`).
