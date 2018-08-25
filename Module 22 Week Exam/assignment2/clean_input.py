'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    '''function to clean string'''
    res_str = ""
    for char in string:
        if char in "!@#$%^&*()_+":
            res_str += ""
        else:
            res_str += char
    res_str = res_str.replace(" ", "")
    return res_str
def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
