class Product:
    """Класс описания продукта."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product1 = Product("Кофе", "Свежесваренный кофе", 150.0, 10)
    product2 = Product("Чай", "Черный чай", 100.0, 20)

    print(product1.price)
