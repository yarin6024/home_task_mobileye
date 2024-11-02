from product import Product


class Inventory:
    def __init__(self):
        self.products = []

    # add product type as Product
    def add_product(self, product: Product):
        for existing_product in self.products:
            if existing_product.get_name() == product.get_name():
                print(f"Product with name {product.get_name()} already exists")
            else:
                self.products.append(product)

    def remove_product(self, product_name: str):
        self.products.remove(self.get_product(product_name=product_name))

    def get_product(self, product_name:str) -> Product:
        wanted_product = None
        for product in self.products:
            if product.get_name() == product_name:
                wanted_product = product

        if wanted_product is None:
            print(f"There is no product with the name {product_name}")

        return wanted_product
