#Test to combine games




print("Would you like to play Guess A Number, or Guess A Number AI?")
if input() == "Guess A Number":
    import random
    import math

    #config
    low_human = 1
    high_human = 100
    limit_human = math.ceil(math.log(high_human - low_human + 1 ,2))

    #helper functions
    def show_start_screen_human():
        print("   ______                        ___       _   __                __              __")
        print("  / ____/_  _____  __________   /   |     / | / /_  ______ ___  / /_  ___  _____/ /")
        print(" / / __/ / / / _ \/ ___/ ___/  / /| |    /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/ / ")
        print("/ /_/ / /_/ /  __(__  |__  )  / ___ |   / /|  / /_/ / / / / / / /_/ /  __/ /  /_/  ")
        print("\____/\__,_/\___/____/____/  /_/  |_|  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/  (_)   ")
  
    def show_credits_human():
        print("                                                                                             )                           ")
        print("  *   )   )                                                               (             )        ( /(  (                 ") 
        print("` )  /(( /((       (  (     )    )     (    (  (      )         )      )  )\ )  (    ( /( (      )\()) )\(   )  (     )  ") 
        print(" ( )(_))\())\ (    )\))( ( /(   (     ))\   )\))(  ( /( (      (    ( /( (()/( ))\   )\()))\ )  ((_)\ ((_)\ /(( )\ ( /(  ")
        print("(_(_()|(_)((_))\  ((_))\ )(_))  )\  '/((_) ((_)()\ )(_)))\     )\  ')(_)) ((_))((_) ((_)\(()/(    ((_) _((_|_))((_))(_)) ")
        print("|_   _| |(_|_|(_)  (()(_|(_)_ _((_))(_))   _(()((_|(_)_((_)  _((_))((_)_  _| (_))   | |(_))(_))  / _ \| |(_))((_|_|(_)_  ")
        print("  | | | ' \| (_-< / _` |/ _` | '  \() -_)  \ V  V / _` (_-< | '  \() _` / _` / -_)  | '_ \ || | | (_) | || \ V /| / _` | ")
        print("  |_| |_||_|_/__/ \__, |\__,_|_|_|_|\___|   \_/\_/\__,_/__/ |_|_|_|\__,_\__,_\___|  |_.__/\_, |  \___/|_||_|\_/ |_\__,_| ")
        print("                  |___/                                                                   |__/                           ")
  
    def get_guess_human():
        while True:
            guess_human = input("Guess a number: ")

        if guess_human.isnumeric():
            guess_human = int(guess_human)
            return guess_human
        else:
            print("You must enter a number.")

    def pick_number_human():
        print("I'm thinking of a number from " + str(low_human) + " to " + str(high_human) + ".")
        print("You have " + str(limit_human) + " tries to guess.");

        return random.randint(low_human,high_human)

    def check_guess_human(guess_human, rand):
        if guess_human < rand:
            print("You guessed too low.")
        elif guess_human > rand:
            print("You guessed too high.")

    def show_result_human(guess_human, rand):
        if guess_human == rand:
            print("Congration you done it")
        else:
            print("Get gud scrub. The number I was thinking of is " + str(rand) + ".")

    def play_again_human():
        while True:
            decision_human = input("Would like to play again? (y/n)")

            if decision_human.lower() == "y" or decision_human.lower() == "yes":
                return True
            elif decision_human.lower() == "n" or decision_human.lower() == "no":
                return False
            else:
                print("I don't understand, please answer 'y' or 'n'.")

    def play():
        guess_human = -1
        tries_human = 0

        rand = pick_number_human()
    
        while guess_human != rand and tries_human < limit_human:
            guess_human = get_guess_human()
            check_guess_human(guess_human, rand)
    
            tries_human += 1

        show_result_human(guess_human, rand)

    #game starts running here
    show_start_screen_human()

    playing_human = True

    while playing_human:
        play()
        playing_human = play_again_human()

    show_credits_human()
        
elif input() == "Guess A Number AI":
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
            
    def play_ai():
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

        
