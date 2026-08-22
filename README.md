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
python3 pantry.py
```

**What it does:**
- Adds six pantry items with details
- Prints the total item count and individual item details
- Shows expiration dates stored as tuples
- Builds a set of categories and checks membership in it
- Removes an item from the pantry list

---

More stages coming: loops and functions, then object-oriented programming, then real file storage with Pandas, then live recipe suggestions from an API.