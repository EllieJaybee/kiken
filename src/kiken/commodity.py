class Commodity:
    def __init__(self, commodity_dict: dict) -> None:
        self.id: int = commodity_dict["id"]
        self.name: str = commodity_dict["name"]
        self.buy_price: int = commodity_dict["buyPrice"]
        self.stock: int = commodity_dict["stock"]
        self.sell_price: int = commodity_dict["sellPrice"]
        self.demand: int = commodity_dict["demand"]
        self.stock_bracket: int = commodity_dict["stockBracket"]
