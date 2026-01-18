# 🌱 Growing Code: Python Fundamentals Through Garden Data

An introductory Python project focused on core programming foundations through garden-themed exercises. This module builds practical skills in expressions, variables, functions, control flow, iteration, recursion, formatting, and basic type annotations.

---

## 📋 Project Overview

Growing Code is a progressive learning project that turns fundamental Python concepts into practical skills. Each exercise is self-contained and emphasizes clear, readable, and testable code.

What this module develops:
- Write single-responsibility functions that handle console I/O
- Work with numbers and strings to compute areas and totals
- Make decisions using conditional logic
- Repeat work using iteration and recursion
- Produce consistent, human-readable outputs
- Introduce type hints to clarify function contracts (Exercise 7)

---

## 🎯 Key Concepts Learned

1. **Expressions & Variables**
	- Store and manipulate values for real-world tasks (areas, totals)

2. **Input/Output (I/O)**
	- Read user input safely within scope and print formatted results

3. **Functions**
	- Define, name, and structure behavior as standalone functions

4. **Control Flow**
	- Use `if/else` and comparisons to make decisions (age checks, reminders)

5. **Iteration**
	- Use `range()` and loops for counting and accumulation

6. **Recursion**
	- Model repeated actions via function self-calls with base/step cases

7. **Formatting & Summaries**
	- Combine multiple inputs into clear, consistent output messages

8. **Type Hints (Intro)**
	- Annotate parameters and return types to document intent (ex7)

---

## 📁 Project Structure

```
Python_Module_00/
├── ex0/
│   └── ft_hello_garden.py            # Greeting and simple output
├── ex1/
│   └── ft_plot_area.py               # Area computation from length/width
├── ex2/
│   └── ft_harvest_total.py           # Sum across multiple days
├── ex3/
│   └── ft_plant_age.py               # Conditional readiness check
├── ex4/
│   └── ft_water_reminder.py          # Watering reminder logic
├── ex5/
│   ├── ft_count_harvest_iterative.py # Counting via iteration
│   └── ft_count_harvest_recursive.py # Counting via recursion
├── ex6/
│   └── ft_garden_summary.py          # Summary output formatting
├── ex7/
│   └── ft_seed_inventory.py          # Type-annotated inventory output
└── README.md
```

---

## 📚 Exercise Breakdown

### Exercise 0: Hello Garden
**File:** [ex0/ft_hello_garden.py](ex0/ft_hello_garden.py)

**What You Learn:**
- Basic console output and string handling
- Function structure with clear naming

**Behavior:**
- Prints a welcome message for the garden community

**Example:**
```
Hello, Garden Community!
```

---

### Exercise 1: Garden Plot Area
**File:** [ex1/ft_plot_area.py](ex1/ft_plot_area.py)

**What You Learn:**
- Reading input, converting to integers, computing areas
- Producing formatted results from numeric operations

**Behavior:**
- Prompts for length and width; prints `Plot area: <area>`

**Example:**
```
Enter length: 5
Enter width: 3
Plot area: 15
```

---

### Exercise 2: Harvest Total
**File:** [ex2/ft_harvest_total.py](ex2/ft_harvest_total.py)

**What You Learn:**
- Accumulation patterns and addition across inputs
- Simple multi-step input and output sequences

**Behavior:**
- Prompts for harvest weights from 3 days; prints total

**Example:**
```
Day 1 harvest: 5
Day 2 harvest: 8
Day 3 harvest: 3
Total harvest: 16
```

---

### Exercise 3: Plant Age Check
**File:** [ex3/ft_plant_age.py](ex3/ft_plant_age.py)

**What You Learn:**
- Conditional logic and comparisons
- Message selection based on thresholds

**Behavior:**
- Asks plant age in days; prints readiness if > 60 days, else needs more time

**Example:**
```
Enter plant age in days: 75
Plant is ready to harvest!
```

---

### Exercise 4: Water Reminder
**File:** [ex4/ft_water_reminder.py](ex4/ft_water_reminder.py)

**What You Learn:**
- Conditional branching and message formatting

