from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, CollectionRule
from .Data.Strings import VICTORY, UPGRADE, REGION, ACHIEVEMENT
from .locations import ACHIEVEMENTS
from .regions import ALL_REGION_DATA

if TYPE_CHECKING:
    from .world import TFWRWorld

# Rules define the requirements to move between regions (as in, use an entrance)

def set_all_rules(world: TFWRWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: TFWRWorld) -> None:
    for region_data in ALL_REGION_DATA:
        if region_data.requirements is not None:
            entrance = world.get_entrance(region_data.entrance_name)
            for requirement in region_data.requirements:
                set_rule(entrance, lambda state: state.has(requirement, world.player))


def has_completed_location_count(state:CollectionState, world:TFWRWorld, count: int) -> bool:
    actual = 0

    actual += [state.can_reach(location) if 1 else 0 for location in world.get_locations()]
    return actual >= count

def set_all_location_rules(world: TFWRWorld) -> None:
    pass

def set_completion_condition(world: TFWRWorld) -> None:
    # How do you win? Use world.options.<> to change the condition
    if world.options.easy_mode:
        world.multiworld.completion_condition[world.player] = lambda state: (
            sum(state.can_reach_location(l.name, world.player) for l in ACHIEVEMENTS) >= 5
        )
    else:
        world.multiworld.completion_condition[world.player] = lambda state: (
            sum(state.can_reach_location(l.name, world.player) for l in ACHIEVEMENTS) >= 15
        )