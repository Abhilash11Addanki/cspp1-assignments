'''GCD using recursion.'''
def gcd_recr(a_1, b_1):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    rem_1 = 0
    if a_1%b_1 == 0:
        return b_1
    else:
        rem_1 = a_1%b_1
        a_1 = b_1
        b_1 = rem_1
        return gcd_recr(a_1, b_1)
def main():
    data = input()
    data = data.split()
    print(gcd_recr(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
