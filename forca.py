##############################################################
#MAIN FUNCTION/MODEL
##############################################################
import random

def play():
    wrongs = 0
    acertou = False
    enforcou = False

    secret_word = get_secret_word("word.txt")
    correctly_letters = print_letters("_", secret_word)
    print(print_correctly_letters(correctly_letters))

    while(not enforcou and not acertou):
        kick = set_kick()
        if(kick in secret_word):
            register_kick(kick, correctly_letters, secret_word)
        else:
            wrongs += 1
            print_forca(wrongs)

        enforcou = (wrongs == 7)
        acertou = "_" not in correctly_letters
        print(correctly_letters)

    print(print_row())
    print(print_result(acertou, secret_word))
    print(print_end_game())
    print(print_row())

##############################################################
# UTILS FUNCTIONS/MODELS
##############################################################
def register_kick(kick, correctly_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (kick == letter):
            correctly_letters[index] = letter
        index += 1

def set_kick():
    kick = input("What Letter? ")
    kick = kick.strip().upper()
    return kick

def get_secret_word(file_name):
    file_name = open(file_name, "r")
    words = []
    for row in file_name:
        row = row.strip()
        words.append(row)

    file_name.close()
    index_number = random.randrange(0, len(words))
    secret_word = words[index_number].upper()
    return secret_word

def print_correctly_letters(letters):
    return letters

def print_letters(str, secret_word):
    return [str for letter in secret_word]

def print_row():
    return "\n***********************************\n"

def print_end_game():
    return "...: THE END GAME - FORCA!!! :..."

def print_header():
    print("***********************************")
    print("*** Welcome - GAME of the Forca ***")
    print("***********************************")

def print_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def print_result(var_result, secret_word):
    if(var_result):
        print("YOU WON. Congratulations!!!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Sorry, YOU LOSE!")
        print("The Word was: {}".format(secret_word))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

#CHECK EXECUTE MAIN CLASS
if(__name__ == "__main__") :
    play()