"""
Unit tests for the Store class in the store module.

These tests verify the functionality, validation logic, and error handling of the Store class,
including product management, order processing, and data integrity.
"""

from products import Product
from store import Store


def test_store_initialization():
    """Test initializing store with valid products."""
    p1 = Product("Phone", 500.0, 10)
    p2 = Product("Tablet", 300.0, 5)
    store = Store([p1, p2])
    assert store.get_total_quantity() == 2
    assert p1 in store.get_all_products()
    assert p2 in store.get_all_products()


def test_add_duplicate_product_raises():
    """Test that adding a duplicate product raises a ValueError."""
    p1 = Product("Phone", 500.0, 10)
    store = Store([p1])
    try:
        store.add_product(p1)
        assert False
    except ValueError:
        pass


def test_remove_product():
    """Test removing a product from the store."""
    p1 = Product("Phone", 500.0, 10)
    store = Store([p1])
    store.remove_product(p1)
    assert store.get_total_quantity() == 0
    assert p1 not in store.get_all_products()


def test_order_valid_products():
    """Test valid order processing and quantity reduction."""
    p1 = Product("Phone", 500.0, 10)
    p2 = Product("Tablet", 300.0, 5)
    store = Store([p1, p2])
    total = store.order([(p1, 1), (p2, 2)])
    assert total == 500.0 + 600.0
    assert p1.quantity == 9
    assert p2.quantity == 3


def test_order_invalid_quantity_type():
    """Test that ordering with invalid quantity type raises TypeError."""
    p1 = Product("Phone", 500.0, 10)
    store = Store([p1])
    try:
        store.order([(p1, "two")])
        assert False
    except TypeError:
        pass


def test_order_zero_quantity():
    """Test that ordering with zero quantity raises ValueError."""
    p1 = Product("Phone", 500.0, 10)
    store = Store([p1])
    try:
        store.order([(p1, 0)])
        assert False
    except ValueError:
        pass


def test_order_inactive_product():
    """Test that ordering an inactive product raises ValueError."""
    p1 = Product("Phone", 500.0, 10)
    p1.deactivate()
    store = Store([])
    try:
        store.order([(p1, 1)])
        assert False
    except ValueError:
        pass


def test_validate_shopping_list_not_list():
    """Test that passing non-list to validate_shopping_list raises TypeError."""
    try:
        Store.validate_shopping_list("not-a-list")
        assert False
    except TypeError:
        pass


def test_validate_shopping_list_empty():
    """Test that passing empty list to validate_shopping_list raises ValueError."""
    try:
        Store.validate_shopping_list([])
        assert False
    except ValueError:
        pass
