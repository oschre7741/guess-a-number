import random

#config
low = 1
high = 100
limit = 10

#start game
rand = random.randrange(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

#play the game
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    
    tries += 1

#tell player outcome
if guess == rand:
    print("You win!")
else:
    print("You're dumb. The number I was thinking of is " + str(rand) + ".")
    

