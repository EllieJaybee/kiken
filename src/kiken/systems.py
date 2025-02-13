from .bodies import get_body, Planet, Star
from .stations import get_station, Station, FleetCarrier
from typing import Union

__all__ = ["System"]


class System:
    def __init__(
        self, bodies_dict: dict, value_dict: dict, stations_list: list
    ) -> None:
        self.id: int = bodies_dict["id"]
        self.id64: int = bodies_dict["id64"]
        self.name: str = bodies_dict["name"]
        self.url: str = bodies_dict["url"]
        self.body_count: int = bodies_dict["bodyCount"]
        self.bodies: list[Union[Planet, Star]] = [
            get_body(_, value_dict["valuableBodies"]) for _ in bodies_dict["bodies"]
        ]
        self.estimated_value: int = value_dict["estimatedValue"]
        self.estimated_value_mapped: int = value_dict["estimatedValueMapped"]
        self.stations: list[Union[FleetCarrier, Station]] = [
            get_station(_) for _ in stations_list
        ]
        for body in self.bodies:
            for station in self.stations:
                if station.body_id == body.id:
                    body.stations.append(station)
            if body.parent_id:
                for parent in self.bodies:
                    if parent.body_id == body.parent_id:
                        parent.children.append(body)
                        body.parent = parent


def get_system(bodies_dict: dict, value_dict: dict, stations_list: list):
    return System(bodies_dict, value_dict, stations_list)
