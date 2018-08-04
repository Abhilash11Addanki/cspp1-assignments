'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    int_input = int(input())
    int_input1 = int_input
    rem = 0
    res = 1
    if int_input < 0:
        int_input = abs(int_input)
    elif int_input == 0:
        res *= int_input
    while int_input > 0:
        rem = int_input%10
        res *= rem
        int_input //= 10
    if int_input1 >= 0:
        print(res)
    else:
        print(-res)
if __name__ == "__main__":
    main()
