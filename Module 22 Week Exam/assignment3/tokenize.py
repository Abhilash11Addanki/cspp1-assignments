'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    '''tokenize function.'''
    dict_ = {}
    list_ = string.split(" ")
    for char in list_:
        dict_[char] = list_.count(char)
    return dict_
def main():
    '''main function.'''
    n_1 = int(input())
    for i in range(n_1):
        i = input()
    print(tokenize(i))
if __name__ == '__main__':
    main()
