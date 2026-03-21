from src.product import Product


def test_product_init_1(product_1):
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_init_2(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_price_setter_valid_value(product_1):
    """Тест: Сеттер должен устанавливать корректную цену"""
    product_1.price = 99999.99
    assert product_1.price == 99999.99


def test_price_setter_negative_value(product_1, capsys):
    """Тест: Сеттер должен игнорировать отрицательную цену. Проверяет, что цена не изменилась и сообщение выведено"""
    old_price = product_1.price
    product_1.price = -5000
    assert product_1.price == old_price

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_zero_value(product_1, capsys):
    """Тест: Сеттер должен игнорировать нулевую цену. Проверяет, что цена не изменилась и сообщение выведено"""
    old_price = product_1.price
    product_1.price = 0
    assert product_1.price == old_price

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_from_dict():
    """Тест: Создание продукта из словаря"""
    data = {"name": "Test Phone", "description": "Just a test", "price": 100500.0, "quantity": 1}

    prod = Product.new_product(data)

    assert isinstance(prod, Product)
    assert prod.name == data["name"]
    assert prod.description == data["description"]
    assert prod.price == data["price"]


def test_product_addition():
    product_a = Product("Ноутбук", "Игровой", 100000.0, 2)
    product_b = Product("Мышь", "Беспроводная", 1500.0, 10)
    total_value = product_a + product_b
    expected_value = (100000.0 * 2) + (1500.0 * 10)
    assert total_value == expected_value
    assert total_value == 215000.0
