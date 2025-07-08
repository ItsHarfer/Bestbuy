from products import Product


class Store:
    """
    A class to represent a store that manages a list of products and facilitates product orders.

    This class allows adding, removing, and querying products in the store.
    It also handles order processing by validating shopping lists and updating
    product quantities accordingly.

    :param product_list: List of Product instances to initialize the store with.
    :type product_list: list[Product]

    :raises TypeError: If any item in product_list or shopping_list is not of the expected type.
    :raises ValueError: If a product is inactive or the shopping list is invalid.
    """

    def __init__(self, product_list: list[Product]):
        """
        Initialize the store with a list of products.

        :param product_list: List of Product instances
        :type product_list: list[Product]
        """
        self.product_list = []
        for product in product_list:
            self.validate_product(product)
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """
        Add a product to the store's product list.

        :param product: Product instance to add
        :raises ValueError: If the product already exists in the store
        """
        if product in self.product_list:
            raise ValueError("Product already exists in the store")

        self.product_list.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store's product list.

        :param product: Product instance to remove
        """
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Get the total number of products in the store.

        :return: Number of products
        """

        return sum(product.quantity for product in self.product_list)

    def get_all_products(self) -> list[Product]:
        """
        Retrieve all active products currently in the store.

        :return: List of active Product instances
        """
        return [product for product in self.product_list if product.active]

    def print_products(self) -> None:
        """
        Print a numbered list of all active products in the store.
        """

        active_products = self.get_all_products()
        if not active_products:
            print("No products available.")
        else:
            print()
            print("Available products:")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. ", end="")
                product.show()
            print()

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Process a shopping list order by validating and purchasing the listed products.

        :param shopping_list: A list of tuples containing (Product, quantity)
        :return: Total price of the order
        """
        self.validate_shopping_list(shopping_list)

        total_price = 0
        for product, quantity in shopping_list:
            self.validate_product(product)
            total_price += product.buy(quantity)
        return total_price

    @staticmethod
    def validate_shopping_list(shopping_list: list[tuple[Product, int]]) -> None:
        """
        Validate that the shopping list is a non-empty list of valid product-quantity tuples.

        :param shopping_list: List of (Product, int) tuples
        :raises TypeError: If shopping_list is not a list or items are of incorrect types
        :raises ValueError: If the list is empty
        """
        if not isinstance(shopping_list, list):
            raise TypeError("Invalid shopping list type")
        if len(shopping_list) == 0:
            raise ValueError("Shopping list is empty")
        for product, quantity in shopping_list:
            Store.validate_product(product)
            Store.validate_quantity(quantity)

    @staticmethod
    def validate_product(product: Product) -> None:
        """
        Validate that a given product is an instance of Product and is active.

        :param product: Product to validate
        :raises TypeError: If the product is not an instance of Product
        :raises ValueError: If the product is inactive
        """
        if not isinstance(product, Product):
            raise TypeError("Invalid product type")
        if not product.is_active():
            raise ValueError("Product is not active")

    @staticmethod
    def validate_quantity(quantity: int) -> None:
        """
        Validate that a quantity is a positive integer.

        :param quantity: Quantity to validate
        :raises TypeError: If the quantity is not an integer
        :raises ValueError: If the quantity is less than or equal to 0
        """
        if not isinstance(quantity, int):
            raise TypeError("Invalid quantity type")
        if not quantity > 0:
            raise ValueError("Quantity must be greater than 0")


def main():
    """Main function to test the Store class."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
