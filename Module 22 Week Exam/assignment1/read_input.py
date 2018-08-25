'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''main function'''
    n_1 = int(input())
    for read_input in range(n_1):
        read_input = input()
        print(read_input)

if __name__ == '__main__':
    main()
