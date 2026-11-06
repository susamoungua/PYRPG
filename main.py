# click command 0 for adrian to open commit window, then select changes and click COMMIT AND PUSH to upload new files to git.

# imports
import sleep

# functions
def prints(x):
    print("\n" * x)

prints(10)

# booleans
settings = False
inter = 0
spk = 0
sgt = 0
dex = 0
aim = 0


print("Welcome to PY.T.R.P.G")
while True:
    # terminal
    print("1: boot")
    print("2: persona")
    print("3: exit")
    ans = input("access: ")
    if ans == "1" and settings == True:
        prints(20)
        # refresh screen and play game
        # intro monolouge
        print("you are a test dummy")
        time.sleep(1)
        print("the people who created you do not care")
        time.sleep(1)
        print("you must control this person")
        time.sleep(2)
        print()
        time.sleep(1)
        print("and escape this space station")
        time.sleep(1)
        print("once and for all")
        time.sleep(1)
        prints(30)
        print("PYTRPG")
        print("a terminal based rpg made by humans")
    elif ans == "2":
        # charatcher creation
        while True:
            database = input("please enter database ")
            if database.strip() == "homo sapien":
                inter = input("int: ")
                aim = input("aim: ")
                dex = input("dex: ")
                prints(20)
        
            else:
                print("invalid database")

            if int(inter) + int(aim) + int(dex) == 30:
                break
            else:
                print("database must equal 30")
            settings = True


    elif ans == "3":
        break
    else:
        print("invalid")

