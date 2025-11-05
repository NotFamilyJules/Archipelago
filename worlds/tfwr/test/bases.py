from test.bases import WorldTestBase

from ..world import TFWRWorld

class TFWRTestBase(WorldTestBase):
    game = "The Farmer Was Replaced"
    world: TFWRWorld