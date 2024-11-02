class Product:
    def __init__(self, name: str, price: int):
        self.name: str = name
        self.price: int = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> int:
        return self.price

    def change_price(self, new_price: int):
        self.price = new_price