from __future__ import annotations

import typing
from typing import TYPE_CHECKING
from dataclasses import dataclass
from BaseClasses import Item, ItemClassification
from .Data.Strings import FILLER, UPGRADE
from ..hk.Items import item_type

if TYPE_CHECKING:
    from .world import TFWRWorld


# Items are receivables. Can be sent by somebody to you.

@dataclass
class ItemData:
    name: str
    id: int
    count: int = 1
    classification: ItemClassification = ItemClassification.progression

# How to handle multiple upgrades? At least one is needed for logic, others are nice to have
UPGRADES: list[ItemData] = [
    ItemData(UPGRADE.Loop, 11001),
    ItemData(UPGRADE.Drone_Speed, 11002, 3),
    ItemData(UPGRADE.Hats, 11003),
    ItemData(UPGRADE.Grass, 11004, 10),
    ItemData(UPGRADE.Expand, 11005, 9),
    ItemData(UPGRADE.Plant, 11006),
    ItemData(UPGRADE.Carrot, 11007, 10),
    ItemData(UPGRADE.Watering, 11008, 9),
    ItemData(UPGRADE.Fertilizer, 11009, 4),
    ItemData(UPGRADE.Sunflowers, 11010),
    ItemData(UPGRADE.Mazes, 11011, 6),
    ItemData(UPGRADE.TopHat, 11012),
    ItemData(UPGRADE.Trees, 11013, 10),
    ItemData(UPGRADE.Pumpkins, 11014, 10),
    ItemData(UPGRADE.Polyculture, 11015, 5),
    ItemData(UPGRADE.Cactus, 11017, 6),
    ItemData(UPGRADE.Dinosaurs, 11018, 6),
    ItemData(UPGRADE.Unknown, 11019),
    ItemData(UPGRADE.Megafarm, 11020, 5),
]

FILLERS: list[ItemData] = [
    ItemData(FILLER.Free_Hay, 12001, ItemClassification.filler),
]

ALL_ITEMS: list[ItemData] = (
    UPGRADES
    +FILLERS
)

ITEM_NAME_TO_ID: dict[str, int] = { item.name: item.id for item in ALL_ITEMS }

DEFAULT_ITEM_CLASSIFICATIONS: dict[str, ItemClassification] = { item.name: item.classification for item in ALL_ITEMS }

class TFWRItem(Item):
    game = "The Farmer Was Replaced"


def get_random_filler_item_name(world: TFWRWorld) -> str:
    # Optionally, use a trap's name here with a random chance
    return FILLER.Free_Hay


def create_item_with_correct_classification(world: TFWRWorld, name: str) -> TFWRItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return TFWRItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: TFWRWorld) -> None:
    item_pool: list[TFWRItem] = [ world.create_item(item.name) for item in UPGRADES ]

    number_of_items: int = len(item_pool)

    number_of_unfilled_locations: int = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items: int = number_of_unfilled_locations - number_of_items

    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += item_pool
