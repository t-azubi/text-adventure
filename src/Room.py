class Room:

    def __init__(self, size, props, loot, enemies):
        self.size = size
        self.props = props
        self.loot = loot
        self.enemies = enemies


class SpiderRoom(Room):
    def __init__(self):
        super().__init__(size="big", props="chairs", loot="gold", enemies="Spiders")


class TrollRoom(Room):
    def __init__(self):
        super().__init__(size="big", props="chairs", loot="gold", enemies="Troll")


class OgreRoom(Room):
    def __init__(self):
        super().__init__(size="big", props="chairs", loot="gold", enemies="Ogre")


class LootRoom(Room):
    def __init__(self):
        super().__init__(size="big", props="chest", loot="item", enemies="non")


class TradeRoom(Room):
    def __init__(self):
        super().__init__(size="big", props="merchant", loot="gold", enemies="non")


class StartingRoom():
    def intro_text():
        print(">You find yourself if a cave with a flickering torch on the wall.")
