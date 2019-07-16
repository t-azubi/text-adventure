class Item():
    """The base class for all items"""

    def __init__(self, name, description, value, amount, base):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.base = base

    def __str__(self):
        return "{}\n{}\nValue: {}\nAmount: {}\n".format(self.name, self.description, self.value, self.amount)


class Weapon(Item):
    def __init__(self, name, kind, dmg, value, broken, description, amount, base):
        self.name = name
        self.kind = kind
        self.dmg = dmg
        self.value = value
        self.broken = broken
        self.description = description
        self.amount = amount
        self.base = base


class Rock(Weapon):
    def __init__(self, amount, base=0):
        self.amount = amount
        self.base = base
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=1,
                         value=self.base * self.amount,
                         broken=False,
                         description="A Rock at the size as your fist. It hopefully will be enough for the beginning ",
                         amount=amount,
                         base=0
                         )


class Dagger(Weapon):
    def __init__(self, amount, base=10):
        self.amount = amount
        self.base = base
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=5,
                         value=self.base * self.amount,
                         broken=False,
                         description="A small knife, now we can fight!",
                         amount=amount,
                         base=10
                         )


class Bow(Weapon):
    def __init__(self, amount, base=20):
        self.amount = amount
        self.base = base
        super().__init__(name="Rock",
                         kind="range",
                         dmg=10,
                         value=self.base * self.amount,
                         broken=False,
                         description="A bow with some arrows, let's shoot some monsters.",
                         amount=amount,
                         base=20
                         )


class Sword(Weapon):
    def __init__(self, amount, base=25):
        self.amount = amount
        self.base = base
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=15,
                         value=self.base * self.amount,
                         broken=False,
                         description="A sword, now we can defend your self against all",
                         amount=amount,
                         base=25
                         )


class Axe(Weapon):
    def __init__(self, amount, base=35):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=18,
                         value=base * self.amount,
                         broken=False,
                         description="Off with their heads",
                         amount=amount
                         )


class Gold(Item):
    def __init__(self, amount, base=1):
        self.amount = amount
        self.base = base
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amount)),
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=1)
