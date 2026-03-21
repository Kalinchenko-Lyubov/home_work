import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def cat_smartphone(product_1, product_2):
    product_3 = Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)

    return Category(
        name="Смартфоны",
        description="Смартфоны - средство не только коммуникации, но и получение дополнительных функций для удобства",
        products=[product_1, product_2, product_3],
    )


@pytest.fixture
def create_categories():
    categories = [
        Category("Смартфоны", "Различные модели смартфонов", []),
        Category("Компьютеры", "Портативные ноутбуки и ПК", []),
        Category("Планшеты", "Модели планшетов", []),
    ]
    return categories


@pytest.fixture(autouse=True)
def reset_counters():
    """Автоматически сбрасывает счётчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
