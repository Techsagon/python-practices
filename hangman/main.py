import random

words = [
    "apple", "banana", "cherry", "grape", "orange", "melon", "peach", "pear", "plum", "kiwi",
    "zebra", "tiger", "lion", "elephant", "giraffe", "monkey", "panda", "kangaroo", "koala", "leopard",
    "river", "mountain", "forest", "desert", "valley", "island", "ocean", "beach", "volcano", "glacier",
    "school", "teacher", "student", "pencil", "eraser", "notebook", "backpack", "lesson", "classroom", "exam",
    "python", "program", "function", "variable", "loop", "string", "integer", "boolean", "dictionary", "list",
    "robot", "spaceship", "galaxy", "planet", "asteroid", "rocket", "comet", "satellite", "universe", "nebula",
    "castle", "dragon", "wizard", "sword", "knight", "magic", "kingdom", "princess", "quest", "treasure",
    "winter", "spring", "summer", "autumn", "weather", "cloud", "thunder", "lightning", "rainbow", "breeze",
    "guitar", "piano", "drums", "violin", "trumpet", "flute", "singer", "band", "melody", "rhythm",
    "happy", "sad", "angry", "excited", "scared", "bored", "curious", "nervous", "lonely", "proud"
]
hangman = [
    # Full hangman (head, body, both arms and both legs)
    '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    ''',

    # Missing one leg
    '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''',

    # Missing both legs
    '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''',

    # Missing right arm
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',

    # Missing left arm
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',

    # Only head
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',

    # Empty gallows
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    '''
]

# Choosing a word and initializing variables
word = random.choice(words)
lives = 6
letters = []
guessed_letters = []
for i in range(len(word)):
    letters.append(word[i])
    guessed_letters.append('-')

while True:
    print(f"-----------------------------[ Lives: {lives} ]-----------------------------")
    print(hangman[lives])
    temp_word = ""
    for w in guessed_letters:
        temp_word += w
    print("The Word: ",temp_word)
    input_letter = input("\nEnter a letter: ").lower()

    counter = 0
    guessed = False
    for j in letters:
        if j == input_letter:
            guessed_letters[counter] = j
            guessed = True
        counter += 1
    if guessed == False:
        lives -= 1

    # do while condition
    if guessed_letters == letters:
        print(f"You guessed it! The word is: {word}")
        break
    if lives <= 0:
        print(f"-----------------------------[ Lives: {lives} ]-----------------------------")
        print(hangman[lives])
        print(f"You lost! The word was: {word}")
        break

input("\nPress Enter to exit...")
