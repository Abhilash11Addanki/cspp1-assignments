'''Exercise: odd'''
def odd(x_1):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return bool(x_1%2 != 0)
def main():
    '''Main function.'''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
