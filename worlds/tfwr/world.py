from collections.abc import Mapping
from typing import Any

import Utils
# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world
from .Data.Strings import REGION

class TFWRWorld(World):
    """
    Program and optimize a drone to automate a farm and watch it do the work for you. Collect resources to unlock better technology and become the most efficient farmer in the world. Improve your problem solving and coding skills.
    """

    game = "The Farmer Was Replaced"

    web = web_world.TFWRWebWorld()

    options_dataclass = options.TFWROptions
    # Something about mutability causes an error in PyLance
    options: options.TFWROptions # type: ignore

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = REGION.Start

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TFWRItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "easy_mode",
        )

    def pre_fill(self):
        from BaseClasses import CollectionState
        from Fill import sweep_from_pool
        state = sweep_from_pool(CollectionState(self.multiworld), self.multiworld.itempool)
        unreachable_locations = [location for location in self.get_locations() if not location.can_reach(state)]
        assert not unreachable_locations, f"All state can't reach all locations: {unreachable_locations}"