# name: Richard
# date: 08-07-2019
# description: text-based adventure game
import random
import time
import sys

from .Classes import Room , quotes, actions

############### Changes to be made ###############
#
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


displayIntro()


def IntroQuestion(intro):
    if intro.upper == "START" :
        print("\n> Alright, so let us start the adventure of Gerwald of Waldstett!")
        #time.sleep(1.5)
        return Story(intro)
    elif intro.upper == "HELP":
        print("\nINSTRUCTIONS, just follow along the questions and just input the things you are allowed to!!!")
        #time.sleep(1.5)
        return Help(intro)
    elif intro.upper == "QUIT":
        print("\n#######################################")
        print("##                                   ##")
        print("##  Thank you for playing the game.  ##")
        print("##                                   ##")
        print("#######################################")
        sys.exit()
    else:
        intro = str(input("\nPlease enter one of the commands above: "))
        return IntroQuestion(intro)


def Story(intro):
    if intro.upper == "START":
        #time.sleep(1.5)
        print("\n> I hope you brought enough time and i hope you have fun playing.")
        return
    else:
        intro = str(input("\n"+ quotes.invaildCommand))
        return IntroQuestion(intro)

def Help(intro):
    if intro.upper == "HELP":
        intro = input("\nIf you are ready to start the game, enter the START command! ")
        return IntroQuestion(intro)
    else:
        intro = str(input("\n"+ quotes.invaildCommand))
        return IntroQuestion(intro)

intro = str(input("\n> Please state what you want to do! \n"))

IntroQuestion(intro)


#time.sleep(1.5)
print("\n> And so the tale begins. Years ago in the land of Ghrezok, there lived a man named Gerwald in a city called Waldstett.")
#time.sleep(1.5)
print("\n> You now have the choice of choosing one of two paths. Type (1) to choose path one or (2) to choose path two.")


def Path(choose_path):
    if choose_path == "1":
        print("\n> Alright, you chose the first path")
        return 1
    elif choose_path == "2":
        print("\n> You chose path 2")
        return 2
    else:
        choose_path = str(input(quotes.invaildCommand))
        return Path(choose_path)

choose_path = str(input("\n> Enter your choice: "))

Path(choose_path)


def Path1(action):
    if action.upper == actions.LOOK:
        print("> You are looking around")
        return
    elif action.upper == "TAKE":
        print("> There is nothing to take yet.")
        return
    elif action.upper == "ATTACK" or action == "attack":
        print("> There is nothing to attack yet.")
        return
    else:
        action = str(input("> Please enter a valid command! "))
        return Path1(action)


action = str(input("\n> What do you want to do, you can LOOK, TAKE or ATTACK: "))


while Path(choose_path) == 1:
    Path1(action)
    action = str(input("\n> What do you want to do, you can LOOK, TAKE or ATTACK: "))
    if action == "leave" or action == "LEAVE":
        break



print("well done, you broke our loop")
