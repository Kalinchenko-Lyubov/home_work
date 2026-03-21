class Product:
    """Класс описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод для сложения двух продуктов.
        """
        if type(self) is not type(other):
            # Если классы разные, вызываем ошибку TypeError
            raise TypeError("Нельзя складывать товары из разных категорий (разных классов).")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового объекта Product из словаря.
        """
        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    @property
    def price(self) -> float:
        """Геттер для получения цены товара."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены с проверкой на положительность."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = value


class Smartphone(Product):
    """
    Класс-наследник Product для категории 'Смартфон'.
    """
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    """
    Класс-наследник Product для категории 'Трава газонная'
    """
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
