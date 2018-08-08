'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
'''
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    res_1 = ""
    l_1 = len(secret_word)
    res_1 = ""
    for i in range(l_1):
        cnt_1 = 0
        for j in letters_guessed:
            if j == secret_word[i]:
                cnt_1 = 1
        if cnt_1 == 1:
            res_1 = res_1 + secret_word[i]
        else:
            res_1 = res_1+"_"
    return res_1
def main():
    '''
    Main function for current assignment
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
    print(get_guessed_word(secret_word, list_1))
if __name__ == "__main__":
    main()
