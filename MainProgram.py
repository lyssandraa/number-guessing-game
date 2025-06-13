import random

def welcomeMessage():
    message = "\nWelcome to the Awesome Number Guessing Game!\n\
        \nThe rules are simple: guess the number the program picked from the range you provided.\
        \nYou get to decide the difficulty by choosing how many attempts you are allowed.\n"
    print(message)

def userInput():
    lowerBound = int(input("Enter first number: "))
    upperBound = int(input("Enter second number: "))
    attempts = int(input("How many attempts would you like?\nEnter here: "))
    return lowerBound, upperBound, attempts

def getRandomNumber(lowerBound, upperBound):
    secretNumber = random.randint(lowerBound, upperBound)
    return secretNumber

def userGuess(lowerBound, upperBound):
    while True:
        guess = int(input("\nEnter guess: "))
        if lowerBound <= guess <= upperBound:
            return guess
        else:
            print("Invalid input! Please enter a number within the specified range.")

def checkGuess(guess, secretNumber):
        if guess == secretNumber:
            return "Correct!"
        elif guess > secretNumber:
            return "Too high!"
        else:
            return "Too low!"

def attemptsTracker(lowerBound, upperBound, attempts, secretNumber):
    print(f"\nThanks for the input.\nYou are now to guess the secret number between {lowerBound} and {upperBound} in {attempts} tries.")
    attemptsCounter = 0
    won = False

    while attemptsCounter < attempts:
        attemptsCounter += 1
        guess = userGuess(lowerBound, upperBound)
        result = checkGuess(guess, secretNumber)
        
        if result == "Correct!":
            print(f"Congratulations! You outsmarted the machine in {attemptsCounter} attempt(s).")
            won = True
            break
        else: 
            print(f"{result}")
            if attemptsCounter < attempts:
                print(f"You have {attempts - attemptsCounter} attempt(s) remaining.\n")
    
    if not won:
        print(f"There are no more available attempts.\nThe correct number was {secretNumber}.")

def confirmPlay():
    confirmation = input("Would you like to play?\nPlease enter Yes or No: ").strip().lower()
    if confirmation in ("yes", "y"):
        print("Thanks for confirming. Good luck outsmarting the machine!\n" \
        "The game starts now!\n")
        lowerBound, upperBound, attempts = userInput()
        secretNumber = getRandomNumber(lowerBound, upperBound)
        attemptsTracker(lowerBound, upperBound, attempts, secretNumber)
    elif confirmation in ("no", "n"):
        print("Thanks for stopping by!")
    else: 
        print("Invalid input. Exiting game!")

def main():
    welcomeMessage()
    confirmPlay()
    

main()