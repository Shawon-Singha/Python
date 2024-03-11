from random import randint

for x in range(1,6):
    guessNumber = int(input("Enter the value bewteen 1 to 5: "))

    randomNumber =randint(1,5)

    if guessNumber == randomNumber:
        print("You win")

    else:
        print("You Loss")
        print("Random number was:",randomNumber)
