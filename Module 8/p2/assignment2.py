'''Sum of digits using recursion.'''
def sumofdigits(n_1):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_1 == 0:
        return 0
    return n_1%10+sumofdigits(n_1//10)
def main():
    '''Main Function.'''
    a_1 = input()
    print(sumofdigits(int(a_1)))
if __name__ == "__main__":
    main()
