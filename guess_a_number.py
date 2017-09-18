import random

#config
low = 1
high = 100
limit = 10

#helper functions
def get_guess():
    while True:
        g = input("Take a guess:")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number.")

def play_again():
    while True:
        decision = input("Would like to play again? (y/n)")

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            return False

        print("I don't understand, please answer 'y' or 'n'.")

again = True

while again:   
    #start game
    rand = random.randrange(low, high)
    print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

    guess = -1
    tries = 0

    #play the game
    while guess != rand and tries < limit:
        guess = get_guess()
   
        if guess < rand:
            print("You guessed too low.")
        elif guess > rand:
            print("You guessed too high.")
    
        tries += 1

#end the game
    if guess == rand:
        print("You win!")
    else:
        print("You're dumb. The number I was thinking of is " + str(rand) + ".")

    again = play_again()

    print("Goodbye.")
    

