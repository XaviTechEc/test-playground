# Test Plan — calculator.py (TDD)

## Framework

Default: stdlib `unittest` (no install, matches "no package manager" setup).
Alternative: `pytest`.

## Test cases by function

### `add`

1. positive + positive (2+3=5)
2. negative + positive (-1+1=0)
3. zero + positive

### `subtract`

1. positive − positive (5-3=2)
2. result negative (3-5=-2)
3. zero − positive

### `multiply`

1. positive × positive (2×3=6)
2. negative × positive (-2×3=-6)
3. × zero = 0

### `divide`

1. exact division (10/2=5)
2. non-integer result (1/4=0.25)
3. negative ÷ positive
4. raises `ZeroDivisionError` when `b==0`

### `power`

1. square (2**3=8)
2. exponent 0 = 1
3. negative exponent (2**-1=0.5)

### `sqrt`

1. perfect square (sqrt(16)=4)
2. non-perfect (sqrt(2)≈1.414, use `assertAlmostEqual`)
3. sqrt(0)=0
4. raises `ValueError` when `a<0`

### `mod`

1. exact (10%3=1)
2. larger % smaller (2%5=2)
3. raises `ZeroDivisionError` when `b==0`

### `sin`

1. sin(0)=0
2. sin(π/2)=1
3. sin(π)≈0 (use `assertAlmostEqual`)

### `cos`

1. cos(0)=1
2. cos(π/2)≈0 (use `assertAlmostEqual`)
3. cos(π)=-1

## Structure

Single file `test_calculator.py` (or `tests/` if preferred):

- One `TestCase` per function.
- Import via `from calculator import ...`.
- Error cases: `assertRaises(ZeroDivisionError)` / `assertRaises(ValueError)`.
- Float results: `assertAlmostEqual`.
- Run: `python -m unittest test_calculator -v`.

## TDD flow (red → green → refactor)

Since `calculator.py` already implements everything, the TDD cycle applies as:

1. Write each test first (fails only if behavior differs from spec).
2. Confirm against current impl.
3. Refactor only if a test exposes a gap (none expected — code already handles errors).

No production code changes needed unless a test fails.

## Deliverable

One file `test_calculator.py`, ~35 assertions, no dependencies.
