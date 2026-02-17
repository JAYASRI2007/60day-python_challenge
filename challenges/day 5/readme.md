# Day 5 — Challenges

This folder contains Day 5 challenge files.

## Challenge Description

The script simulates an Emergency Resource Dispatch Analyzer used during disaster drills. 
It reads multiple resource request values, classifies them into demand categories, 
handles invalid inputs, and applies a personalized filtering rule (PLI) based on 
the user's birth year. Finally, it generates a dispatch report summarizing 
categorized requests and statistics.

## Approach / Logic Used

- Read `n` resource requests using a for loop and store them in a list.
- Process each request using conditional statements:
  - Negative values → Invalid Requests
  - Zero → No Demand (ignored)
  - 1–20 → Low Demand
  - 21–50 → Moderate Demand
  - >50 → High Demand
- Maintain a counter for valid requests (excluding invalid and no-demand entries).
- Compute Personalized Logic Index (PLI) using birth year:
  
  PLI = BirthYear % 3

- Apply filtering rules based on PLI:
  - PLI = 0 → Remove all Low Demand requests
  - PLI = 1 → Remove all High Demand requests
  - PLI = 2 → Keep only Moderate Demand requests
- Track number of removed requests.
- Print categorized lists and final dispatch summary.

## Algorithm / Steps

1. Read `n` (number of resource requests).
2. Read `n` integer request values and store them in a list.
3. For each request:
   - If request < 0 → Add to Invalid Requests
   - Else if request == 0 → Ignore (No Demand)
   - Else if request <= 20 → Low Demand
   - Else if request <= 50 → Moderate Demand
   - Else → High Demand
4. Read Birth Year.
5. Compute PLI = BirthYear % 3.
6. Apply Personalized Filtering Rule:
   - Rule A → Remove Low Demand
   - Rule B → Remove High Demand
   - Rule C → Keep only Moderate Demand
7. Print Dispatch Report:
   - Birth Year
   - PLI Value
   - Categorized Demand Lists
   - Invalid Requests
   - Valid Request Count
   - Removed Request Count

## Notes

- Requires Python 3.x.
- Uses lists, for loops, and conditional statements only.
- No list comprehension, dictionaries, sets, or built-in aggregation functions.
- Output varies per student due to personalization logic (PLI).
