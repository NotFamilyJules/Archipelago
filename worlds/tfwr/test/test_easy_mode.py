import os

import Utils
from BaseClasses import Location, Region
from .bases import TFWRTestBase
from ..Data.Strings import REGION


class TestEasyModeLogic(TFWRTestBase):
    """I'm really just copying APQuest for now"""

    options = {
        "easy_mode": True,
    }

    def test_easy_mode_access(self) -> None:
        with self.subTest("Tests checks accessible with nothing"):
            hello_world: Location = self.world.get_location("Hello World!")

            self.assertTrue(hello_world.can_reach(self.multiworld.state))

        with self.subTest("Regions are set up correctly"):
            start: Region = self.world.get_region(REGION.Start)
            self.assertEqual(len(start.entrances), 0, "Start is the start, it shouldn't have entrances")
            self.assertTrue(start.can_reach(self.multiworld.state), "Start should always be accessible")

            loops: Region = self.world.get_region(REGION.Loops)
            self.assertEqual(len(loops.entrances), 1, "Loops should have an entrance from Start")

        with self.subTest("Create visualization"):
            """ This builds PUML files, it is not a test """
            state = self.multiworld.get_all_state(False)
            state.update_reachable_regions(self.player)
            folder: str = os.getcwd() + "/worlds/tfwr/test/visualization/"
            regions: list[str] = ["Start"]
            for region in regions:
                Utils.visualize_regions(self.world.get_region(region),
                                        folder + region + "_Easy.puml",
                                        regions_to_highlight=state.reachable_regions[self.player],
                                        )