**Behavior:**
- If days since last watering > 2: `Water the plants!`; else: `Plants are fine`

**Example:**
```
Days since last watering: 4
Water the plants!
```

---

### Exercise 5: Count to Harvest (Iteration & Recursion)
**Files:** [ex5/ft_count_harvest_iterative.py](ex5/ft_count_harvest_iterative.py), [ex5/ft_count_harvest_recursive.py](ex5/ft_count_harvest_recursive.py)

**What You Learn:**
- Two approaches to repetition: loops vs. recursion
- Base/step design and clear termination conditions

**Behavior:**
- Prompts for number of days; prints `Day 1` ... `Day N` then `Harvest time!`

**Example:**
```
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```

---

### Exercise 6: Garden Summary
**File:** [ex6/ft_garden_summary.py](ex6/ft_garden_summary.py)

**What You Learn:**
- Multi-input combination and consistent output formatting

**Behavior:**
- Prompts for garden name and number of plants; prints a summary with fixed status

**Example:**
```
Enter garden name: Community Garden
Enter number of plants: 25
Garden: Community Garden
Plants: 25
Status: Growing well!
```

---

### Exercise 7: Seed Inventory (Type Annotations)
**File:** [ex7/ft_seed_inventory.py](ex7/ft_seed_inventory.py)

**What You Learn:**
- Type-annotated function signatures and clear contracts
- Conditional messaging by unit type

**Signature:**
```
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	 ...
```

**Behavior:**
- Prints inventory information for supported units:
  - `packets` → "packets available"
  - `grams` → "grams total"
  - `area` → "covers X square meters"
- For any other unit: "Unknown unit type"

**Examples:**
```
Tomato seeds: 15 packets available
Carrot seeds: 8 grams total
Lettuce seeds: covers 12 square meters
```

---

## 🧪 Testing Helper

A `main.py` helper is provided in the attachments. Place it in the project root to import and exercise the functions.

Run:
```bash
python3 main.py
```

This verifies behavior without adding any `__main__` blocks to exercise files.

---

## 📝 Technical Requirements

- **Python Version:** 3.10 or higher
- **Code Style:** Compliant with flake8 linter standards
- **Structure:** One function per file; exact function names; no `if __name__ == "__main__":`
- **Scope:** Input validation/error handling not required unless explicitly stated
- **Type Hints:** Optional; introduced in Exercise 7

---

## 💡 Key Takeaways

- Clear, single-purpose functions simplify reasoning and testing
- Basic I/O and arithmetic underpin practical data tasks
- Conditionals and iteration form the backbone of program flow
- Recursion offers expressive alternatives when loops are not ideal
- Consistent output formatting improves readability and usability
- Type hints document intent and aid tooling

---

## 🎓 Learning Path

1. Start with greetings and basic output (ex0)
2. Compute areas and totals (ex1–ex2)
3. Make decisions with conditionals (ex3–ex4)
4. Practice repetition with loops and recursion (ex5)
5. Produce concise summaries (ex6)
6. Add type-annotated signatures (ex7)

---

## 🔍 Debugging Tips

1. Read messages carefully; confirm values and flow
2. Print intermediate values when unsure
3. Check integer conversions and thresholds
4. Verify loop bounds (`range()` off-by-one errors)
5. For recursion, ensure a correct base case and progress toward it

---

## ✅ Validation Checklist

- [ ] Exact function names and one function per file
- [ ] No `if __name__ == "__main__":` blocks
- [ ] I/O handled inside the function as specified
- [ ] Output messages match examples exactly
- [ ] Flake8 style compliance (naming, spacing, line length)
- [ ] Type-annotated signature added in ex7

---

## 📊 Concepts Summary

| Concept              | Purpose                             | Where Used          |
|----------------------|-------------------------------------|---------------------|
| Expressions/Variables| Compute and store values            | ex1, ex2            |
| Input/Output         | Interact via console                | ex0–ex4, ex6        |
| Functions            | Encapsulate behavior                | all                 |
| Control Flow         | Make decisions                      | ex3, ex4            |
| Iteration            | Repeat actions with loops           | ex2, ex5 (iterative) |
| Recursion            | Repeat via self-calls               | ex5 (recursive)     |
| Formatting           | Produce readable output             | ex6                 |
| Type Hints           | Clarify contracts                   | ex7                 |

