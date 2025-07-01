class Product:
    """
    A class to represent a product with pricing, quantity, and availability logic.

    This class handles product validation, stock control, activation status,
    and purchasing logic. It ensures that all inputs are valid upon initialization
    and provides methods for safe modification and querying of the product state.

    :param name: Name of the product.
    :type name: str
    :param price: Price of the product. Must be a non-negative number.
    :type price: float
    :param quantity: Available stock. Must be a non-negative integer.
    :type quantity: int

    :raises TypeError: If the name is not a string, or if price/quantity have incorrect types.
    :raises ValueError: If the name is empty/whitespace, or if price/quantity are negative.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """Constructor method"""
        self.validate_name(name)
        self.validate_price(price)
        self.validate_quantity(quantity)

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Getter function for quantity.

        :return: Returns the quantity of the product (int).

        """
        return self.quantity

    def set_quantity(self, quantity) -> None:
        """
        Setter function for quantity. If the quantity reaches 0, deactivates the product.
        :param quantity: New quantity (int)
        """
        self.validate_quantity(quantity)
        self.quantity = quantity

        if self.quantity <= 0:
            self.active = False

    def is_active(self) -> bool:
        """
        Getter function for active.

        :return: Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self) -> None:
        """Activates the product"""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product"""
        self.active = False

    def show(self) -> str:
        """
        Returns a string that represents the product.
        :return: String representation of the product. For example,
        "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Purchases a specified quantity of the product and updates the stock accordingly.
        Edge cases: negative quantity, quantity greater than the quantity of the product.
        :param quantity: Quantity to buy (int)
        :return: Total price of the purchase (float)
        :raises ValueError: If the requested quantity is greater than the available stock.
        """
        self.validate_quantity(quantity)
        self.validate_stock(quantity)
        self.quantity -= quantity
        return self.price * quantity

    def validate_stock(self, requested_quantity: int) -> None:
        """
        Validates that enough stocks are available for the requested quantity.

        :param requested_quantity: Amount to check against current stock
        :raises ValueError: if requested_quantity exceeds current stock
        """
        if requested_quantity > self.quantity:
            raise ValueError(
                f"Requested quantity ({requested_quantity}) exceeds available stock "
                f"({self.quantity})."
            )

    @staticmethod
    def validate_name(name) -> None:
        """
        Validates the name of the product.
        Edge cases: empty string, whitespace only, type error

        :param name: Name of the product (str)
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty or whitespace only")

    @staticmethod
    def validate_price(price) -> None:
        """
        Validates the price of the product.
        Edge cases: negative number, type error
        :param price: Price of the product (float)
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")

    @staticmethod
    def validate_quantity(quantity) -> None:
        """
        Validates the quantity of the product.
        Edge cases: negative number, type error
        :param quantity: Quantity of the product (int)
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")


def main():
    """Main function to test the Product class."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
