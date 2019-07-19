class Enemy:
    """A base class for all enemies"""

    def __init__(self, name, hp, damage, armor, exp):
        """Creates a new enemy
        :param name: the name of the enemy
        :param hp: the hit points of the enemy
        :param damage: the damage the enemy does with each attack
        :param armor: the amount of damage that is negated
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.exp = exp

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=3, armor=1, exp=10)


class Spider(Enemy):
    def __init__(self):
        super().__init__(name="Spider", hp=3, damage=1, armor=0, exp=5)


class Troll(Enemy):
    def __init__(self):
        super().__init__(name="Troll", hp=20, damage=2, armor=2, exp=15)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=15, damage=5, armor=1, exp=10)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=25, damage=2, armor=4, exp=20)



class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=6, damage=3, armor=0, exp=10)



class Ghost(Enemy):
    def __init__(self):
        super().__init__(name="Ghost", hp=5, damage=10, armor=2, exp=20)



class Bat(Enemy):
    def __init__(self):
        super().__init__(name="Bat", hp=1, damage=1, armor=1, exp=2)
