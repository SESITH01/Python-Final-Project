import csv
import random
# Creates hangman display depending on guess number, chosen by comma
Hangman_Display = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']


def UserInput(letters_guessed):
    # Returns letter player has guessed and ensures that it is a letter not a word.
    while True:
        guess = input("Guess a letter (or 'quit' to quit): ")
        guess = guess.lower()
        # Offers a way to quit
        if guess == "quit":
            quit()
        # Secret passcode that reveals the word
        elif guess == "secret":
            print(x)
        # Makes sure the guess is one letter
        elif len(guess) != 1:
            print("Please enter a single letter")
        # Makes sure it's a letter that hasn't already been guessed
        elif guess in letters_guessed:
            print("Please enter a letter that hasn't been chosen yet")
        # Makes sure that the guess is a letter and not a number or symbol
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter, not a number")
        # Returns guess if passes all statements
        else:
            return guess

# Function that prints the hangman images / stores wrong guesses and right guesses


def Display(wrong, right, x):
    # prints the corresponding hangman display depending on incorrect guesses
    print(Hangman_Display[len(wrong)])
    print()
    # Stores guesses for the reader to see if they were incorrect
    print("Wrong Guesses: ", end='')
    for letter in wrong:
        print(letter, end='')
    print()

    # Creates blank spaces the length of the word
    blanks = '_' * len(x)

    # Finds if the guess is in the length of the word
    for i in range(len(x)):
        if x[i] in right:
            blanks = blanks[:i] + x[i] + blanks[i+1:]
    # Replaces blank with letter
    for letter in blanks:
        print(letter, end='')
    print()


if __name__ == "__main__":
    # Opens csv and converts it into a list
    word_to_guess = open("word_or_phrase.csv", "r")
    reader = csv.DictReader(word_to_guess, delimiter=',')
    words = []
    i = 0
    for row in reader:
        Words = [row['Word']]
        words.append(Words)
        i += 1
    word_to_guess.close()
    # Keeps the display printing as long as the game is not over
    while True:
        GameOver = False
        print("H A N G M A N\n"
              "______________")
        # Empty list for right and wrong letters
        right = []
        wrong = []
        # Makes the words in the csv file lowercase
        x = ''.join(random.choice(words)).lower()
        # List of letters guessed
        letters_guessed = []
        while True:
            # Stores guess in right or wrong depending on if the letter matches
            Display(wrong, right, x)
            new_guess = UserInput(letters_guessed)
            if new_guess in x:
                right += new_guess
                letters_guessed += new_guess
            else:
                wrong += new_guess
                letters_guessed += new_guess
                # Decides if the game is over
            GameOver = True
            for character in x:
                if character not in right:
                    GameOver = False
                    break
            # Ends the game when the hang man is completely hung
            if len(wrong) == len(Hangman_Display)-1:
                GameOver = True
            # Allows the user to see the word at the end of the game regardless of win
            if GameOver:
                print("\nThe Game is over\n\nThe word was "+x+"")
                # Display Total Points
                print("\nTotal Points: ", len(wrong)*0.5 + len(right))
            # Allows the player to play another game if they input anything other than "Quit"
                break
        new_game = input("\nDo you want to play again? ('Quit' to quit)")
        if new_game == "Quit":
            break

