# FizzBuzz Python Example Design

## Goal

Add a self-contained Python example in `fizzbuzz.py`. Its main function,
`fizzbuzz`, should generate standard FizzBuzz results, print them, and return
them for reuse.

## Interface

`fizzbuzz(n)` accepts a positive integer `n` and processes the numbers from 1
through `n`:

- Multiples of both 3 and 5 become `FizzBuzz`.
- Multiples of 3 become `Fizz`.
- Multiples of 5 become `Buzz`.
- All other values remain numbers.

The function prints one result per line and returns the complete list. Its
docstring will document the parameter, return value, and behavior. Invalid
inputs will raise `ValueError` with a clear message.

## Direct execution

When run as `python3 fizzbuzz.py`, the file will call `fizzbuzz(15)` so the
example demonstrates all standard cases. Importing the file will not print
anything automatically.

## Verification

Add a lightweight Python test script covering the standard sequence, printing
and return behavior, and invalid input. Run it with the repository's available
Python interpreter; no package manager or test framework is required.
