import pytest

from src.product import LawnGrass, Product


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
    product_1.price = 99999.99
    assert product_1.price == 99999.99


def test_price_setter_negative_value(product_1, capsys):
    old_price = product_1.price
    product_1.price = -5000
    assert product_1.price == old_price

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_zero_value(product_1, capsys):
    old_price = product_1.price
    product_1.price = 0
    assert product_1.price == old_price

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_from_dict():
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


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "iPhone 15"
    assert smartphone_1.price == 120000.0
    assert smartphone_1.quantity == 10
    assert smartphone_1.efficiency == "Высокая"
    assert smartphone_1.model == "15"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Черный"


def test_smartphone_addition(smartphone_1, smartphone_2):
    total_value = smartphone_1 + smartphone_2
    expected_value = (smartphone_1.price * smartphone_1.quantity) + (smartphone_2.price * smartphone_2.quantity)
    assert total_value == expected_value


def test_smartphone_addition_error(smartphone_1, lawn_grass_1):
    with pytest.raises(TypeError, match="Нельзя складывать товары из разных категорий"):
        smartphone_1 + lawn_grass_1


def test_lawn_grass_init(lawn_grass_1):
    assert lawn_grass_1.name == "Газон Универсальный"
    assert lawn_grass_1.price == 450.0
    assert lawn_grass_1.quantity == 100
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "10-14 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_lawn_grass_addition(lawn_grass_1):
    grass_2 = LawnGrass(
        name="Газон Премиум",
        description="Для футбольных полей",
        price=700.0,
        quantity=50,
        country="Дания",
        germination_period="7 дней",
        color="Изумрудный",
    )
    total_value = lawn_grass_1 + grass_2
    expected_value = (lawn_grass_1.price * lawn_grass_1.quantity) + (grass_2.price * grass_2.quantity)
    assert total_value == expected_value


def test_lawn_grass_addition_error(lawn_grass_1, smartphone_1):
    with pytest.raises(TypeError, match="Нельзя складывать товары из разных категорий"):
        lawn_grass_1 + smartphone_1


def test_mixin_repr():
    product = Product("Книга", "Описание", 500, 10)
    expected_repr = "Product(name='Книга', description='Описание', _price=500, quantity=10)"
    assert repr(product) == expected_repr, "Миксин не сформировал правильную строку!"
