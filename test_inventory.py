from product import Product


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