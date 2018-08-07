'''This program prints the factorial of a number.'''
def func_factorial(n_1):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if n_1 > 1:
        return n_1*func_factorial(n_1-1)
    return 1
def main():
    '''Main Function.'''
    a_1 = input()
    print("The factorial of", a_1, "is:", func_factorial(int(a_1)))
if __name__ == "__main__":
    main()
