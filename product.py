class Product:
    def __init__(self, name: str, price: float, quantity:int):
        self.name: str = name
        self.price: float = price
        self.quantity = quantity

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_quantity(self) -> int:
        return self.quantity

    def change_quantity(self, new_quantity: int):
        self.quantity = new_quantity

    def change_price(self, new_price: float):
        self.price = new_price