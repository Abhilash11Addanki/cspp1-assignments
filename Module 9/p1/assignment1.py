'''
Exercise: Assignment-1
First, implement the function isWordGuessed that takes in two parameters -
a string, secret_word, and a list of letters, letters_guessed. This function
returns a boolean - True if secret_word has been guessed (ie, all the letters of
secret_word are in letters_guessed) and False otherwise.
'''


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    cnt = 0
    for i in letters_guessed:
        if i in secret_word:
            cnt += 1
    if cnt == len(secret_word):
        return True
    return False
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list_1 = []
    for j in range(1, len(data)):
        list_1.append(data[j][0])
    print(is_word_guessed(secret_word, list_1))

if __name__ == "__main__":
    main()
