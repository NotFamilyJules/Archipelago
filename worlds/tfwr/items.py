from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from .Data.Strings import FILLER, UPGRADE

if TYPE_CHECKING:
    from .world import TFWRWorld


# Items are receivables. Can be sent by somebody to you.

@dataclass
class ItemData:
    name: str
    id: int
    count: int = 1
    classification: ItemClassification = ItemClassification.progression
    secondary_count: int = 0
    secondary_classification: ItemClassification = ItemClassification.filler


# How to handle multiple upgrades? At least one is needed for logic, others are nice to have
UPGRADES: list[ItemData] = [
    ItemData(UPGRADE.Loop, 11001),
    ItemData(UPGRADE.Drone_Speed, 11002, 5),
    ItemData(UPGRADE.Hats, 11003),
    ItemData(UPGRADE.Grass, 11004, secondary_count=9),
    ItemData(UPGRADE.Expand, 11005, 9),
    ItemData(UPGRADE.Plant, 11006),
    ItemData(UPGRADE.Carrot, 11007, secondary_count=9),
    ItemData(UPGRADE.Watering, 11008, secondary_count=8),
    ItemData(UPGRADE.Fertilizer, 11009, secondary_count=3),
    ItemData(UPGRADE.Sunflowers, 11010),
    ItemData(UPGRADE.Mazes, 11011, secondary_count=5),
    ItemData(UPGRADE.TopHat, 11012),
    ItemData(UPGRADE.Trees, 11013, secondary_count=9),
    ItemData(UPGRADE.Pumpkins, 11014, secondary_count=9),
    ItemData(UPGRADE.Polyculture, 11015, 5, ItemClassification.useful),
    ItemData(UPGRADE.Cactus, 11017, secondary_count=5),
    ItemData(UPGRADE.Dinosaurs, 11018, secondary_count=5),
    ItemData(UPGRADE.TheFarmersRemains, 11019),
    ItemData(UPGRADE.Megafarm, 11020, 5),
    ItemData(UPGRADE.Debug, 11021),
    ItemData(UPGRADE.MoreDebug, 11022, 1, ItemClassification.filler),
    ItemData(UPGRADE.Timing, 11023, 1, ItemClassification.filler),
    ItemData(UPGRADE.Simulation, 11024, 1, ItemClassification.filler),
    ItemData(UPGRADE.Operators, 11026),
    ItemData(UPGRADE.Senses, 11027, 1, ItemClassification.filler),
    ItemData(UPGRADE.Variables, 11028),
    ItemData(UPGRADE.Functions, 11029),
    ItemData(UPGRADE.Import, 11030),
    ItemData(UPGRADE.Utilities, 11031, 1, ItemClassification.filler),
    ItemData(UPGRADE.Lists, 11032),
    ItemData(UPGRADE.Dictionaries, 11033),
    ItemData(UPGRADE.Costs, 11034, ItemClassification.filler),
    ItemData(UPGRADE.Unlock, 11035, ItemClassification.filler),
]

FILLERS: list[ItemData] = [
    ItemData(FILLER.Free_Hay, 12001, ItemClassification.filler),
]

ALL_ITEMS: list[ItemData] = (
        UPGRADES
        + FILLERS
)

ITEM_NAME_TO_ID: dict[str, int] = {item.name: item.id for item in ALL_ITEMS}

DEFAULT_ITEM_CLASSIFICATIONS: dict[str, ItemClassification] = {item.name: item.classification for item in ALL_ITEMS}


class TFWRItem(Item):
    game = "The Farmer Was Replaced"


def get_random_filler_item_name(world: TFWRWorld) -> str:
    # Optionally, use a trap's name here with a random chance
    return FILLER.Free_Hay


def create_item_with_correct_classification(world: TFWRWorld, name: str,
                                            classification: ItemClassification | None = None) -> TFWRItem:
    if classification is None:
        classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return TFWRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: TFWRWorld) -> None:
    item_pool: list[TFWRItem] = []
    # Create every upgrade item
    for item in UPGRADES:
        # for each copy needed
        for i in range(0, item.count):
            item_pool.append(create_item_with_correct_classification(world, item.name, item.classification))
        # for each secondary copy
        for i in range(0, item.secondary_count):
            item_pool.append(create_item_with_correct_classification(world, item.name, item.secondary_classification))

    # Get count of items
    number_of_items: int = len(item_pool)
    # Get count of missing items
    number_of_unfilled_locations: int = len(world.multiworld.get_unfilled_locations(world.player))
    # How many filler items should we create?
    needed_number_of_filler_items: int = number_of_unfilled_locations - number_of_items
    # Create filler items
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    # Save the items to the multiworld
    world.multiworld.itempool += item_pool
