pantry = []

rice = {
    "Name": "Rice",
    "Quantity": 2,
    "Unit": "kg",
    "Category": "Grains",
    "Expiration Date": ("12-10-2028",)
}
wheat = {
    "Name": "Wheat",
    "Quantity": 5,
    "Unit": "kg",
    "Category": "Grains",
    "Expiration Date": ("12-10-2029",)
}
sugar_small_bag = {
    "Name": "Sugar",
    "Quantity": 3,
    "Unit": "kg",
    "Category": "Sweeteners",
    "Expiration Date": ("11-1-2028",)
}
milk = {
    "Name": "Milk",
    "Quantity": 2,
    "Unit": "liters",
    "Category": "Dairy",
    "Expiration Date": ("1-12-2025",)
}
yogurt = {
    "Name": "Yogurt",
    "Quantity": 1,
    "Unit": "kg",
    "Category": "Dairy",
    "Expiration Date": ("1-12-2025",)
}
sugar_large_bag = {
    "Name": "Sugar",
    "Quantity": 5,
    "Unit": "kg",
    "Category": "Sweeteners",
    "Expiration Date": ("12-10-2030",)
}

pantry.append(rice)
pantry.append(wheat)
pantry.append(milk)
pantry.append(sugar_small_bag)
pantry.append(yogurt)
pantry.append(sugar_large_bag)

total_items = len(pantry)
print("Total items in the pantry:", total_items)

print("Item 1 name in the pantry using index 0:", pantry[0]["Name"])
print("Item 1 details in the pantry using variable rice:", rice)

print("Expiry date of", rice["Name"], "is", rice["Expiration Date"])
print("Expiry date of", wheat["Name"], "is", wheat["Expiration Date"])
print("Expiry date of", milk["Name"], "is", milk["Expiration Date"])

categories = {"Dairy", "Grains", "Sweeteners", "Sweeteners"}
print("Categories of items in the pantry are:", categories)

if "Grains" in categories:
    print("Yes, Grains exists in the categories!")
else:
    print("No, Grains does not exist.")

pantry.remove(yogurt)
print("Total items in the pantry after removing Yogurt:", len(pantry))
print("Items in the pantry after removing Yogurt:", pantry)