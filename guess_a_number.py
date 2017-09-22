import random
import math

#config
low = 1
high = 100
limit = math.ceil(math.log(high - low + 1 ,2))

#helper functions
def show_start_screen():
    print("   ______                        ___       _   __                __              __")
    print("  / ____/_  _____  __________   /   |     / | / /_  ______ ___  / /_  ___  _____/ /")
    print(" / / __/ / / / _ \/ ___/ ___/  / /| |    /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/ / ")
    print("/ /_/ / /_/ /  __(__  |__  )  / ___ |   / /|  / /_/ / / / / / / /_/ /  __/ /  /_/  ")
    print("\____/\__,_/\___/____/____/  /_/  |_|  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/  (_)   ")
                                                                                   


def show_credits():
  
    print("                                                                                             )                           ")
    print("  *   )   )                                                               (             )        ( /(  (                 ") 
    print("` )  /(( /((       (  (     )    )     (    (  (      )         )      )  )\ )  (    ( /( (      )\()) )\(   )  (     )  ") 
    print(" ( )(_))\())\ (    )\))( ( /(   (     ))\   )\))(  ( /( (      (    ( /( (()/( ))\   )\()))\ )  ((_)\ ((_)\ /(( )\ ( /(  ")
    print("(_(_()|(_)((_))\  ((_))\ )(_))  )\  '/((_) ((_)()\ )(_)))\     )\  ')(_)) ((_))((_) ((_)\(()/(    ((_) _((_|_))((_))(_)) ")
    print("|_   _| |(_|_|(_)  (()(_|(_)_ _((_))(_))   _(()((_|(_)_((_)  _((_))((_)_  _| (_))   | |(_))(_))  / _ \| |(_))((_|_|(_)_  ")
    print("  | | | ' \| (_-< / _` |/ _` | '  \() -_)  \ V  V / _` (_-< | '  \() _` / _` / -_)  | '_ \ || | | (_) | || \ V /| / _` | ")
    print("  |_| |_||_|_/__/ \__, |\__,_|_|_|_|\___|   \_/\_/\__,_/__/ |_|_|_|\__,_\__,_\___|  |_.__/\_, |  \___/|_||_|\_/ |_\__,_| ")
    print("                  |___/                                                                   |__/                           ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
     print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".")
     print("You have " + str(limit) + " tries to guess.");

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

        if decision.lower() == "y" or decision.lower() == "yes":
            return True
        elif decision.lower() == "n" or decision.lower() == "no":
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
    

