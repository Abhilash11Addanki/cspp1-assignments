'''GCD using iteration'''

def gcd_iter(a_1, b_1):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    rem_num = a_1%b_1
    while b_1 != 0:
        if a_1%b_1 == 0:
            return b_1
        rem_num = a_1%b_1
        a_1 = b_1
        b_1 = rem_num

def main():
    '''Main function.'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
