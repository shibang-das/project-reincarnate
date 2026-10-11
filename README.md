# Invoice Service

This is a small existing Python codebase. Treat it like an interview repository: inspect it first, run the tests, trace the failing behavior, and make the smallest safe fix. Do not rewrite everything.

## Setup

Python 3.10+

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Task

A customer reports that invoice totals are sometimes wrong and some invalid invoices are accepted. Investigate the code and tests, fix the defects, and add regression tests. Preserve the public function signatures unless there is a strong reason not to.

Expected workflow:
1. Read `invoice_service/` and `tests/`.
2. Run `pytest -q` and inspect failures.
3. Explain the root cause before changing code.
4. Implement a minimal fix.
5. Add tests for edge cases and rerun the suite.

Do not look for a hidden answer file—there isn't one. After you finish, send me your diagnosis, patch, and test output and I'll review it like an interviewer. Then I'll add a requirement change.
