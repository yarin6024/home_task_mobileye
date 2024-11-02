import pytest
from invetory import Inventory
from product import Product
import random

adjectives = ["Red", "Fresh", "Large", "Small", "Bright"]
nouns = ["Apple", "Banana", "Carrot", "Laptop", "Book"]


@pytest.fixture
def empty_inventory():
    return Inventory()

@pytest.fixture
def preset_inventory():
    inventory = Inventory()
    inventory.add_product(Product("Apple", 1.00, 10))
    inventory.add_product(Product("Banana", 0.50, 20))
    return inventory

@pytest.fixture
def random_inventory():
    inventory = Inventory()
    for current_product in range(random.randint(1, 5)):
        name = f"{random.choice(adjectives)} {random.choice(nouns)}_{random.randint(1, 10)}"
        price = round(random.uniform(1.0, 50.0), 2)
        quantity = random.randint(1, 10)
        inventory.add_product(Product(name, price, quantity))
    return inventory