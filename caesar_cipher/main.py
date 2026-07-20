from itertools import islice, cycle

print('''
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓█▓▒░      ░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
''')

lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(word, key):
    crypted_word = ""
    for letter in word:
        if letter in lower_alphabet:
            alphabet_cycle = islice(cycle(lower_alphabet), lower_alphabet.index(letter), None)
            crypted_letter = ''
            for i in range(key+1):
                crypted_letter = next(alphabet_cycle)
            crypted_word += crypted_letter
        elif letter in upper_alphabet:
            alphabet_cycle = islice(cycle(upper_alphabet), upper_alphabet.index(letter), None)
            crypted_letter = ''
            for i in range(key + 1):
                crypted_letter = next(alphabet_cycle)
            crypted_word += crypted_letter
        else:
            crypted_word += letter
    return crypted_word

def decrypt(word, key):
    lower_alphabet.reverse()
    upper_alphabet.reverse()
    decrypted_word = ""
    for letter in word:
        if letter in lower_alphabet:
            alphabet_cycle = islice(cycle(lower_alphabet), lower_alphabet.index(letter), None)
            crypted_letter = ''
            for i in range(key+1):
                crypted_letter = next(alphabet_cycle)
            decrypted_word += crypted_letter
        elif letter in upper_alphabet:
            alphabet_cycle = islice(cycle(upper_alphabet), upper_alphabet.index(letter), None)
            crypted_letter = ''
            for i in range(key + 1):
                crypted_letter = next(alphabet_cycle)
            decrypted_word += crypted_letter
        else:
            decrypted_word += letter
    lower_alphabet.reverse()
    upper_alphabet.reverse()
    return decrypted_word

while True:
    print("What would you like to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    todo = int(input("\nEnter your choice (1, 2): "))

    if todo == 1:
        word = input("\nEnter the word to Encrypt: ")
        key = int(input("Enter the key: "))
        print("\nThe encrypted word is:", encrypt(word, key))
    elif todo == 2:
        word = input("\nEnter the word to Decrypt: ")
        key = int(input("Enter the key: "))
        print("\nThe decrypted word is:", decrypt(word, key))
    else:
        print("\nInvalid choice, Try again.")

    try_again = input("\nWould you like to try again (y/n)?")
    if try_again == "n" or try_again == "N" or try_again == "No" or try_again == "no" or try_again == "NO" or try_again == "nO":
        break
    else:
        print("\n######################################################################################################\n")

input("\nPress enter to exit...")