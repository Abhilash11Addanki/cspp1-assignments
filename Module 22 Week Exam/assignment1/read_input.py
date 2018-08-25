'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    n_1 = int(input())
    res_str = ""
    for i in range(n_1):
        read_input = input()
        res_str += read_input
    print(res_str)

if __name__ == '__main__':
    main()
