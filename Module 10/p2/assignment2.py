'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from ps3_hangman import isWordGuessed, getGuessedWord, getAvailableLetters
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    word_list = line.split()
    print("  ", len(word_list), "words loaded.")
    return word_list

def choose_word(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
word_list = load_words()

def hangman_func(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses_cnt = 10
    letters_guessed = []
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")
    while guesses_cnt > 0 and (not isWordGuessed(secret_word, letters_guessed)):
        print("You have", guesses_cnt, "guesses left.")
        print("Available letters:", getAvailableLetters(letters_guessed))
        guess = str.lower(input("Please guess a letter:"))
        guessed_word = getGuessedWord(secret_word, letters_guessed)
        letters_guessed.append(guess)
        if guess in guessed_word:
            guessed_word = getGuessedWord(secret_word, letters_guessed)
            print("Oops! You've already guessed that letter:", guessed_word)
            print("\n------------")
        elif guess in secret_word:
            guessed_word = getGuessedWord(secret_word, letters_guessed)
            print("Good guess", guessed_word)
            print("\n------------")
        elif guess not in secret_word:
            guessed_word = getGuessedWord(secret_word, letters_guessed)
            print("Oops! That letter is not in my word:", guessed_word)
            print("\n------------")
            guesses_cnt -= 1
    if isWordGuessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("\n------------")
    else:
        print("Sorry, you ran out of guesses. The word was " + secret_word + "\n------------")

def main():
    '''
    Main function for the given program

    When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
    secret_word = choose_word(word_list).lower()
    hangman_func(secret_word)


if __name__ == "__main__":
    main()
