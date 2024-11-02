from product import Product


def test_add_product(empty_inventory):
    product = Product("Laptop", 150.00, 3)
    empty_inventory.add_product(product)
    assert empty_inventory.get_product("Laptop") == product

