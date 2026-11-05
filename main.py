# click command 0 for adrian to open commit window, then select changes and click COMMIT AND PUSH to upload new files to git.

# imports
from time import sleep



# functions
def prints(x):
    print("\n" * x)

prints(10)

settings = False
int = 0
spk = 0
sgt = 0
dex = 0
aim = 0

print("Welcome to PY.T.R.P.G")
while True:
    print("1: boot")
    print("2: persona")
    print("3: exit")
    ans = input("access: ")
    if ans == "1" and settings == True:
        prints(10)
        print("insert actual game here")

    elif ans == "2":
        while True:
            prints(20)
            database = input("please enter database ")
            if database.strip() == "homo sapien":
                int = input("int: ")
                aim = input("aim: ")
                dex = input("dex: ")
        
            else:
                print("invalid database")

            if int+aim+dex+sgt+spk ==30:
                break
            else:
                print("database must equal 30")
            settings = True


    elif ans == "3":
        break
    else:
        print("invalid")

