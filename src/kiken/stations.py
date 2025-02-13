__all__ = ["FleetCarrier", "Station"]


class BaseStation:
    def __init__(self, stations_dict: dict) -> None:
        self.id: int = stations_dict["id"]
        self.market_id: int = stations_dict["marketId"]
        self.name: str = stations_dict["name"]
        self.type: str = stations_dict["type"]
        self.distance_to_arrival: int = stations_dict["distanceToArrival"]
        self.have_market: bool = stations_dict["haveMarket"]
        self.have_shipyard: bool = stations_dict["haveShipyard"]
        self.have_outfitting: bool = stations_dict["haveOutfitting"]
        other_services: list[str] = stations_dict["otherServices"]
        self.have_black_market: bool = "Black Market" in other_services
        self.have_restock: bool = "Restock" in other_services
        self.have_refuel: bool = "Refuel" in other_services
        self.have_repair: bool = "Repair" in other_services
        self.have_contacts: bool = "Contacts" in other_services
        self.have_universal_cartographics: bool = (
            "Universal Cartographics" in other_services
        )
        self.have_missions: bool = "Missions" in other_services
        self.have_crew_lounge: bool = "Crew Lounge" in other_services
        self.have_tuning: bool = "Tuning" in other_services
        self.have_search_and_rescue: bool = "Search and Rescue" in other_services
        self.have_apex: bool = "Apex Interstellar Transport" in other_services
        self.have_frontline: bool = "Frontline Solutions" in other_services
        self.have_pioneer: bool = "Pioneer Supplies" in other_services
        self.have_vista: bool = "Vista Genomics" in other_services
        self.body_id: int = (
            stations_dict["body"]["id"]
            if ("body" in stations_dict.keys())
            and ("id" in stations_dict["body"].keys())
            else None
        )
        self.body_name: str = (
            stations_dict["body"]["name"]
            if ("body" in stations_dict.keys())
            and ("name" in stations_dict["body"].keys())
            else None
        )
        self.latitude: float = (
            stations_dict["body"]["latitude"]
            if ("body" in stations_dict.keys())
            and ("latitude" in stations_dict["body"].keys())
            else None
        )
        self.longitude: float = (
            stations_dict["body"]["longitude"]
            if ("body" in stations_dict.keys())
            and ("longitude" in stations_dict["body"].keys())
            else None
        )


class FleetCarrier(BaseStation):
    def __init__(self, stations_dict: dict) -> None:
        super().__init__(stations_dict)


class Station(BaseStation):
    def __init__(self, stations_dict: dict) -> None:
        super().__init__(stations_dict)
        self.controlling_faction: dict = stations_dict["controllingFaction"]
        self.allegiance: str = stations_dict["allegiance"]
        self.government: str = stations_dict["government"]
        self.economy: str = stations_dict["economy"]
        self.second_economy: str = stations_dict["secondEconomy"]


def get_station(stations_dict: dict):
    if stations_dict["type"] == "Fleet Carrier":
        return FleetCarrier(stations_dict)
    else:
        return Station(stations_dict)
