from .stations import Station

from typing import Literal, Union

__all__ = ["Star", "Planet"]


class Body:
    def __init__(self, body_dict: dict) -> None:
        self.id: int = body_dict["id"]
        self.id64: int = body_dict["id64"]
        self.body_id: int = body_dict["bodyId"]
        self.name: str = body_dict["name"]
        self.type: Literal["Star", "Planet"] = body_dict["type"]
        self.sub_type: str = body_dict["subType"]
        self.distance_to_arrival: int = body_dict["distanceToArrival"]
        self.surface_temperature: int = body_dict["surfaceTemperature"]
        self.orbital_period: float = body_dict["orbitalPeriod"]
        self.semi_major_axis: float = body_dict["semiMajorAxis"]
        self.orbital_eccentricity: float = body_dict["orbitalEccentricity"]
        self.orbital_inclination: float = body_dict["orbitalInclination"]
        self.arg_of_periapsis: float = body_dict["argOfPeriapsis"]
        self.rotational_period: float = body_dict["rotationalPeriod"]
        self.is_tidally_locked: bool = body_dict["rotationalPeriodTidallyLocked"]
        self.axial_tilt: float = body_dict["axialTilt"]
        try:
            self.discovery: dict = body_dict["discovery"]
        except KeyError:
            self.discovery = None
        self.stations: list[Station] = []
        self.parents: Union[list[Body], None] = (
            body_dict["parents"]
            if ("parents" in body_dict.keys()) and (body_dict["parents"])
            else []
        )
        self.sanitized_parents: list[Body] = []
        for parent in self.parents:
            if list(parent.keys())[0] != "Null":
                self.sanitized_parents.append(parent)
        if self.sanitized_parents:
            self.parent_id: int = list(self.sanitized_parents[0].values())[0]
        else:
            self.parent_id = None
        self.children: list[Body] = []
        self.parent: Body = None


class Star(Body):
    def __init__(self, body_dict: dict) -> None:
        super().__init__(body_dict)
        self.is_main_star: bool = body_dict["isMainStar"]
        self.is_scoopable: bool = body_dict["isScoopable"]
        self.age: int = body_dict["age"]
        self.luminosity: str = body_dict["luminosity"]
        self.absolute_magnitude: float = body_dict["absoluteMagnitude"]
        self.solar_masses: float = body_dict["solarMasses"]
        self.solar_radius: float = body_dict["solarRadius"]


class Planet(Body):
    def __init__(self, body_dict: dict, valuable_bodies: list[dict]) -> None:
        super().__init__(body_dict)
        self.is_landable: bool = body_dict["isLandable"]
        self.gravity: float = body_dict["gravity"]
        self.earth_masses: float = body_dict["earthMasses"]
        self.radius: float = body_dict["radius"]
        self.volcanism_type: str = body_dict["volcanismType"]
        self.atmosphere_type: str = body_dict["atmosphereType"]
        self.terraforming_state: str = body_dict["terraformingState"]
        for valuable_body in valuable_bodies:
            if valuable_body["bodyId"] == body_dict["id"]:
                self.value: int = valuable_body["valueMax"]
            else:
                self.value = 0


def get_body(body_dict: dict, valuable_bodies: list[dict]):
    if body_dict["type"] == "Star":
        return Star(body_dict)
    elif body_dict["type"] == "Planet":
        return Planet(body_dict, valuable_bodies)
