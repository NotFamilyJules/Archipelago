from __future__ import annotations

from typing import TYPE_CHECKING, Counter

from BaseClasses import CollectionState
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, True_, HasAny, CanReachLocation
from .Data.Strings import UPGRADE, RULE, REGION
from .locations import ALL_LOCATIONS
from .options import EasyMode
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
            world.set_rule(entrance, HasAll(*region_data.requirements))
        elif region_data.name == REGION.EndGame:
            entrance = world.get_entrance(region_data.entrance_name)
            world.set_rule(entrance, Has(UPGRADE.Expand, 9))


def set_all_location_rules(world: TFWRWorld) -> None:
    for location_data in ALL_LOCATIONS:
        if location_data.requirements is not None:
            location = world.get_location(location_data.name)
            world.set_rule(location, resolve_rules(location_data.requirements))


def resolve_rules(loc_requirements: list[str]) -> Rule[TFWRWorld]:
    rule = True_()

    # Build list of requirements
    requirements = Counter(loc_requirements)

    for requirement in requirements:
        if requirement not in RULE.Rules:
            if requirement not in UPGRADE.ALL_UPGRADES:
                # throw some error
                raise ValueError("This item is not contained in RULE.Rules or UPGRADE.ALL_UPGRADES")
            else:
                rule &= Has(requirement, count=requirements[requirement])
        else:
            match requirement:
                case RULE.AnyHatItems:
                    rule &= HasAny(UPGRADE.Hats, UPGRADE.TopHat)
                case RULE.ReallyBigFarm:
                    rule &= Has(UPGRADE.Expand, 9)
                case _:
                    # throw some error
                    raise ValueError(
                        "Great job! You made a string for a rule, but forgot to actually make the rule in rules.py[resolve_rules]")
    return rule


def set_completion_condition(world: TFWRWorld) -> None:
    """How do you win?"""
    world.set_completion_rule(
        CanReachLocation("Gold Farmer", options=[OptionFilter(EasyMode, True)])
        | CanReachLocation("Size Matters", options=[OptionFilter(EasyMode, False)])
    )
