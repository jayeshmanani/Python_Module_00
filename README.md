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
