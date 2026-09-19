# PantryPal

A pantry tracker that starts simple and grows into a small tool that suggests recipes based on what's actually in your kitchen. Built step by step while working through Python fundamentals, each stage adds a new concept on top of the last one instead of starting a new project from scratch.

## Stage 1: Data Structures

The first stage is about representing pantry data correctly using Python's core data structures, no loops or functions yet.

**What's in this stage:**
- A **list** holding all pantry items
- Each item stored as a **dictionary**, so one item can carry multiple facts (name, quantity, unit, category, expiration date)
- **Tuples** for expiration dates, since a date shouldn't change once it's set
- A **set** for tracking unique categories, so duplicates are automatically dropped

**Run it:**
```
python3 pantry_stage1.py
```

**What it does:**
- Adds six pantry items with details
- Prints the total item count and individual item details
- Shows expiration dates stored as tuples
- Builds a set of categories and checks membership in it
- Removes an item from the pantry list

---

## Stage 2: Programming Fundamentals

The fixed script from Stage 1 is now an interactive, menu-driven program. It keeps running and responding until you choose to exit.

**What's in this stage:**
- **Functions** for each action (add, view, remove, search), so logic isn't repeated
- A **while loop** running the main menu so the program keeps asking what to do next
- **for loops** to walk through the pantry list when printing or searching
- **if/elif/else** to route the user's menu choice to the right function
- **try/except** to catch bad input, both for item details and for the menu choice itself, without crashing

**Run it:**
```
python3 pantry_stage2.py
```

**What it does:**
- Menu with 6 options: add item, view pantry, remove item, view categories, search by category, exit
- Add item asks for name, quantity, unit, category, and expiry, and safely handles invalid numeric input
- Remove item searches the list by name and removes it if found
- Search by category filters and prints only matching items
- A non-numeric menu choice shows an error and returns to the menu instead of crashing the program
- Program loops until you choose Exit

---

More stages coming: object-oriented programming, then real file storage with Pandas, then live recipe suggestions from an API.
