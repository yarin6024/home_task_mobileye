import pytest

from product import Product

@pytest.mark.xfail
def test_get_non_existent_product_should_fail(empty_inventory):
    result = empty_inventory.get_product("NonExistentProduct")
    assert result is not None

@pytest.mark.xfail
def test_incorrect_inventory_value_should_fail(preset_inventory):
    assert preset_inventory.total_inventory_value() == 25.00

def test_add_product(empty_inventory):
    product = Product("Laptop", 150.00, 3)
    empty_inventory.add_product(product)
    assert empty_inventory.get_product("Laptop") == product

def test_remove_product(preset_inventory):
    preset_inventory.remove_product("Apple")
    assert preset_inventory.get_product("Apple") is None
    assert preset_inventory.product_count() == 1

def test_total_inventory_value(preset_inventory):
    assert preset_inventory.total_inventory_value() == (1.00 * 10 + 0.50 * 20)

def test_get_non_existent_product(empty_inventory):
    assert empty_inventory.get_product("NonExistent") is None

def test_inventory_random_products(random_inventory):
    # Ensure the inventory has between 1 and 5 products
    products = random_inventory.get_products()
    assert 1 <= random_inventory.product_count() <= 5
    # Check if total value is correct
    total_value = sum([product.get_price() * product.get_quantity() for product in products])
    assert random_inventory.total_inventory_value() == total_value

def test_update_product_quantity(preset_inventory):
    preset_inventory.get_product(product_name="Apple").change_quantity(15)
    product = preset_inventory.get_product("Apple")
    assert product.quantity == 15

def test_inventory_product_names(preset_inventory):
    product_names = [product.name for product in preset_inventory.get_products()]
    assert "Apple" in product_names and "Banana" in product_names

