import argparse
import asyncio
from . import systems, market
from .request import Request

__all__ = ["Client"]

parser = argparse.ArgumentParser(description="Run kiken")
parser.add_argument(
    "--debug", dest="debug", help="set log level to DEBUG", action="store_true"
)
args = parser.parse_args()


class Client:
    async def get_system(self, system):
        r = Request(args.debug)
        bodies = await r.request("api-system-v1/bodies", systemName=system)
        value = await r.request("api-system-v1/estimated-value", systemName=system)
        stations = await r.request("api-system-v1/stations", systemName=system)
        return systems.get_system(bodies, value, stations["stations"])

    async def get_market(
        self, market_id: int = None, system_name: str = None, station_name: str = None
    ):
        if not any([market_id, system_name]):
            raise ValueError("Either market_id or system_name must be provided")
        if market_id:
            return await market.get_market_by_id(market_id)
        elif system_name:
            return await market.get_market_by_system(system_name, station_name)

    def run(self):
        asyncio.run()
