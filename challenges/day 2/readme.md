# Day 2 — Challenges

This folder contains Day 2 challenge files.

## Notes

- Requires Python 3.x. Use quotes around the filename if your shell requires them because of spaces.
- Inspect the script for usage or required inputs.

## Challenge Description

`smart reg system.py` validates a student registration form: it checks `student_id` format, `email`, `password` strength, and a `referral` code. It prints `APPROVED` if all checks pass, otherwise `REJECTED`.

## Approach / Logic Used

- Check `password` length/format: expects a capital letter at the start and at least one digit.
- Check `student_id` begins with `CSE-` followed by three digits.
- Validate `email` contains `@` and `.`, does not start/end with `@`, and ends with `.edu`.
- Validate `referral` starts with `REF`, has two digits, and ends with `@`.
- Use a `status` variable set to `APPROVED` and switch to `REJECTED` on the first failing rule.

## Algorithm / Steps

1. Read `student_id`, `email`, `password`, and `referral` from input.
2. Initialize `status` = `APPROVED`.
3. Validate `password` (presence of characters, starts with an uppercase letter, contains at least one digit); set `status` = `REJECTED` on failure.
4. Validate `student_id` pattern `CSE-XXX` where `X` are digits; set `status` = `REJECTED` on failure.
5. Validate `email` contains `@` and `.`, not start/end with `@`, and ends with `.edu`; set `status` = `REJECTED` on failure.
6. Validate `referral` format (`REF` + two digits + `@` at end); set `status` = `REJECTED` on failure.
7. Print final `status`.