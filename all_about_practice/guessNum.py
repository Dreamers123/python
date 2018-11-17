import random
secretNumber=random.randint(1,20)
print("I am thinking of a number between 1 to 20")

for guessTaken in range(1,7):
    print("Take a guess.")
    guess=int(input())
    if(guess < secretNumber):
        print("Your guesss is little bit low")
    elif(guess > secretNumber):
        print("your guess is little bit high")
    elif(guess == secretNumber):
        print("You succcessfully guessed the number")
        break
    else:
        print("Your turn is over ")
        break