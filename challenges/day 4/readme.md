# Day 4 — Challenges

This folder contains Day 4 challenge files.

## Challenge Description

The script reads multiple activity scores and a registration number. It classifies scores into Low, Medium, High, and Critical risk buckets, ignores negative entries, then applies a personalized filter that removes either all Low or all High entries depending on the parity of the registration number. Finally it prints the categorized lists and a summary report.

## Approach / Logic Used

- Read `n` scores and store in a list; ignore negative scores.
- Classify valid scores into four buckets using threshold ranges.
- Use registration number parity (`D % 2`) to determine whether to remove all Low (even) or all High (odd) scores from the final report.
- Maintain counts for valid, ignored, and removed entries and print lists before and after the personalized filter.

## Algorithm / Steps

1. Read `n` (number of activity scores) and then read `n` integer `score` values.
2. Read registration number `D`.
3. For each `score`:
   - If `score` < 0: increment `ignored_entries`.
   - Else: increment `valid_entries` and place `score` into one of the buckets:
     - `<= 30`: Low Risk
     - `<= 60`: Medium Risk
     - `<= 100`: High Risk
     - `> 100`: Critical Risk
4. Print bucket contents (before personalized filter).
5. If `D` is even: remove all Low Risk entries; else remove all High Risk entries. Track `removed_entries`.
6. Print bucket contents after filter and the final summary: valid, ignored, removed counts.

## Notes

- Requires Python 3.x. The script uses fixed-size lists preallocated by `n` and prints results to stdout.
