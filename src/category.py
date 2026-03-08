class Category:
    """Класс с описанием категории продуктов"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products or []
        Category.category_count += 1
        Category.product_count += len(self.products)

if __name__ == "__main__":

    category_coffee = Category("Напитки", "Горячие напитки", ["Кофе", "Свежесваренный кофе", 150.0, 10])
    category_tea = Category("Напитки", "Горячие напитки", ["Чай", "Черный чай", 100.0, 20])

    print(category_coffee.name)
    print(category_tea.name)
    print(Category.product_count)