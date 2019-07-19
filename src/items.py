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
                         kind="melee",
                         dmg=1,
                         value=self.base * self.amount,
                         broken=False,
                         description="A Rock at the size as your fist. It hopefully will be enough for the beginning ",
                         amount=amount,
                         base=0
                         )


class Dagger(Weapon):

    def __init__(self, amount, base=5):
        self.amount = amount
        self.base = base
        super().__init__(name="Dagger",
                         kind="melee",
                         dmg=5,
                         value=self.base * self.amount,
                         broken=False,
                         description="A small knife, now we can fight!",
                         amount=amount,
                         base= 5
                         )


class Bow(Weapon):

    def __init__(self, amount, base=40):
        self.amount = amount
        self.base = base
        super().__init__(name="Bow",
                         kind="ranged",
                         dmg=10,
                         value=self.base * self.amount,
                         broken=False,
                         description="A bow with some arrows, let's shoot some monsters.",
                         amount=amount,
                         base=40
                         )


class Sword(Weapon):
    def __init__(self, amount, base=65):
        self.amount = amount
        self.base = base
        super().__init__(name="Sword",
                         kind="melee",
                         dmg=15,
                         value=self.base * self.amount,
                         broken=False,
                         description="A sword, now we can defend your self against all",
                         amount=amount,
                         base= 65
                         )


class Axe(Weapon):
    def __init__(self, amount, base=70):
      self.amount = amount
      self.base = base
      super().__init__(name="Axe",
                       kind="melee",
                       dmg=18,
                       value=base * self.amount,
                       broken=False,
                       description="Off with their heads",
                       amount=amount,
                       base = 130
                       )


class Gold(Item):
    def __init__(self, amount, base=1):
        self.amount = amount
        self.base = base
        super().__init__(name="Gold",
                         description="A round shiny Coin",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=1)

class Armor(Item):
    def __init__(self,description, value, name, amount, base, armor, part):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.base = base
        self.part = part
        self.armor = armor

class Leather_ChestPlate(Armor):
    def __init__(self, amount, base=10):
        self.part = "chest"
        self.amount = amount
        self.base = base
        self.armor = 1
        super().__init__(name = "Leather Chest Plate",
                         description = "A very tattered leather chestplate.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)

class Leather_Cap(Armor):
    def __init__(self, amount , base = 5):
        self.part = "head"
        self.amount = amount
        self.base = base
        self.armor = 0.5
        super().__init__(name = "Leather Cap",
                         description = "A leathern cap.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)

class Wooden_Shield(Armor):
    def __init__(self, amount , base = 15, armor = 1):
        self.part = "shield"
        self.amount = amount
        self.base = base
        self.armor = armor
        super().__init__(name="Wooden Shield",
                         description="A wooden shield, may it help.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)
