from Player import Character
from items 


class Merchant:
    """A base class for the merchant"""

    def __init__(self, name, gold = 100, items):

        self.name = name
        self.gold = items.Gold(100)
        self.items = [items.Axe(1), items.Sword(1), items.Hammer(1)]

    def has_gold(self):
        return self.gold > 0

#hammer should be added to the items class

########
if Merchant.gold == 0:
    print("You can sell items to the merchant.")
elif Merchant.gold > 100:
    print("You cant sell items to the merchant.")

if  Character.inventory[0].amount > 0  
    player can buy items from merchant
    elif
    player gold == 0
    player cant buy item
########

selling von items dann durch appenden der merchant item list

zuweisen von values zu den items in der liste ?


##player selling items
def sell(self, merchant):
 for item in player_inventory 
    print(item)
 bool = False
 item = (input("Which items do you want to sell? "))
 for items in the_player.inventory:
            if items.name.upper == item.upper():
                if items.amount > 0 :
                the_player.inventory[0].amount += items.value
                items.amount -= 1
                for mitems in merchant.items:
                    if mitems.name == item.name:
                    mitems.amount += item.amount
                    mitems.value = mitems.base * mitems.amount
                    bool = True
                if bool == False:
                    merchant.items.append(item)


##player buying items
   for item in merchant_items 
    print(item)
merchant_items.remove(input("Which items do you want to buy? "))
