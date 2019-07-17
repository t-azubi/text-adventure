from Player import Character
from items import Item


class Merchant:
    """A base class for the merchant"""

    def __init__(self, name, gold, items):

        self.name = name
        self.gold = gold
        self.items = items

    def has_gold(self):
        return self.gold > 0


merchant_items = ["sword", "axe", "hammer"]


########
if Merchant.gold > 0:
    print("You can sell items to the merchant.")
elif Merchant.gold == 0:
    print("You cant sell items to the merchant.")

if Character.inventory. > 0  ### zugriff auf gold des characters ?
    player can buy items from merchant
    elif
    player gold == 0
    player cant buy item
########

selling von items dann durch appenden der merchant item list

zuweisen von values zu den items in der liste ?


##player selling items

merchant_items = ["sword", "axe", "hammer"]
print(merchant_items)
merchant_items.append(input("Which items do you want to sell? "))


##player buying items
print(merchant_items)
merchant_items.remove(input("Which items do you want to buy? "))
