'''
Exercise : Assignment-1
implement the function get_available_letters that takes in one parameter -
a list of letters, letters_guessed. This function returns a string
that is comprised of lowercase English letters - all lowercase English letters
that are not in letters_guessed
'''
import string
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_1 = string.ascii_lowercase
    list_1 = list(str_1)
    list_2 = []
    list_3 = []
    for i in range(len(list_1)):
        list_2 += [ord(str_1[i])]
    dic_1 = dict(zip(list_2, list_1))
    str_2 = ''.join(letters_guessed)
    for j in range(len(letters_guessed)):
        list_3 += [ord(str_2[j])]
    dic_2 = dict(zip(list_3, letters_guessed))
    for i in dic_2.keys():
        if i in dic_1.keys():
            del dic_1[i]
    list_4 = []
    for i in dic_1.values():
        list_4.append(i)
    return ''.join(list_4)
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
