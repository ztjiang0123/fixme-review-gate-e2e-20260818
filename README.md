# Fix Me review-gate E2E fixture

This repository is an isolated IntentLab test fixture. Its default branch
requires one approving pull-request review. The intentionally long parameter
list in `src/review_gate/shipping.py` seeds one Code Health signal for testing
the Fix Me approval-required state.
