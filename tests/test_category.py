from src.category import Category


def test_category_init(cat_smartphone):
    assert cat_smartphone.name == "Смартфоны"
    assert (
        cat_smartphone.description
        == "Смартфоны - средство не только коммуникации, но и получение дополнительных функций для удобства"
    )
    assert cat_smartphone.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]


def test_category_product_count(cat_smartphone):
    """Проверка подсчета количества продуктов в категории."""
    assert len(cat_smartphone.products) == 3


def test_category_empty_product_list():
    """Проверка работы с пустой категорией."""
    empty_category = Category("Прочие устройства", "Другие гаджеты", [])
    assert len(empty_category.products) == 0


def test_category_count(create_categories):
    """Проверка подсчета количества категорий."""
    assert Category.category_count == 3

