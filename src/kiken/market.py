from .request import Request
from .commodity import Commodity

r = Request()


class Market:
    def __init__(self, market_dict: dict) -> None:
        self.system_id = market_dict["id"]
        self.system_id64 = market_dict["id64"]
        self.system_name = market_dict["name"]
        self.id = market_dict["marketId"]
        self.station_id = market_dict["sId"]
        self.station_name = market_dict["sName"]
        self.url = market_dict["url"]
        self.commodities = [Commodity(_) for _ in market_dict["commodities"]]


async def get_market_by_id(market_id: int):
    market_dict = await r.request("api-system-v1/stations/market", marketId=market_id)
    return Market(market_dict)


async def get_market_by_system(system_name: str, station_name: str):
    market_dict = await r.request(
        "api-system-v1/stations/market",
        systemName=system_name,
        stationName=station_name,
    )
    return Market(market_dict)
