pantry=[]
categories=set()
def add_item():
    name=input("Enter the name of the item: ")
    try:
        quantity=int(input("Enter the quantity of the item: "))
    except ValueError:
        print("Quantity must be a number")
        return
    unit=input("Enter the unit:")
    category=input(("Enter the category:"))
    try:
        month=int(input("Enter the expiration month:"))
        year=int(input("Enter the expiration year:"))
    except ValueError:
        print("Expiration month and year should be numbers")
        return
    item={
        "Name":name,
        "Quantity":quantity,
        "Unit":unit,
        "Category":category,
        "Expiration date":(month,year)
    }
    pantry.append(item)
    categories.add(category)
    print("The item has been added sucessfully")

def view_pantry():
    if not pantry:
         print("The pantry is Empty")
         return
    for item in pantry:
        print("Name:", item["Name"])
        print("Quantity:", item["Quantity"])
        print("Unit:", item["Unit"])
        print("Category:", item["Category"])
        print("Expiration date:", item["Expiration date"])

def remove_item():
    name=input("Enter the name of the item to remove:")
    Found=False
    for item in pantry:
        if item["Name"].lower()==name.lower():
            pantry.remove(item)
            Found=True
            break
    if not Found:
        print("Item not found")
    else:
        print("Item removed")

def view_categories():
    if not categories:
        print("No categories yet")
        return
    print(categories)

def search_by_category():
    category=input("Enter the category you want to search")
    Found=False
    for item in pantry:
        if item["Category"].lower()==category.lower():
            print("Name:", item["Name"])
            print("Quantity:", item["Quantity"])
            print("Unit:", item["Unit"])
            print("Category:", item["Category"])
            print("Expiration date:", item["Expiration date"])
            Found=True
    if not Found:
        print("No items found in that category")
        
def main():
    while True:
        print("\n1. Add item")
        print("2. view pantry")
        print("3. Remove Item")
        print("4. View Categories")
        print("5. Search by Category")
        print("6. Exit")
        try:
            choice=int(input("Enter your choice :"))
        except ValueError:
            print("Please write the numerical value ")
            continue
        if choice==1:
            add_item()
        elif choice==2:
            view_pantry()
        elif choice==3:
            remove_item()
        elif choice==4:
            view_categories()
        elif choice==5:
            search_by_category()
        elif choice==6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice,try again")

main()