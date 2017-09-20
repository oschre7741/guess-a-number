import random

#config
low = 1
high = 100
limit = 10

#helper functions
def show_start_screen():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~ Guess A Number! ~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

def show_credits():
    print("This game was made by Olivia Schreiner")

def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
     print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

     return random.randint(low,high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("Congration you done it")
    else:
        print("Get gud scrub. The number I was thinking of is " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would like to play again? (y/n)")

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            return False
        else:
            print("I don't understand, please answer 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)
    
        tries += 1

        show_result(guess, rand)

#game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
    

