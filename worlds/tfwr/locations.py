from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING
from pathlib import Path
from yaml import safe_load

from BaseClasses import Location, Region
from .Data.Strings import REGION

if TYPE_CHECKING:
    from .world import TFWRWorld


@dataclass
class LocationData:
    name: str
    id: int
    region: str
    requirements: list[str] | None = None


ACHIEVEMENTS: list[LocationData] = []

with open(Path(__file__).resolve().parent / "Data/data.yaml", "r") as file:
    config_data = safe_load(file)
for location in config_data["locations"]:
    ACHIEVEMENTS.append(
        LocationData(location["name"], location["id"], location["region"], location.get("requirements", None)))

ALL_LOCATIONS: list[LocationData] = (
    ACHIEVEMENTS
)

# Remember, locations don't have to be completed. These are "steps" along the way to completing the game, but might be optional
LOCATION_NAME_TO_ID: dict[str, int] = {location.name: location.id for location in ALL_LOCATIONS}


class TFWRLocation(Location):
    game = "The Farmer Was Replaced"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: TFWRWorld) -> None:
    create_achieve_locations(world)
    create_events(world)


def create_achieve_locations(world: TFWRWorld) -> None:
    # For each region
    regionName: str
    for regionName in REGION.Regions:
        region: Region = world.get_region(regionName)
        # Get all locations with a matching region
        locations = get_location_names_with_ids(
            [location.name for location in ALL_LOCATIONS if location.region == regionName]
        )
        # add the locations to the region
        region.add_locations(locations, TFWRLocation)


def create_events(world: TFWRWorld) -> None:
    # This is used to create a location that acts as an event trigger
    # Possibly useful if the player needs to do something to move between regions that isn't related to a location?
    # Something like an in-game button. I can't think of any use in TFWR though.
    pass
