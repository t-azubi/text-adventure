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

class Chainmail_ChestPlate(Armor):
    def __init__(self, amount, base=50):
        self.part = "chest"
        self.amount = amount
        self.base = base
        self.armor = 2
        super().__init__(name = "Chainmail Chest Plate",
                         description = "A Chainmail chestplate.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)

class Iron_ChestPlate(Armor):
    def __init__(self, amount, base=150):
        self.part = "chest"
        self.amount = amount
        self.base = base
        self.armor = 5
        super().__init__(name = "Iron Chest Plate",
                         description = "A strong looking Iron chestplate.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)

class Steel_ChestPlate(Armor):
    def __init__(self, amount, base=210):
        self.part = "chest"
        self.amount = amount
        self.base = base
        self.armor = 7
        super().__init__(name = "Steel Chest Plate",
                         description = "A steel chestplate.",
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
class Chainmail_Cap(Armor):
    def __init__(self, amount , base = 30):
        self.part = "head"
        self.amount = amount
        self.base = base
        self.armor = 1.5
        super().__init__(name = "Chainmail Cap",
                         description = "A Chainmail cap, will safe your head.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)
class Iron_Cap(Armor):
    def __init__(self, amount , base = 55):
        self.part = "head"
        self.amount = amount
        self.base = base
        self.armor = 2
        super().__init__(name = "Iron Cap",
                         description = "A iron cap.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)
class Viking_Cap(Armor):
    def __init__(self, amount , base = 85):
        self.part = "head"
        self.amount = amount
        self.base = base
        self.armor = 5
        super().__init__(name = "Viking Cap",
                         description = "A cap from a Viking, it looks pretty cool.",
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
class Iron_Shield(Armor):
    def __init__(self, amount , base = 95, armor = 3):
        self.part = "shield"
        self.amount = amount
        self.base = base
        self.armor = armor
        super().__init__(name="Iron Shield",
                         description="A Iron shield, let's fight.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)
class Reinforced_Wooden_Shield(Armor):
    def __init__(self, amount , base = 55, armor = 2):
        self.part = "shield"
        self.amount = amount
        self.base = base
        self.armor = armor
        super().__init__(name="Reinforced Wooden Shield",
                         description="A reinforced wooden shield, it looks like this will protect you very well.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)

class Reinforced_Wooden_Shield(Armor):
    def __init__(self, amount , base = 150, armor = 5):
        self.part = "shield"
        self.amount = amount
        self.base = base
        self.armor = armor
        super().__init__(name="Reinforced Iron Shield",
                         description="A strong reinforced Iron shield. It's is like a wall protecting you.",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         armor=self.armor,
                         part=self.part)


class Potion(Item):
    def __init__(self,description, value, name, amount, base,heal):
        self.name = name
        self.description = description
        self.value = value
        self.amount = amount
        self.base = base
        self.heal = heal

class SmallPotion(Potion):
    def __init__(self,amount, base = 10):
        self.base = base
        self.amount = amount
        super().__init__(
                         name="Small healing potion",
                         description="A small healing Potion, which heals you by {}HP".format(self.base),
                         value= self.base * self.amount,
                         amount= self.amount,
                         base= self.base,
                         heal= base)

class MediumPotion(Potion):
    def __init__(self, amount, base = 30):
        self.base = base
        self.amount = amount
        super().__init__(
                         name="Medium healing potion",
                         description="A medium healing Potion, which heals you by {}HP".format(self.base),
                         value= self.base * self.amount,
                         amount= self.amount,
                         base= self.base,
                         heal= base)

class BigPotion(Potion):
    def __init__(self, amount, base = 70):
        self.base = base
        self.amount = amount
        super().__init__(name="Big healing potion",
                         description="A big healing Potion, which heals you by {}HP".format(self.base),
                         value= self.base * self.amount,
                         amount= self.amount,
                         base= self.base,
                         heal= base)

class Potionplus(Potion):
    def __init__(self, amount, base=70, heal= 10000):
        self.base = base
        self.amount = amount
        super().__init__(name="Big healing potion",
                         description="A big healing Potion, which heals to max hp",
                         value=self.base * self.amount,
                         amount=self.amount,
                         base=self.base,
                         heal=heal)