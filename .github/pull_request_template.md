## Problem

What recurring failure mode does this change address?

## Pressure scenario

What task exposes the problem? Was it live-tested or is it a forward-test definition?

## Change

What changed, and why is the default context no larger than necessary?

## Verification

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/validate_skills.py .`
- [ ] Relative links checked
- [ ] No private repository content, credentials, customer data, or sensitive local paths
- [ ] Live Codex behavior replay described if available; otherwise explicitly marked not run
