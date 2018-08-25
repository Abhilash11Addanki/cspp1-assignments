'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    '''tokenize function.'''
    dict_ = {}
    list_ = string.split(" ")
    return list_
    for char in list_:
    	dict_[char] = list_.count(char)
    return dict_
            
def main():
    '''main function.'''
    n_1 = int(input())
    res_str = ""
    for str1 in range(n_1):
    	str1 = input()
    print(tokenize(res_str))

if __name__ == '__main__':
    main()
