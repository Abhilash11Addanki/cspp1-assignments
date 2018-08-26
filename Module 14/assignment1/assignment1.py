'''Problem 1 - Build the Shift Dictionary and Apply Shift'''
# The Message class contains methods that could be used to apply a
# cipher to a string, either to encrypt or to decrypt a message
# (since for Caesar codes this is the same action).

# In the next two questions, you will fill in the methods of the
# Message class found in ps6.py according to the specifications in the
# docstrings. The methods in the Message class already filled in are:
# __init__(self, text)
# The getter method get_message_text(self)
# The getter method get_valid_words(self), notice that this one
# returns a copy of self.valid_words to prevent someone from mutating the
# original list.

# In this problem, you will fill in two methods:
# Fill in the build_shift_dict(self, shift) method of the Message class.
# Be sure that your dictionary includes both lower and upper case
# letters, but that the shifted character for a lower case letter and its
# uppercase version are lower and upper case instances of the
# same letter. What this means is that if the original letter is "a" and
# its shifted value is "c", the letter "A" should shift to the letter "C".

# If you are unfamiliar with the ordering or characters of the English alphabet,
# we will be following the letter ordering displayed by
# string.ascii_lowercase and string.ascii_uppercase:

# >>> import string
# >>> print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
# >>> print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# A reminder from the introduction page - characters such as the space character,
# commas, periods, exclamation points, etc will not be encrypted by this cipher
# Basically, all the characters within string.punctuation, plus the space (' ')
# and all numerical characters (0 - 9) found in string.digits.

# Fill in the apply_shift(self, shift) method of the Message class.
# You may find it easier to use build_shift_dict(self, shift).
# Remember that spaces and punctuation should not be changed by the cipher.

# Helper code
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list

WORDLIST_FILENAME = 'words.txt'
# Helper code End


### Paste your implementation of the Message class here
class Message(object):
    """message"""
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
     #delete this line and replace with your code here
        dic = {}
        import string
        a_1 = list(string.ascii_lowercase)
        b_1 = list(string.ascii_uppercase)
        c_1 = []
        d_1 = []
        l_1 = len(a_1)
        for i in range(l_1):
            if i < (l_1-shift):
                c_1.append(a_1[i+shift])
                d_1.append(b_1[i+shift])
            else:
                for j in range(shift):
                    c_1.append(a_1[j])
                    d_1.append(b_1[j])
                break
        a_1.extend(b_1)
        c_1.extend(d_1)
        dic = dict(zip(a_1, c_1))
        return dic
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dic = self.build_shift_dict(shift)
        s_1 = ""
        for i in self.message_text:
            if i in dic:
                s_1 = s_1+dic[i]
            else:
                s_1 = s_1+i
        return s_1


def main():
    '''
        Function to handle testcases
    '''
    data = Message(input())
    data.get_message_text()
    print(data.apply_shift(int(input())))

if __name__ == "__main__":
    main()
