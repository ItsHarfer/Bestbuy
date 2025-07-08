"""
Unit tests for the Product class in the products' module.

These tests verify the functionality, error handling, and edge cases for the Product class,
including initialization, validation, state toggling, and purchasing logic.
"""

import io
from contextlib import redirect_stdout

from products import Product


def test_valid_initialization():
    """Test that a Product instance initializes correctly with valid input."""
    product = Product("Test Product", 10.0, 5)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.quantity == 5
    assert product.active


def test_invalid_name_type():
    """Test that a TypeError is raised when name is not a string."""
    try:
        Product(123, 10.0, 5)
        assert False
    except TypeError:
        pass


def test_invalid_name_value():
    """Test that a ValueError is raised when name is empty or whitespace."""
    try:
        Product("   ", 10.0, 5)
        assert False
    except ValueError:
        pass


def test_invalid_price_type():
    """Test that a TypeError is raised when price is not a number."""
    try:
        Product("Item", "not-a-float", 5)
        assert False
    except TypeError:
        pass


def test_negative_price():
    """Test that a ValueError is raised when price is negative."""
    try:
        Product("Item", -1.0, 5)
        assert False
    except ValueError:
        pass


def test_invalid_quantity_type():
    """Test that a TypeError is raised when quantity is not an integer."""
    try:
        Product("Item", 5.0, "ten")
        assert False
    except TypeError:
        pass


def test_negative_quantity():
    """Test that a ValueError is raised when quantity is negative."""
    try:
        Product("Item", 5.0, -10)
        assert False
    except ValueError:
        pass


def test_get_quantity():
    """Test the getter for product quantity."""
    product = Product("Test Product", 10.0, 5)
    assert product.get_quantity() == 5


def test_set_valid_quantity():
    """Test setting a valid quantity updates the value and keeps product active."""
    product = Product("Test Product", 10.0, 5)
    product.set_quantity(10)
    assert product.quantity == 10
    assert product.active


def test_set_zero_quantity_deactivates():
    """Test setting quantity to zero deactivates the product."""
    product = Product("Test Product", 10.0, 5)
    product.set_quantity(0)
    assert product.quantity == 0
    assert not product.active


def test_set_quantity_invalid_type():
    """Test that setting quantity to a non-integer raises a TypeError."""
    product = Product("Test Product", 10.0, 5)
    try:
        product.set_quantity("ten")
        assert False
    except TypeError:
        pass


def test_set_quantity_negative():
    """Test that setting quantity to a negative value raises a ValueError."""
    product = Product("Test Product", 10.0, 5)
    try:
        product.set_quantity(-1)
        assert False
    except ValueError:
        pass


def test_activate():
    """Test that the product can be activated."""
    product = Product("Test Product", 10.0, 5)
    product.deactivate()
    product.activate()
    assert product.active


def test_deactivate():
    """Test that the product can be deactivated."""
    product = Product("Test Product", 10.0, 5)
    product.deactivate()
    assert not product.active


def test_is_active():
    """Test the is_active method reflects correct active state."""
    product = Product("Test Product", 10.0, 5)
    assert product.is_active()
    product.deactivate()
    assert not product.is_active()


def test_show():
    """Test that the string representation is printed correctly."""
    product = Product("Test Product", 10.0, 5)

    # Redirect standard output to the buffer so we can capture and inspect what 'show()' prints
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        product.show()
    output = buffer.getvalue()

    assert "Test Product" in output
    assert "Price: 10.0" in output
    assert "Quantity: 5" in output


def test_buy_valid_quantity():
    """Test buying a valid quantity decreases stock and returns total price."""
    product = Product("Test Product", 10.0, 5)
    total = product.buy(2)
    assert total == 20.0
    assert product.quantity == 3


def test_buy_reduces_to_zero():
    """Test buying the full quantity reduces stock to zero."""
    product = Product("Test Product", 10.0, 5)
    total = product.buy(5)
    assert total == 50.0
    assert product.quantity == 0


def test_buy_too_much():
    """Test buying more than available quantity raises a ValueError."""
    product = Product("Test Product", 10.0, 5)
    try:
        product.buy(6)
        assert False
    except ValueError:
        pass


def test_buy_negative():
    """Test that buying a negative quantity raises a ValueError."""
    product = Product("Test Product", 10.0, 5)
    try:
        product.buy(-1)
        assert False
    except ValueError:
        pass


def test_buy_invalid_type():
    """Test that buying with a non-integer quantity raises a TypeError."""
    product = Product("Test Product", 10.0, 5)
    try:
        product.buy("two")
        assert False
    except TypeError:
        pass


def test_validate_stock_enough():
    """Test that validate_stock passes when stock is sufficient."""
    product = Product("Test Product", 10.0, 5)
    product.validate_stock(2)  # should not raise


def test_validate_stock_too_much():
    """Test that validate_stock raises ValueError when stock is insufficient."""
    product = Product("Test Product", 10.0, 5)
    try:
        product.validate_stock(10)
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_valid_initialization()
    test_invalid_name_type()
    test_invalid_name_value()
    test_invalid_price_type()
    test_negative_price()
    test_invalid_quantity_type()
    test_negative_quantity()
    test_get_quantity()
    test_set_valid_quantity()
    test_set_zero_quantity_deactivates()
    test_set_quantity_invalid_type()
    test_set_quantity_negative()
    test_activate()
    test_deactivate()
    test_is_active()
    test_show()
    test_buy_valid_quantity()
    test_buy_reduces_to_zero()
    test_buy_too_much()
    test_buy_negative()
    test_buy_invalid_type()
    test_validate_stock_enough()
    test_validate_stock_too_much()
