# Day 3 — Challenges

This folder contains Day 3 challenge files.

## Challenge Description

The script reads a registration number to determine a bonus value, then reads marks for multiple students. It validates marks, applies the bonus for valid marks, categorizes performance (Excellent, Very Good, Good, Average, Fail), and reports original/updated lists and counts.

## Approach / Logic Used

- Use parity of the registration number to set `bonus` (even -> 2, odd -> 1).
- Read `n` marks into an `original_marks` list.
- For each mark: if invalid (<0 or >100) mark as `Invalid`; otherwise add bonus, categorize, update counts and `updated_marks`.
- Track total valid and failed students and print summaries.

## Algorithm / Steps

1. Read `reg` (registration number); set `bonus` = 2 if `reg` is even else 1.
2. Read `n` (number of students).
3. For `n` times read each `mark` and append to `original_marks`.
4. For each `mark` in `original_marks`:
   - If `mark` < 0 or > 100 -> category = `Invalid`, append original mark to `updated_marks`.
   - Else: increment `valid_count`, compute `processed_mark = mark + bonus`, append to `updated_marks`.
   - Categorize `processed_mark` into thresholds: >=90 Excellent, >=75 Very Good, >=60 Good, >=40 Average, else Fail (increment `fail_count`).
   - Print each student's category.
5. Print `Original Marks List`, `updated Marks List`, `Total Valid students`, and `Total Failed students`.

## Notes

- Requires Python 3.x. Inspect the script for exact input prompts.
