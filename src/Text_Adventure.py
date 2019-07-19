# name: Richard
# date: 08-07-2019
# description: text-based adventure game
import sys

import IdelOption
import Room
from Classes import Quotes, GenPaths
from Player import Character
import merchant


############### Changes to be made ###############
#
# input auf upper/ lower(done)
# waffe kann kaputt gehen, brauchen noch random chance dafür
#
#
#
#
#### Erik ist ein trunkenbold #####
#
#
#
#
#
##################################################


def displayIntro():
    print("#############################################")
    print("##                                         ##")
    print("##                WELCOME                  ##")
    print("##          TO THE ADVENTURES OF           ##")
    print("##          GERWALD OF WALDSTETT           ##")
    print("##                                         ##")
    print("##          Type: START to start           ##")
    print("##       Type: HELP to receive help        ##")
    print("##       Type: QUIT to quit the game       ##")
    print("##  Type: LANGUAGE to change the language  ##")
    print("##                                         ##")
    print("#############################################")


def IntroQuestion(intro):
    if intro.upper() == "START":
        print("\n> Alright, so let us start the adventure of Gerwald of Waldstett!")
        # time.sleep(1.5)
        Story(intro)
    elif intro.upper() == "HELP":
        print("\nINSTRUCTIONS, just follow along the questions and just input the things you are allowed to!!!")
        # time.sleep(1.5)
        Help(intro)
    elif intro.upper() == "QUIT":
        print("\n#######################################")
        print("##                                   ##")
        print("##  Thank you for playing the game.  ##")
        print("##                                   ##")
        print("#######################################")
        sys.exit()
    else:
        intro = str(input("\nPlease enter one of the commands above: "))
        IntroQuestion(intro)


def Story(intro):
    if intro.upper() == "START":
        # time.sleep(1.5)
        print("\n> I hope you brought enough time and i hope you have fun playing.")
    else:
        intro = str(input("\n" + Quotes.invalid_input()))
        IntroQuestion(intro)


def Help(intro):
    if intro.upper() == "HELP":
        intro = input("\nIf you are ready to start the game, enter the START command! ")
        IntroQuestion(intro)
    else:
        intro = str(input("\n" + Quotes.invalid_input()))
        IntroQuestion(intro)


displayIntro()
intro = str(input("\n> Please state what you want to do! \n"))
IntroQuestion(intro)

# time.sleep(1.5)
print(
    "\n> And so the tale begins. Years ago in the land of Ghrezok, there lived a man named Gerwald in a city called Waldstett.")
# time.sleep(1.5)


def modRoom(room, player):
    if room != Room.EmptyCavePath:
        room.modify_player(player)


def enemyRoom(room, player):
    if room.name == "enemyroom":
        print(room.intro_text())
        actions = room.available_actions()
        for x in actions:
            print(x.name)
        while room.enemy.is_alive():
            action = input(str(">Please type what you want to do\n"))
            if action.upper() == "ATTACK":
                player.attack(enemy=room.enemy)
            elif action.upper() == "FLEE":
                player.flee()
                player.fledFromRoom += 1
                Room.Gen_Current_Room().gen()
                player.roomcounter += 1
                return player
            else:
                print(">Invalid input")
        player.slayedEnemies += 1
        enemy = room.enemy
        exp = enemy.exp * (1 + (player.roomcounter / 10))
        print(">{} drops {} exp.".format(enemy.name, exp))
        player.exp[1] += exp
        player.exp = player.update_lvl()
        return player
    elif room.name == "merchantroom":
        print(room.intro_text())
        action = input(str("> Do you want to sell, buy or leave?\n"))
        merch = merchant.Merchant()
        merch.items = merch.gen_listofitems()
        while not action.lower() == "leave":
            if action.upper() == "SELL":
                merch = player.sell(merch)
                action = input(str("\nDo you want to buy or sell something other or leave?"))
            elif action.upper() == "BUY":
                 merch = player.buy(merch)
                 action = input(str("\nDo you want to buy or sell something other or leave?"))
            else:
                action = input()
    else:
        print(room.intro_text())
    return player

player = Character()
Room.StartingRoom.intro_text(Room)
print("> You look around an find some items\n")
Character.print_inventory(player)
option = IdelOption.Option
GenPaths().path_gen()
player.roomcounter += 1
room = Room.Gen_Current_Room().gen()
player = enemyRoom(room=room, player=player)
modRoom(room=room, player=player)
while player.is_alive() and not player.victory:
    option.desciption(player)
    GenPaths().path_gen()
    player.roomcounter += 1
    room = Room.Gen_Current_Room().gen()
    player = enemyRoom(room=room, player=player)
    modRoom(room=room, player=player)
