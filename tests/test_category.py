from src.category import Category
from src.product import Product


def test_category_init_and_products_getter(cat_smartphone):
    """Тест проверяет инициализацию и работу геттера products"""
    assert cat_smartphone.name == "Смартфоны"
    assert (
        cat_smartphone.description
        == "Смартфоны - средство не только коммуникации, но и получение дополнительных функций для удобства"
    )

    result = cat_smartphone.products
    assert isinstance(result, str)

    expected_first_line = "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert result.startswith(expected_first_line)


def test_category_empty_product_list():
    """Проверка работы геттера для пустой категории"""
    empty_category = Category("Прочие устройства", "Другие гаджеты", [])
    assert empty_category.products == "Товаров нет"


def test_add_product_updates_list_and_count(cat_smartphone):
    """Тест проверяет метод add_product"""
    new_prod = Product("Тестовый товар", "Описание", 999.0, 1)
    old_count = Category.product_count
    cat_smartphone.add_product(new_prod)
    assert Category.product_count == old_count + 1
    assert "Тестовый товар" in cat_smartphone.products


def test_class_counters(create_categories):
    """Тест проверяет работу классовых счетчиков"""
    assert Category.category_count == 3
