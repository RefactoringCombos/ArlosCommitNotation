# Migrating from V1 to V2

Where `x`/`X` is an intention code:

| V1     | V2    |
|--------|-------|
| `x - ` | `. X` |
| `X - ` | `^ X` |
| `X!!`  | `! X` |
| `X**`  | `@ X` |

## Notes

- Consistent casing; lower case becomes `.` and upper case becomes `^`. Neither combine risk and intention in the same place.
- Risk before intention
- Risk is a single character
- `*` becomes `@`
