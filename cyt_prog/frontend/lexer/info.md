# CYT Lexer — Design Specification

## Overview

The lexer transforms a source string into a linear stream of tokens.
It operates in a **single pass**, processes each character **exactly once**, and emits a deterministic token sequence suitable for parsing.

The lexer is intentionally minimal and currently targets a very small Python-like subset
(e.g. `a = 1`).  
The architecture, however, is explicitly designed to scale without structural rewrites.

---

## Core Principles

1. Exactly one cursor controls progress through the source.
2. No character is processed more than once.
3. Token ranges never overlap.
4. Token positions (line/column) are exact.
5. Scanning determines token *extent*, not semantics.
6. Structural tokens are never produced by scanning.
7. Scan termination is implicit (predicate-based).
8. Progress is committed atomically.
9. EOF is always present.

Violating any of these principles constitutes a lexer bug.

---

## Cursors and Authority

### Main Cursor (`c`)

The main cursor is the **sole authority** over lexer progress.

- `c` always points **at** the current character.
- `line` and `col` describe the position of `c`.
- Only `c` may:
  - emit tokens
  - update global state (`line`, `col`)
  - decide when lexing terminates

`c` is never reconciled with other cursors.  
If `c` moves, that movement is final.

---

### Temporary Cursor (`tc`)

The temporary cursor is **strictly subordinate** to the main cursor.

- `tc` exists only while scanning a token whose length cannot be known a priori.
- `tc`:
  - never emits tokens
  - never updates global state
  - never advances the source independently
- `tc` exists solely to determine **how far a token extends**.

`tc` is disposable and has no semantic authority.

---

### Cursor Commitment Rule

When scanning completes:

- Progress is committed **atomically** by assigning:

  ```
  c = tc
  ```

There is:
- no reconciliation
- no skipping
- no catch-up logic

This guarantees that characters belonging to a token are never reprocessed.

---

## Token Categories

### Structural Tokens (Single-Character)

Structural tokens are determined directly by `c` and require **no scanning**.

Examples:
- `NEWLINE` (from `'\n'`)
- assignment operator (`'='`)
- punctuation and delimiters (future)
- `EOF`

Structural tokens:
- are emitted immediately
- always correspond to exactly one character
- are never produced by `tc`

---

### Scan-Based Tokens (Variable Length)

Scan-based tokens require scanning to determine their extent.

Examples:
- `NAME`
- `INT` / `VALUE`
- comparison operators (future)
- strings (explicitly not supported yet)

Scan-based tokens:
- are initiated by `c`
- scanned by `tc`
- emitted only after scanning completes
- commit progress via `c = tc`

---

## Scanning Model (Core Invariant)

For a scan-based token of kind **K**, scanning proceeds as follows:

> Scanning continues while the predicate `allowed(K, ch)` is true.  
> Scanning terminates on the first character for which the predicate is false.

Important properties:
- There are no hard-coded terminators.
- There are no special characters inside scanning.
- `tc` has no concept of whitespace, newline, or syntax.

Termination is **implicit** and purely predicate-based.

---

### Example: NAME Token

Source:
```
abc@d = 1
```

Predicate:
```
allowed(NAME, ch) == True  for letters, digits, and '@'
```

Scan result:
```
NAME("abc@d")
```

The character `'@'` is accepted by policy and may trigger a warning,
but does not terminate the scan.

---

## NEWLINE Semantics

The newline character `'\n'`:

- belongs to the **current line**
- has a concrete `(line, col)` position
- is always emitted as a `NEWLINE` token by `c`

`tc`:
- never emits `NEWLINE`
- never treats `'\n'` specially
- terminates scanning if `'\n'` fails the predicate

### Example

Source:
```
abc
def
```

Character positions:
```
a  -> (1,1)
b  -> (1,2)
c  -> (1,3)
\n -> (1,4)
d  -> (2,1)
```

Processing:
1. `tc` scans `abc`
2. `tc` stops at `'\n'`
3. `c = tc`
4. `c` emits `NEWLINE` at `(1,4)`
5. `line += 1`, `col = 1`
6. lexing continues

There is no deferred state and no special casing.

---

## Whitespace Policy

Whitespace characters (space, tab for now):

- are not tokens
- are not errors
- are not warnings
- are consumed silently
- advance `col`

Whitespace does not participate in scanning logic and has no semantic meaning at this stage.

---

## Error and Warning Model

### Hard Lexer Errors

A hard lexer error is raised when:

- `c` encounters a character that cannot start any token
- the lexer cannot meaningfully proceed

Effect:
- tokenization aborts
- compilation stops immediately

---

### Soft Lexer Errors (Warnings)

A soft lexer error represents a **warning**, not a failure.

Raised when:
- `tc` encounters a character that is unusual but explicitly permitted
- e.g. `'@'` inside an identifier

Effect:
- token remains valid
- scanning continues
- warning is recorded for diagnostics

This is a **language policy**, not error recovery.

---

## Token Validity Guarantees

- All emitted tokens are:
  - complete
  - non-overlapping
  - structurally valid
- Tokens may be *unusual* but are never partially invalid.
- Any later rejection is semantic, not lexical.

---

## EOF Handling

- EOF is a **logical token**, not a character.
- EOF is appended:
  - exactly once
  - after the source is exhausted
  - regardless of trailing newline
- Empty input produces:
  ```
  [EOF]
  ```

This avoids empty token streams entirely.

---

## Strings (Explicitly Deferred)

Strings are **not supported** in the current lexer.

Reason:
- strings invert the acceptance model
- strings require mode-based scanning
- strings may legally contain newlines

Supporting strings will require:
- a dedicated scanning mode
- different termination rules
- escape semantics

This is acknowledged and intentionally postponed.

---

## Global Invariants (Summary)

1. Only `c` controls progress
2. No character is processed twice
3. No token overlaps another
4. Line/column tracking is exact
5. `tc` determines extent only
6. Structural tokens are never scanned
7. Scanning terminates via predicates
8. Progress commits via `c = tc`
9. EOF always exists

---

## Final Notes

This lexer design is:

- minimal
- deterministic
- extensible
- structurally sound

If implemented according to this document, no additional bookkeeping,
reconciliation logic, or special cases should be required.
