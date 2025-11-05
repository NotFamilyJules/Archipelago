from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from BaseClasses import Region
from .Data.Strings import REGION, UPGRADE

if TYPE_CHECKING:
    from .world import TFWRWorld


@dataclass
class RegionData:
    name: str
    parent: str = None
    requirements: list[str] | None = None
    entrance_name: str = ""

    def __post_init__(self):
        if self.parent is not None:
            self.entrance_name = f"{self.parent} to {self.name}"


# This list must be sorted like a hierarchy: Dependent regions come after its dependents
ALL_REGION_DATA: list[RegionData] = [
    RegionData(REGION.Start),
    RegionData(REGION.Loops, REGION.Start, [UPGRADE.Loop]),
    RegionData(REGION.Swap, REGION.Loops, [UPGRADE.Cactus]),
    RegionData(REGION.Fertilizer, REGION.Loops, [UPGRADE.Fertilizer]),
    RegionData(REGION.Measure, REGION.Fertilizer, None),
]


def create_and_connect_regions(world: TFWRWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: TFWRWorld) -> None:
    # Create regions and add them to the world object here.
    regions: list[Region] = [Region(region.name, world.player, world.multiworld) for region in ALL_REGION_DATA]

    # variable = Region("Name", world.player, world.multiworld)

    # Add all regions to a list

    # Some regions might be optional
    # if ####:
    #     regions.append(Region("Optional Region", world.player, world.multiworld))

    # Be sure to use += to avoid overwriting regions
    world.multiworld.regions += regions


def connect_regions(world: TFWRWorld) -> None:
    """Connect regions via entrances"""

    # get all regions by name
    # region = world.get_region("Region 1 Name")

    # probably should cache results from world.get_region?
    regions: dict[str, Region] = {}

    #achievement_region: Region | None = None

    regionData: RegionData
    for regionData in ALL_REGION_DATA:
        region = world.get_region(regionData.name)
        regions[regionData.name] = region
        # Set up entrance if needed
        if regionData.parent is not None:
            regions[regionData.parent].connect(region, regionData.entrance_name)

    # Entrances can be optional
    # if ####:
    #     region1.connect(region3, "Optional Entrance Name")
