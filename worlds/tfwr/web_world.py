from BaseClasses import Tutorial

from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class TFWRWebWorld(WebWorld):
    game = "The Farmer Was Replaced"

    theme = "dirt"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up The Farmer Was Replaced for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Seadoggie"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets