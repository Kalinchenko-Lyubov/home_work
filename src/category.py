class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


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
        Category.product_count += len(self._products)

    def add_product(self, product):
        """Добавляет объект класса Product в приватный список товаров"""
        self._products.append(product)
        Category.product_count += 1

    @property
    def products_list(self) -> str:
        """Геттер для вывода списка товаров в виде строки"""
        if not self._products:
            return "Товаров нет"
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {getattr(p, 'stock', 'нет данных')} шт."
            for p in self._products

        )
