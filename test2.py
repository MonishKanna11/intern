import random
8
def guess_the_number():
    
    random_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Guessing Game!")
    print("I have generated a random number between 1 and 100.")
    

    while guess != random_number:
    
        guess = int(input("Enter your guess: "))
        attempts += 1

        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")

    
    print(f"Congratulations! You've guessed the number {random_number} correctly!")
    print(f"It took you {attempts} attempts to win the game.")

guess_the_number()