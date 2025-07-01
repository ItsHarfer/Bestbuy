"""
Order processing module

This module provides functionality to interactively process a customer's order by:
- Listing products available in the store.
- Accepting product selections and desired quantities.
- Submitting the shopping cart to the store for final order processing.


Author: Martin Haferanke
Date: 2025-07-01
"""

from store import Store


def process_order(store: Store) -> None:
    """
    Processes an order from a store. This function allows a user to select products from
    the store, input their desired quantities, and finalize the order. Once the process
    is complete, the total cost of the shopping cart will be displayed.

    :param store: The store object from which products will be retrieved and the
                  order will be processed
    :raises ValueError: If the user inputs an invalid product number or quantity
    :raises Exception: If an error occurs during order processing
    """
    shopping_cart = []
    products = store.get_all_products()

    while True:
        try:
            choice = int(input("Enter product number to buy (0 to finish): "))
            if choice == 0:
                break
            if 1 <= choice <= len(products):
                qty = int(input(f"Enter quantity for {products[choice - 1].name}: "))
                if qty > 0:
                    shopping_cart.append((products[choice - 1], qty))
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    try:
        total = store.order(shopping_cart)
        print(f"Order placed successfully. Total cost: ${total}")
    except Exception as e:
        print(f"Error processing order: {e}")
