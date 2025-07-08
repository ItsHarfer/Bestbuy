"""
Command handlers for interacting with the store system.

This module provides user-facing command functions for listing products,
displaying total product quantities, initiating product orders, and exiting
the application. These handlers are used to map user menu selections to
store-related operations.

Functions:
- handle_list_products: Lists all products in the store.
- handle_show_total_quantity: Shows the total count of products in the store.
- handle_make_order: Initiates the product ordering process.
- handle_quit_program: Exits the program.

Author: Martin Haferanke
Date: 2025-07-01
"""

from store import Store
from utils.order import process_order


def handle_list_products(store: Store) -> None:
    """
    Display all available products in the store.

    :param store: The store instance containing products.
    """

    if not store.get_all_products():
        print("No products in store.")
        return

    store.print_products()


def handle_show_total_quantity(store: Store) -> None:
    """
    Display the total number of products currently in the store.

    :param store: The store instance containing products.
    """
    print(f"Total products in store: {store.get_total_quantity()}")


def handle_make_order(store: Store) -> None:
    """
    Initiate the order process by letting the user purchase products.

    :param store: The store instance containing products.
    """
    if not store.get_all_products():
        print("No products in store.")
        return
    process_order(store)


def handle_quit_program() -> None:
    """Terminate the program with a goodbye message."""
    print("Goodbye!")
    exit()
