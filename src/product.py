class Product:
    """Класс описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity):
        """
        Класс-метод для создания нового объекта Product.
        Принимает параметры товара и возвращает созданный экземпляр.
        """
        return cls(name, description, price, quantity)