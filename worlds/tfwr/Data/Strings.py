class UPGRADE:
    """Upgrades in game. Used as items."""
    Loop = "Loop"
    Drone_Speed = "Drone Speed"
    Hats = "Hats"
    Grass = "Grass"
    Expand = "Expand"
    Plant = "Plant"
    """Plant anything. Also gives bushes."""
    Carrot = "Carrot"
    Watering = "Watering"
    Cactus = "Cactus"
    Fertilizer = "Fertilizer"
    Sunflowers = "Sunflowers"
    Mazes = "Mazes"
    """Unlocks or expands the max maze size"""
    TopHat = "Top Hat"
    Trees = "Trees"
    Pumpkins = "Pumpkins"
    Polyculture = "Polyculture"
    Dinosaurs = "Dinosaurs"
    Megafarm = "Megafarm"
    """Drones"""
    TheFarmersRemains = "TheFarmersRemains"
    Debug = "Debug"
    MoreDebug = "More Debug"
    Timing = "Timing"
    Simulation = "Simulation"
    Leaderboard = "Leaderboard"
    Operators = "Operators"
    Senses = "Senses"
    Variables = "Variables"
    Functions = "Functions"
    Import = "Import"
    Utilities = "Utilities"
    Lists = "Lists"
    Dictionaries = "Dictionaries"
    Costs = "Costs"
    Unlock = "Unlock"
    ALL_UPGRADES: list[str] = [
        Loop, Drone_Speed, Hats, Grass, Expand, Plant, Carrot, Watering, Cactus, Fertilizer, Sunflowers,
        Mazes, TopHat, Trees, Pumpkins, Polyculture,
        Dinosaurs, Megafarm, TheFarmersRemains,
        Debug, MoreDebug, Timing, Simulation, Leaderboard,
        Operators, Senses, Variables, Functions, Import, Utilities,
        Lists, Dictionaries, Costs, Unlock
    ]


class FILLER:
    Free_Hay = "Free Hay"


class REGION:
    Start = "Start"
    Loops = "Loops"
    Sunflower = "Sunflower"
    Cactus = "Cactus"
    Maze = "Maze"
    Pumpkins = "Pumpkins"
    Drones = "Drones"
    Dinos = "Dinos"
    EndGame = "EndGame"
    Regions: list[str] = [Start, Loops, Sunflower, Cactus, Maze, Pumpkins, Drones, Dinos, EndGame]


class RULE:
    """Custom rules to be manually resolved"""
    AnyHatItems = "AnyHatItems"
    """the player has any hats"""
    ReallyBigFarm = "Really Big Farm"
    """the player has all of the expansions"""
    Rules: list[str] = [
        AnyHatItems, ReallyBigFarm,
    ]
