class Item():
    """The base class for all items"""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon:

    def __init__(self, name, kind, dmg, worth, broken):
        self.name = name
        self.kind = kind
        self.dmg = dmg
        self.worth = worth
        self.broken = broken

    def can_attack(self):
        if not self.broken:
            return True
        else:
            return False


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=1,
                         worth=0,
                         broken=Weapon.can_attack()
                         )


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=5,
                         worth=10,
                         broken=Weapon.can_attack()
                         )


class Bow(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=1,
                         worth=0,
                         broken=Weapon.can_attack()
                         )


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=1,
                         worth=0,
                         broken=Weapon.can_attack()
                         )


class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         kind="meele",
                         dmg=1,
                         worth=0,
                         broken=Weapon.can_attack()
                         )


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
