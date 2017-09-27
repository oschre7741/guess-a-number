import random

# config
low = 1
high = 1000


# helper functions
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
                                                                                                                                            
    
def get_guess(current_low, current_high):
    a = (current_high + current_low) // 2
    return a

def pick_number():
    print("Think of a number between " + str(low) + " and " + str(high) + ".")

def check_guess(guess):
    print("Was my guess too high, too low, or correct?")
    check = input()
    
    if check == "too high":
        return 1
    elif check == "too low":
        return -1
    else check == "correct":
        return 0

def show_result():
    if guess.lower == "correct":
        print("Haha! I got it!")
    else:
        print("Dang it. Maybe next time.")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision.lower == 'y' or decision.lower == 'yes':
            return True
        elif decision.lower == 'n' or decision.lower == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            guess = current_low
        elif check == 1:
            guess = current_high
           

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



