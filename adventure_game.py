import time

x = input("What is your name? ")

print("Welcome to the game, " + str(x))

time.sleep(2)

print("This is a game of bravery, skill, and luck")

y = input("Are you sure you want to continue? ")

if y.lower() != "yes":
    print("How can you be so scared of a game? Haha...")
    quit()

print("Alright then, you put this upon yourself...")

time.sleep(2)

print("game loading...")

time.sleep(2)

answer = input("You are trapped in a cave. You may look to your right(r), left(l), forward(f), or back(b). Which do you choose? ")

if answer == "r":
    bnswer = input("You look to your right and you see a window. Beside it is a hammer. You may use the hammer to break the window. Do you?")
    if bnswer.lower() != "yes":
        quit()
    print("You win the game!")

if answer == "l":
    print("You look to your left and you see a monster. ")
    print("Game over")
    quit()

if answer == "f":
    print("You see an opening to the cave")
    cnswer = input("Do you want to run to the opening, and possibly save your life?")
    if cnswer.lower() == "yes":
        print("You have failed. A monster finds you")
        quit()
    print("You have made the right choice") 
    print("However, you have failed")
    quit()

if answer == "b":
    print("You see a gush of water, and with no time to react, you drown.")
    quit()

time.sleep(3)

#continue the story here using the same tactics as before in the code

print("Part 2 loading...")




