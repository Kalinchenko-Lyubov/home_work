import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


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
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def smartphone_1():
    return Smartphone(
        name="iPhone 15",
        description="Смартфон от Apple",
        price=120000.0,
        quantity=10,
        efficiency="Высокая",
        model="15",
        memory=256,
        color="Черный"
    )

@pytest.fixture
def smartphone_2():
     return Smartphone(
        name="Samsung S23",
        description="Флагман на Android",
        price=95000.0,
        quantity=15,
        efficiency="Высокая",
        model="S23",
        memory=512,
        color="Белый"
    )

@pytest.fixture
def lawn_grass_1():
    return LawnGrass(
        name="Газон Универсальный",
        description="Смесь трав для средней полосы",
        price=450.0,
        quantity=100,
        country="Россия",
        germination_period="10-14 дней",
        color="Зеленый"
    )
