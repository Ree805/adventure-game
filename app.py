import time
import random
monsters=["magician","demon","sprite"]
monster=random.choice(monsters)

def print_pause(message):
    print(message)
    time.sleep(2)
# Things that happen when the player runs back to the field
def field():
    print_pause("""You find yourself standing in an open field, filled with grass,and yellow wildflowers.""" )
    print_pause("Rumor has it that a " + monster + " is somewhere around here,and has been terrifying the nearby village.\nIn front of you is a house.\nTo your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)dagger.\n ")
    print_pause("Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.")
    while True:
        user_input = input("What would you like to do?\n( Please enter 1 or 2.) \n")
        if user_input == '1':
           house()
           break
        elif user_input == '2':
           cave()
           break
        else:
            print("Sorry, I don't understand.")


# Things that happen when the player fights
def fight():
    print_pause("You do your best...\nbut your dagger is no match for the " + monster +".\nYou have been defeated!\n")
    while True:
        user_input = input("Would you like to play again? (y/n)\n")
        if user_input == 'y':
           field()
           break
        elif user_input == 'n':
            print_pause("Thanks for playing! See you next time")
        else:
            print_pause("Sorry, I don't understand.")
# Things that happen to the player goes in the cave
def cave():
    print_pause("You peer cautiously into the cave.\nIt turns out to be only a very small cave.\nYour eye catches a glint of metal behind a rock.""")
    print_pause("""You have found the magical Sword of Ogoroth!\nYou discard your silly old dagger and take the sword with you.\nYou walk back out to the field.\n""")
    print_pause ("""Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.\nWhat would you like to do?""")
    while True:
        user_input = input("(Please enter 1 or 2.)\n")
        if user_input == '1':
           house()
           break
        elif user_input == '2':
           print_pause("""You peer cautiously into the cave.\nYou've been here before, and gotten all the good stuff. It's just an empty cave now.\nYou walk back out to the field.""")
           print_pause("""Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.\nWhat would you like to do?""")
           break
        else:
           print_pause("Sorry, I don't understand.")
    while True:
        user_input = input("(Please enter 1 or 2.)\n")
        if user_input == '1':
           house()
           break
        elif user_input == '2':
           cave()
           break
        else:
           print_pause("Sorry, I don't understand.")


# Things that happen to the player in the house
def house():
    print_pause ("you approach the door of the house.\nYou are about to knock when the door opens and out steps a " + monster +".")
    print_pause ("Eep! This is the " + monster +" house!")
    print_pause("The " + monster + " attacks you!\nYou feel a bit under prepared for this, what with only having a tiny dagger.")
    while True:
        user_input = input("Would you like to (1) fight or (2) run away?\n")
        if user_input == '1':
            fight()
            break
        elif user_input == '2':
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
            print_pause("""Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.\nWhat would you like to do?""")
            break
        else:
            print_pause("Sorry, I don't understand.")
    while True:
        user_input = input("(Please enter 1 or 2.)\n")
        if user_input == '1':
            house()
            break
        elif user_input  == '2':
            cave()
            break
        else:
            print_pause("Sorry, I don't understand.")
field()
