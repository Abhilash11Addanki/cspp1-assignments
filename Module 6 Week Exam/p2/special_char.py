'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_result = ""
    for letter in str_input:
        if letter in "!@#$%^&*()_+":
            letter = " "
            str_result += letter
        else:
            str_result += letter
    print(str_result)
if __name__ == "__main__":
    main()
