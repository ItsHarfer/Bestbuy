"""
Dispatcher module for handling user menu commands.

This module provides a function to return a command dispatcher dictionary
that maps user input choices to their corresponding command handlers. Each
handler is responsible for performing a specific store-related operation
such as listing products, showing total quantity, making an order, or quitting
the program.

Author: Martin Haferanke
Date: 2025-07-01
"""

from commands import (
    handle_list_products,
    handle_show_total_quantity,
    handle_make_order,
    handle_quit_program,
)
from store import Store


def get_command_dispatcher(store: Store) -> dict:
    return {
        "1": lambda: handle_list_products(store),
        "2": lambda: handle_show_total_quantity(store),
        "3": lambda: handle_make_order(store),
        "4": handle_quit_program,
    }
