# Plan 001 — Test coverage for `sin`/`cos` and complete calculator spec

Status: PLANNED · Written against commit `2876bd9`

## Why

`calculator.py` already implements every core function in `specs/calculator-tests.md`
(`add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `mod`), and all 23 tests in
`test_calculator.py` pass. Two functions were added after the spec was written —
`sin(a)` and `cos(a)` at the bottom of `calculator.py` — but they have **no test
coverage** and are **not documented in the spec**. This plan closes both gaps so the
test suite is the complete source of truth for the calculator.

## Current state

`calculator.py` (relevant tail):

```python
def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)
```

`test_calculator.py` imports the functions under test at the top:

```python
from calculator import add, divide, mod, multiply, power, sqrt, subtract
```

Each function has its own `TestCase` class (e.g. `TestAdd`, `TestSqrt`), and
float results use `assertAlmostEqual` (see `TestSqrt.test_non_perfect_square`).

## Steps

### 1. Add `sin`/`cos` to the import line

File: `test_calculator.py`, top of file.

Replace:

```python
from calculator import add, divide, mod, multiply, power, sqrt, subtract
```

with:

```python
from calculator import add, cos, divide, mod, multiply, power, sin, sqrt, subtract
```

Verify: `python -m unittest test_calculator -v 2>&1 | tail -3` → still 23 tests, all OK.

### 2. Add `TestSin` and `TestCos` classes

Append to the end of `test_calculator.py`, before the `if __name__ == "__main__":`
block, following the existing one-`TestCase`-per-function pattern. Use
`assertAlmostEqual` for every assertion (floats), and `math.pi` for the radians
constants:

```python
class TestSin(unittest.TestCase):
    def test_sin_of_zero(self):
        self.assertAlmostEqual(sin(0), 0)

    def test_sin_of_pi_over_two(self):
        self.assertAlmostEqual(sin(math.pi / 2), 1)

    def test_sin_of_pi(self):
        self.assertAlmostEqual(sin(math.pi), 0, places=6)


class TestCos(unittest.TestCase):
    def test_cos_of_zero(self):
        self.assertAlmostEqual(cos(0), 1)

    def test_cos_of_pi_over_two(self):
        self.assertAlmostEqual(cos(math.pi / 2), 0, places=6)

    def test_cos_of_pi(self):
        self.assertAlmostEqual(cos(math.pi), -1)
```

`math` is not imported in `test_calculator.py` yet — add `import math` at the top
alongside `import unittest` if it isn't already there.

Verify: `python -m unittest test_calculator -v` → **29 tests, all OK**, including
`TestSin` and `TestCos`.

### 3. Update the spec

File: `specs/calculator-tests.md`. Add the same test cases the spec's other
functions document, keeping the existing formatting (`### sin`, `### cos` sections
with numbered cases):

- `sin`: 1. sin(0)=0 2. sin(π/2)=1 3. sin(π)≈0 (use `assertAlmostEqual`)
- `cos`: 1. cos(0)=1 2. cos(π/2)≈0 3. cos(π)=-1

Update the Deliverable line's "~30 assertions" to "~35 assertions".

## Done criteria (all must hold)

- [ ] `python -m unittest test_calculator -v` runs **29 tests** and reports `OK`
- [ ] `grep -c "def test_" test_calculator.py` → `29`
- [ ] `specs/calculator-tests.md` documents `sin` and `cos`
- [ ] `git diff --stat` shows changes only in `test_calculator.py` and `specs/calculator-tests.md`

## Boundaries

In scope:
- `test_calculator.py` (import line, two new test classes, `import math`)
- `specs/calculator-tests.md`

Out of scope — do NOT touch:
- `calculator.py` (`sin`/`cos` already exist; the plan does not change production code)
- `README.md`, `test.js`, `fibonacci.js`, text files
- No new files, no new dependencies (stdlib `unittest` only)

## Escape hatches

- If `sin` or `cos` is **missing** from `calculator.py` (e.g. the working tree was
  reset), STOP and report — the plan assumes both exist and pass `math.sin`/`math.cos`.
- If the test run reports anything other than 29 passing tests, STOP and report the
  failure output instead of editing production code to force a pass.

## Test plan

The tests added in step 2 are the deliverable. Run `python -m unittest test_calculator -v`
and confirm every `TestSin`/`TestCos` case shows `ok`.

## Maintenance note

`sin`/`cos` take **radians**, not degrees — the tests hard-code radian constants
(`math.pi`) so a future degrees/radians switch in `calculator.py` would break them
deliberately. If a degree-based variant is ever added, it must be a new function
(e.g. `sind`/`cosd`), not a changed default, or these tests will fail by design.
