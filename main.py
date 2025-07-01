"""
Main entry point for the Store Manager application.

This module initializes the store, displays a command-line menu interface,
and dispatches user-selected actions via the command dispatcher.

The program simulates a simple inventory system for a store.

Users can:
- List all available products along with their price and quantity.
- View the total number of different products available in the store.
- Make an order by selecting specific products and quantities, with automatic
  stock validation and update.
- Exit the application gracefully.

Functions:
- print_menu(): Prints the main menu options.
- start(store): Starts the user interaction loop and handles input dispatching.

Execution:
    Run this module directly to launch the application.

Author: Martin Haferanke
Date: 2025-07-01
"""

from dispatcher import get_command_dispatcher
from products import Product
from store import Store

# Set up the initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    Product("iPhone 15 Pro Max", price=1200, quantity=10),
    Product("Samsung Galaxy S22 Ultra", price=1000, quantity=5),
    Product("Apple Watch Series 7", price=1000, quantity=10),
]

best_buy = Store(product_list)


def print_menu():
    print()
    print("Bestbuy Store Menu:")
    print("1. List all products in store")
    print("2. Show total quantity in store")
    print("3. Make an order")
    print("4. Quit")
    print()


def start(store: Store):
    print("Welcome to the Store Manager!")
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        dispatcher = get_command_dispatcher(store)
        action = dispatcher.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    start(best_buy)
