#Guess a Number AI
#You think of a number, computer tries to get it

#9-25-2017

#Olivia S.

#config
low = 1
high = 100

# helper functions
def show_start_screen():
    print("  ▄████  █    ██ ▓█████   ██████   ██████     ▄▄▄          ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███      ▄▄▄       ██▓")
    print(" ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▒████▄        ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒   ▒████▄    ▓██▒")
    print("▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒██  ▀█▄     ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒   ▒██  ▀█▄  ▒██▒")
    print("░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░██▄▄▄▄██    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄     ░██▄▄▄▄██ ░██░")
    print("░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒    ▓█   ▓██▒   ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒    ▓█   ▓██▒░██░")
    print(" ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░    ▒▒   ▓▒█░░▓  ")
    print("  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░     ▒   ▒▒ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░     ▒   ▒▒ ░ ▒ ░")
    print("░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░       ░   ▒         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░      ░   ▒    ▒ ░")
    print("      ░    ░        ░  ░      ░        ░           ░  ░            ░    ░            ░    ░         ░  ░   ░              ░  ░ ░  ")
    print("                                                                                               ░                                  ")
    
def show_credits():
    print("                                                                  *                                    )                     (     ")  
    print("  *   )   )        (                         (  (               (  `         (            (         ( /(  (                  )\ )  ")  
    print("` )  /(( /((       )\ )      )    )     (    )\))(   '   )      )\))(     )  )\ )  (    ( )\ (      )\()) )\(   )  (     )  (()/(  ")
    print(" ( )(_))\())\ (   (()/(   ( /(   (     ))\  ((_)()\ ) ( /( (   ((_)()\ ( /( (()/( ))\   )((_))\ )  ((_)\ ((_)\ /(( )\ ( /(   /(_)) ")
    print("(_(_()|(_)((_))\   /(_))_ )(_))  )\  '/((_) _(())\_)())(_)))\  (_()((_))(_)) ((_))((_) ((_)_(()/(    ((_) _((_|_))((_))(_)) (_))   ")
    print("|_   _| |(_|_|(_) (_)) __((_)_ _((_))(_))   \ \((_)/ ((_)_((_) |  \/  ((_)_  _| (_))    | _ ))(_))  / _ \| |(_))((_|_|(_)_  / __|  ")
    print("  | | | ' \| (_-<   | (_ / _` | '  \() -_)   \ \/\/ // _` (_-< | |\/| / _` / _` / -_)   | _ \ || | | (_) | || \ V /| / _` | \__ \  ")
    print("  |_| |_||_|_/__/    \___\__,_|_|_|_|\___|    \_/\_/ \__,_/__/ |_|  |_\__,_\__,_\___|   |___/\_, |  \___/|_||_|\_/ |_\__,_| |___/  ")
    print("                                                                                             |__/                                  ")                                                                                                     


    
def get_guess(current_low, current_high):
    guess = (current_high + current_low) // 2
    print(guess)
    return guess

def pick_number():
    print("Think of a number between " + str(low) + " and " + str(high) + ".")
    input("Press enter to continue")
                                   
def check_guess(guess):
    print("Was my guess too high, too low, or correct?")
    answer = input()
    if answer.lower() == "too high" or answer.lower() == "l":
        return 1
    elif answer.lower() == "too low" or answer.lower() == "h":
        return -1
    elif answer.lower() == "correct" or answer.lower() == "c":
        return 0
    else:
        print("I don't understand. Please enter too high, too low, or correct.")

def show_result():
    print("Haha! I got it!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
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
            current_low = guess
        elif check == 1:
            current_high = guess
           
    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



