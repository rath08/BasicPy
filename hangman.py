import random


def hangman():
    list_of_words = [
        "dinner",
        "hangman",
        "diesel",
        "forget",
        "agenda",
        "berlin",
        "cinema",
        "depend",
        "escape",
        "factor",
        "family",
        "golden",
        "hockey",
        "insect",
        "kidney",
        "legacy",
        "margin",
        "maggie",
        "mobile",
        "nature",
        "normal",
        "offset",
        "outing",
        "parcel",
        "parity",
        "potato",
        "racial",
        "reader",
        "reduce",
        "saving",
        "screen",
        "access",
        "adhere",
        "attain",
        "branch",
        "bronze",
        " dragon",
        "button",
        "bright",
        "buffer",
    ]
    word = random.choice(list_of_words)
    turns = 10

    guess_made = ""

    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

    while len(word) > 0:
        main_word = ""
        missed = 0
        for letter in word:
            if letter in guess_made:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "
        if main_word == word:

            print(main_word)
            print("\nyou won!!")
            break
        print("guess the word ", main_word)
        guess = input()
        if guess in valid_entry:
            guess_made = guess_made + guess
        else:
            print("enter valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("----------------")
            if turns == 8:
                print("8 turns left")
                print("----------------")
                print("       O        ")
            if turns == 7:
                print("7 turns left")
                print("----------------")
                print("       O        ")
                print("       |        ")

            if turns == 6:
                print("6 turns left")
                print("----------------")
                print("       O        ")
                print("       |        ")

            if turns == 5:
                print("5 turns left")
                print("----------------")
                print("       O        ")
                print("       |        ")
                print("      /         ")

            if turns == 4:
                print("4 turns left")
                print("----------------")
                print("       O        ")
                print("       |        ")
                print("      / \       ")

            if turns == 3:
                print("3 turns left")
                print("----------------")
                print("      \O        ")
                print("       |        ")
                print("      / \       ")

            if turns == 2:
                print("2 turns left")
                print("----------------")
                print("      \O/       ")
                print("       |        ")
                print("      / \       ")

            if turns == 1:
                print("1 turns left")
                print("breaths are counting")
                print("----------------")
                print("      \O/ _|    ")
                print("       |        ")
                print("      / \       ")

            if turns == 0:
                print("you lost")
                print("you let a good man die")
                print("----------------")
                print("       |        ")
                print("       O        ")
                print("     / | \       ")
                print("      | |       ")


name = input("enter the name : ")
print("welcome", name, "!!\n")
print("try to guess the word in less than 10 attempts\n")
hangman()
