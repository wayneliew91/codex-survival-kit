# Regression Contract

Use a contract only for behavior plausibly affected by the current change. Keep it small enough to test directly.

## Contract fields

```text
Surface:
Authority:
Protected behavior:
Inputs / preconditions:
Expected output or effect:
Identity / naming constraints:
Data invariants:
Historical compatibility:
Targeted proof:
Broader completion gate:
Supersession status: NONE | SUPERSESSION(<evidence>)
```

## Evidence selection

Prefer evidence that directly establishes the behavior being protected. Typical sources include:

- tests that intentionally encode accepted behavior;
- current accepted specifications or interface contracts;
- release notes tied to a verified fix;
- issue/PR decisions with explicit acceptance;
- explicit current user requirements.

Do not rank evidence by timestamp alone. Generated files, stale tests, exploratory notes, and implementation accidents can be newer without being authoritative.

## Supersession test

Treat a rule as superseded only when evidence clearly replaces it, for example:

- an explicit requirement says the former behavior is retired/replaced;
- an accepted change documents a compatibility break;
- a versioned contract names the replacement semantics.

If replacement is unclear, keep the conflict visible and do not silently choose the convenient behavior.

## Verification ladder

- `VERIFIED`: targeted proof for every material contract item plus required broader gates.
- `PARTIALLY_VERIFIED`: some contract items directly proved; remaining items identified.
- `UNVERIFIED`: no direct proof for the protected behavior.
- `FAILED`: direct evidence contradicts the contract.
