from __future__ import annotations

from typing import TYPE_CHECKING, Any
from dataclasses import dataclass

from BaseClasses import Location, Region

from .Data.Strings import ACHIEVEMENT, REGION

if TYPE_CHECKING:
    from .world import TFWRWorld


@dataclass
class LocationData:
    name: str
    id: int
    region: str
    requirements: list[str] | None = None


ACHIEVEMENTS: list[LocationData] = [
    LocationData(ACHIEVEMENT.Hello_World, 10000, REGION.Start),
    LocationData(ACHIEVEMENT.Infinite_Loop, 10001, REGION.Start),
    LocationData(ACHIEVEMENT.It_Grew, 10002, REGION.Loops),
    LocationData(ACHIEVEMENT.Error, 10003, REGION.Start),
    LocationData(ACHIEVEMENT.Acrobat, 10004, REGION.Start),
    LocationData(ACHIEVEMENT.Bushes, 10005, REGION.Loops),
    LocationData(ACHIEVEMENT.Thousand_Hay, 10006, REGION.Start),
    LocationData(ACHIEVEMENT.Carrots, 10007, REGION.Loops),
    LocationData(ACHIEVEMENT.Thousand_Wood, 10008, REGION.Loops),
    LocationData(ACHIEVEMENT.Pumpkins, 10009, REGION.Loops),
    LocationData(ACHIEVEMENT.Thousand_Pumpkins, 10010, REGION.Loops),
    LocationData(ACHIEVEMENT.Feels_Good, 10011, REGION.Start),
    LocationData(ACHIEVEMENT.Higher_Order_Programming, 10012, REGION.Start),
    LocationData(ACHIEVEMENT.Sunflowers, 10013, REGION.Measure),
    LocationData(ACHIEVEMENT.Mud_Farm, 10014, REGION.Loops),
    LocationData(ACHIEVEMENT.Thousand_Power, 10015, REGION.Measure),
    LocationData(ACHIEVEMENT.Cacti, 10016, REGION.Swap),
    LocationData(ACHIEVEMENT.Thousand_Cactus, 10017, REGION.Swap),
    LocationData(ACHIEVEMENT.Thousand_Gold, 10018, REGION.Fertilizer),
    LocationData(ACHIEVEMENT.Treasure_Hunter, 10019, REGION.Fertilizer),
    LocationData(ACHIEVEMENT.Megafarm, 10020, REGION.Fertilizer),
    LocationData(ACHIEVEMENT.Fashionable, 10021, REGION.Start),
    # ... I didn't want to add everything yet
]

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
        region:Region = world.get_region(regionName)
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
