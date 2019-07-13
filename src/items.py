class Item():
    """The base class for all items"""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, kind, dmg, value, broken, description):
        self.name = name
        self.kind = kind
        self.dmg = dmg
        self.value = value
        self.broken = broken
        self.description = description


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=1,
                         value=0,
                         broken=False,
                         description="A Rock at the size as your fist. It hopefully will be enough for the beginning "
                         )


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=5,
                         value=10,
                         broken=False,
                         description="A small knife, now we can fight!"
                         )


class Bow(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="range",
                         dmg=10,
                         value=20,
                         broken=False,
                         description="A bow with some arrows, let's shoot some monsters."
                         )


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=15,
                         value=25,
                         broken=False,
                         description="A sword, now we can defend your self against all"
                         )


class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=18,
                         value=35,
                         broken=False,
                         description="Off with their heads"
                         )


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