---

## 📎 Notes

This is an introductory project centered on basic Python syntax. Submissions consist of the individual exercise function files (e.g., ex0/ft_hello_garden.py, ex1/ft_plot_area.py). Advanced project management tools will be introduced in later modules.

**Happy coding! 🌿**

# Growing Code: Python Fundamentals Through Garden Data

An introductory Python project that explores core syntax and semantics through community garden scenarios. The focus is on expressions, variables, functions, and control flow using small, self-contained tasks that operate on simple garden data.

## Overview
This repository contains a sequence of exercises, each designed to highlight a fundamental programming concept. Tasks are concise and incremental, reflecting real-world data handling while emphasizing readable, testable code.

## Introduction
Participants work through practical exercises that build essential programming skills in an engaging context. Each exercise builds on the previous one and remains intentionally small and focused.

Project specification:
- Single-function files: each exercise is implemented as one function in its own file.
- No executable entry points: files do not include `if __name__ == "__main__":` blocks.
- Function names: exact names as specified by each exercise.
- Environment: targets Python 3.10+ and follows flake8 style guidelines.
- Input scope: validation or error handling is out of scope unless explicitly stated; behavior for negative or invalid inputs is unspecified.

## Repository Layout
- [ex0/ft_hello_garden.py](ex0/ft_hello_garden.py)
- [ex1/ft_plot_area.py](ex1/ft_plot_area.py)
- [ex2/ft_harvest_total.py](ex2/ft_harvest_total.py)
- [ex3/ft_plant_age.py](ex3/ft_plant_age.py)
- [ex4/ft_water_reminder.py](ex4/ft_water_reminder.py)
- [ex5/ft_count_harvest_iterative.py](ex5/ft_count_harvest_iterative.py)
- [ex5/ft_count_harvest_recursive.py](ex5/ft_count_harvest_recursive.py)
- [ex6/ft_garden_summary.py](ex6/ft_garden_summary.py)
- [ex7/ft_seed_inventory.py](ex7/ft_seed_inventory.py)

## Concepts Covered
- Basic input/output and strings: greetings, text formatting (ex0).
- Variables and arithmetic: area and total computations (ex1, ex2).
- Control flow: conditional logic for age checks and reminders (ex3, ex4).
- Iteration: loop-based counting and accumulation (ex2, ex5 iterative).
- Recursion: recursive approaches to counting problems (ex5 recursive).
- Data structures and formatting: building summaries, consistent output (ex6).
- Type hints and modules: optional typing to clarify intent (introduced in ex7).

## Exercises

**Exercise 0**
- **Function:** `ft_hello_garden`
- **Directory:** [ex0](ex0/)
- **File:** [ex0/ft_hello_garden.py](ex0/ft_hello_garden.py)
- **Authorized:** print()
- **Behavior:** Displays a welcome message to the garden community.
- **Example output:**
	Hello, Garden Community!

**Exercise 1**
- **Function:** `ft_plot_area`
- **Directory:** [ex1](ex1/)
- **File:** [ex1/ft_plot_area.py](ex1/ft_plot_area.py)
- **Authorized:** input(), int(), print()
- **Behavior:** Prompts for length and width of a rectangular plot, computes and displays the area.
- **Example session:**
	Enter length: 5
	Enter width: 3
	Plot area: 15

**Exercise 2**
- **Function:** `ft_harvest_total`
- **Directory:** [ex2](ex2/)
- **File:** [ex2/ft_harvest_total.py](ex2/ft_harvest_total.py)
- **Authorized:** input(), int(), print()
- **Behavior:** Asks for harvest weights across 3 days and prints the total.
- **Example session:**
	Day 1 harvest: 5
	Day 2 harvest: 8
	Day 3 harvest: 3
	Total harvest: 16

