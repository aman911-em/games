import random
Target=random.randint(1,100)
while True:
    userChoice=input("Guess the the number or quit(Q):")
    if (userChoice.lower()=="q"):
        break

    userChoice = int(userChoice)

    if ((userChoice)==Target):
        print("Success:Guess correct!!")
        break
    elif(userChoice>Target):
        print("your number is too big choice smaller..")
    else:
        print("your number is too small choice bigger..")
print("-----GAME OVER-----")


