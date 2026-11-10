# click command 0 for adrian to open commit window, then select changes and click COMMIT AND PUSH to upload new files to git.

# imports
import time
import random
# functions
def prints(x):
    print("\n" * x)

def room():
    # a room to go through! woohoo!
    seed = random.randint(1,2)
    if seed == 1:
        doors = 2
        chest = 1
    elif seed == 2:
        doors = 3
        chest = 3
    else:
        print("invalid")
    prints(15)
    print("a room has " + str(doors) + " doors, with " + str(chest) + " chests.")
    ans = input("> ")
    for i in range(doors):
        if ans == str("d" + str(i+1)):
            print("you went through a door")
            # go through door
        elif ans == str("c" + str(i+1)):
            print("you went through a chest")
            # insert chest function here
        
prints(10)

# booleans
settings = False
inter = 0
spk = 0
sgt = 0
dex = 0
aim = 0

# intro
while True:
    # boot screen
    print("1: boot")
    print("2: persona")
    print("3: exit")
    ans = input("> ")
    if ans == "1" and settings == True:
        prints(20)
        # refresh screen
        # intro
        print("your eyes were destroyed.")
        print('communicate through a terminal.')
        time.sleep(3)
        prints(15)
        print("P.Y.T.R.P.G")
        print("a terminal based rougelike")
        print("click enter to continue")
        input()
        break
    elif ans == "2":
        # persona creation
        while True:
            database = input("please enter database ")
            if database.strip() == "homo sapien":
                inter = input("int: ")
                aim = input("aim: ")
                dex = input("dex: ")
                prints(15)
        
            else:
                prints(15)
                print("invalid database")
            if int(inter) + int(aim) + int(dex) == 30:
                settings = True
                break
            else:
                print("database must equal 30")


    elif ans == "3":
        break
    else:
        prints(15)
        print("invalid")


# actual game
print("actual game here")
while True:
    ans = input("press enter to continue")
    if ans == "q":
        break
    room()
