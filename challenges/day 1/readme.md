# Day 1 — Challenges

This folder contains Day 1 challenge files.

## Notes

- Requires Python 3.x. Adjust the command if you use a virtual environment or `python3` on your system.
- Inspect `valid.py` for any required input or usage details.

## Challenge Description

`valid.py` reads user inputs (name, email, mobile number, age) and checks whether the user profile meets a set of validation rules. It prints `User Profile is VALID` or `User Profile is INVALID`.

## Approach / Logic Used

- Validate `name` for leading/trailing/insufficient spaces.
- Validate `email` contains `@` and `.` and does not start with `@`.
- Validate `mobile` is 10 digits, numeric, and does not start with `0`.
- Validate `age` is between 18 and 60 inclusive.
- Use a single `status` flag toggled to `INVALID` on any failing check; final output depends on the flag.

## Algorithm / Steps

1. Read `name`, `email`, `mobile`, and `age` from input.
2. Initialize `status` = "VALID".
3. If `name` has leading/trailing space or fewer than two words, set `status` = "INVALID".
4. If `email` missing `@` or `.`, or starts with `@`, set `status` = "INVALID".
5. If `mobile` length != 10, contains non-digits, or starts with `0`, set `status` = "INVALID".
6. If `age` < 18 or > 60, set `status` = "INVALID".
7. Print `User Profile is VALID` if `status` remains `VALID`, otherwise print `User Profile is INVALID`.