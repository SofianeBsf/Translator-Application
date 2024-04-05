# import json
# import os
# import matplotlib.pyplot as plt

# # File paths
# EXPENSES_FILE = "expenses.json"
# BUDGET_FILE = "budget.json"

# # Function to load expenses from file
# def load_expenses():
#     if os.path.exists(EXPENSES_FILE):
#         with open(EXPENSES_FILE, "r") as file:
#             return json.load(file)
#     return []

# # Function to save expenses to file
# def save_expenses(expenses):
#     with open(EXPENSES_FILE, "w") as file:
#         json.dump(expenses, file, indent=4)

# # Function to add a new expense
# def add_expense(expenses, category, amount):
#     expenses.append({"category": category, "amount": amount})
#     save_expenses(expenses)

# # Function to display expenses
# def display_expenses(expenses):
#     for expense in expenses:
#         print(f"{expense['category']}: £{expense['amount']}")

# # Function to calculate total expenses
# def calculate_total_expenses(expenses):
#     return sum(expense["amount"] for expense in expenses)

# # Function to visualize expenses
# def visualize_expenses(expenses):
#     categories = [expense["category"] for expense in expenses]
#     amounts = [expense["amount"] for expense in expenses]

#     plt.bar(categories, amounts)
#     plt.xlabel("Categories")
#     plt.ylabel("Amount (£)")
#     plt.title("Expense Distribution")
#     plt.xticks(rotation=45)
#     plt.show()

# # Main function
# def main():
#     print("Welcome to Personal Finance Manager!")

#     # Load expenses
#     expenses = load_expenses()

#     while True:
#         print("\n1. Add Expense")
#         print("2. View Expenses")
#         print("3. Calculate Total Expenses")
#         print("4. Visualize Expenses")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             category = input("Enter expense category: ")
#             amount = float(input("Enter expense amount: "))
#             add_expense(expenses, category, amount)
#             print("Expense added successfully!")
#         elif choice == "2":
#             print("\n--- Expenses ---")
#             display_expenses(expenses)
#         elif choice == "3":
#             total_expenses = calculate_total_expenses(expenses)
#             print(f"Total Expenses: £{total_expenses}")
#         elif choice == "4":
#             visualize_expenses(expenses)
#         elif choice == "5":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

import json

# Constants
INVENTORY_FILE = "library_inventory.json"

# Function to load library inventory from file
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save library inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file)

# Function to add a book to the library inventory
def add_book(inventory, book_id, title, author):
    inventory[book_id] = {"title": title, "author": author, "available": True}

# Function to search for a book in the library inventory
def search_book(inventory, title):
    for book_id, details in inventory.items():
        if details["title"].lower() == title.lower():
            return book_id, details
    return None, None

# Function to borrow a book from the library inventory
def borrow_book(inventory, book_id):
    if book_id in inventory and inventory[book_id]["available"]:
        inventory[book_id]["available"] = False
        return True
    return False

# Function to return a book to the library inventory
def return_book(inventory, book_id):
    if book_id in inventory and not inventory[book_id]["available"]:
        inventory[book_id]["available"] = True
        return True
    return False

# Function to remove a book from the library inventory
def remove_book(inventory, book_id):
    if book_id in inventory:
        del inventory[book_id]

# Main function to run the library system
def main():
    # Load library inventory from file
    inventory = load_inventory()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Remove Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            add_book(inventory, book_id, title, author)
            save_inventory(inventory)
            print("Book added successfully.")

        elif choice == "2":
            title = input("Enter book title to search: ")
            book_id, details = search_book(inventory, title)
            if book_id:
                print(f"Book found - ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Available: {'Yes' if details['available'] else 'No'}")
            else:
                print("Book not found.")

        elif choice == "3":
            book_id = input("Enter book ID to borrow: ")
            if borrow_book(inventory, book_id):
                save_inventory(inventory)
                print("Book borrowed successfully.")
            else:
                print("Book not available or does not exist.")

        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            if return_book(inventory, book_id):
                save_inventory(inventory)
                print("Book returned successfully.")
            else:
                print("Book not borrowed or does not exist.")

        elif choice == "5":
            book_id = input("Enter book ID to remove: ")
            remove_book(inventory, book_id)
            save_inventory(inventory)
            print("Book removed successfully.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