**Exercise 3**
- **Function:** `ft_plant_age`
- **Directory:** [ex3](ex3/)
- **File:** [ex3/ft_plant_age.py](ex3/ft_plant_age.py)
- **Authorized:** input(), int(), print()
- **Behavior:** Prompts for a plant’s age in days and reports readiness to harvest (more than 60 days) or not.
- **Example session:**
	Enter plant age in days: 75
	Plant is ready to harvest!

**Exercise 4**
- **Function:** `ft_water_reminder`
- **Directory:** [ex4](ex4/)
- **File:** [ex4/ft_water_reminder.py](ex4/ft_water_reminder.py)
- **Authorized:** input(), int(), print()
- **Behavior:** Prompts for days since last watering; if more than 2, prints "Water the plants!", otherwise prints "Plants are fine".
- **Example session:**
	Days since last watering: 4
	Water the plants!

**Exercise 5**
- **Functions:** `ft_count_harvest_iterative`, `ft_count_harvest_recursive`
- **Directory:** [ex5](ex5/)
- **Files:** [ex5/ft_count_harvest_iterative.py](ex5/ft_count_harvest_iterative.py), [ex5/ft_count_harvest_recursive.py](ex5/ft_count_harvest_recursive.py)
- **Authorized:** input(), int(), print(), range()
- **Behavior:** Counts from 1 to a given number, printing each day until harvest; implemented both iteratively and recursively.
- **Example session:**
	Days until harvest: 5
	Day 1
	Day 2
	Day 3
	Day 4
	Day 5
	Harvest time!

**Exercise 6**
- **Function:** `ft_garden_summary`
- **Directory:** [ex6](ex6/)
- **File:** [ex6/ft_garden_summary.py](ex6/ft_garden_summary.py)
- **Authorized:** input(), print()
- **Behavior:** Prompts for a garden name and number of plants, then prints a summary with a fixed status message: "Status: Growing well!".
- **Example session:**
	Enter garden name: Community Garden
	Enter number of plants: 25
	Garden: Community Garden
	Plants: 25
	Status: Growing well!

**Exercise 7**
- **Function:** `ft_seed_inventory`
- **Directory:** [ex7](ex7/)
- **File:** [ex7/ft_seed_inventory.py](ex7/ft_seed_inventory.py)
- **Authorized:** print()
- **Signature:** def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None
- **Behavior:** Displays inventory info for seed types and quantities. Supports units: "packets" ("packets available"), "grams" ("grams total"), "area" ("covers X square meters"). For any other unit, prints "Unknown unit type".
- **Example outputs:**
	Tomato seeds: 15 packets available
	Carrot seeds: 8 grams total
	Lettuce seeds: covers 12 square meters

## Testing Helper
A helper script (`main.py`) is provided in the attachments. When placed in the working directory and executed with Python 3, it imports and exercises the functions automatically, offering a simple way to verify behavior without adding code inside the exercise files.

## General Instructions
- Python Version: Use Python 3.10+.
- Linting: Code must respect flake8 standards.
- One Function per File: Each exercise lives in its own file with the exact function name requested.
- Scope: Input validation and error handling are not required unless explicitly mentioned.
- Invalid Inputs: Behavior for negatives/invalid values is undefined unless specified.
- Type Hints: Optional; introduced in exercise 7.

## Learning Outcomes
- Single-responsibility functions and console I/O (ex0–ex4).
- Numeric computations and accumulation (ex1–ex2).
- Conditional logic and comparisons (ex3–ex4).
- Iteration vs. recursion with base/step cases (ex5).
- Structured, readable summaries and formatting (ex6).
- Type annotations for clearer contracts (ex7).

## Skills Developed
- Clean function design; precise naming and scope.
- Input handling and integer casting; output formatting.
- Arithmetic, boolean logic, and loops with range().
- Recursive solutions with clear termination conditions.
- Flake8-compliant style on Python 3.10+.
- Introductory use of type hints in signatures.

## Notes
This is an introductory project centered on basic Python syntax. Submissions consist of the individual exercise function files (e.g., ft_hello_garden.py, ft_plot_area.py). Advanced project management and tooling will be introduced in later modules.
