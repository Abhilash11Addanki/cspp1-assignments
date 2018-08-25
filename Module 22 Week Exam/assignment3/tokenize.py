'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    '''tokenize function.'''
    dict_ = {}
    list_1 = []
    list_ = string.split(";")
    for i in list_:
        list_1.append(i.split(" "))
    for char in list_1:
        dict_[char] = list_1.count(char)
    return dict_
def main():
    '''main function.'''
    n_1 = int(input())
    res_str = ""
    for str_1 in range(n_1):
        str_1 = input()
        res_str += str_1
    print(tokenize(res_str))
if __name__ == '__main__':
    main()
