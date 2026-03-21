from src.product import Product


class Category:
    """Класс с описанием категории продуктов"""

    name: str
    description: str
    _products: list  # Приватный атрибут списка товаров
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None) -> None:
        self.name = name
        self.description = description
        self._products = products or []  # Всегда создаём список
        Category.category_count += 1
        if products:
            for prod in products:
                if not isinstance(prod, Product):
                    raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников.")
            Category.product_count += len(self._products)

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории
        """
        total_quantity = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Добавляет объект класса Product в приватный список товаров"""
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты класса Product или его наследников.")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в виде строки"""
        if not self._products:
            return "Товаров нет"
        return "\n".join(str(p) for p in self._products)
