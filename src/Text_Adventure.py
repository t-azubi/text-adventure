# name: Richard
# date: 08-07-2019
# description: text-based adventure game
import sys

import IdelOption
import Room
from Classes import Quotes, GenPaths
from Player import Character



############### Changes to be made ###############
#
# input auf (done)
# waffe kann kaputt gehen, brauchen noch random chance dafür
#

#
#
#### Erik ist ein trunkenbold #####
#
#
#k
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
        room.modify_player(room(), player)


def enemyRoom(room, player):
    if room == Room.OgreRoom or room == Room.GiantSpiderRoom:
        print(room.intro_text(room().enemy))
        actions = room().available_actions()
        for x in actions:
            print(x.name)
        while room().enemy.is_alive():
            action = input(str(">Please type what you want to do\n"))
            if action.upper() == "ATTACK":
                player.attack(enemy=room().enemy)
            else:
                player.flee()
                return
    else:
        print(room.intro_text(self=room))

player = Character()
rooms = Room
rooms.StartingRoom.intro_text(self=rooms)
print("> You look around an find some items\n")
Character.print_inventory(player)
option = IdelOption.Option
GenPaths.path_gen()
room = rooms.Gen_Current_Room.gen()
enemyRoom(room=room, player=player)
modRoom(room=room, player=player)
while player.is_alive() and not player.victory:
    option.desciption(player)
    GenPaths.path_gen()
    room = rooms.Gen_Current_Room.gen()
    enemyRoom(room=room, player=player)
    modRoom(room=room, player=player)
