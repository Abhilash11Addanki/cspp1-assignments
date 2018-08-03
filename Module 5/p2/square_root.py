'''This program evaluates the square root of a number.'''
def main():
    '''Main function.'''
    s = int(input())
    epsilon = 0.01
    step = 0.1
    guess = 0
    while abs(guess**2-s) >= epsilon:
        guess += step
    if abs(guess**2-s) >= epsilon:
        print("Failed on square root of", s)
    else:
        print(guess)
if __name__ == "__main__":
    main()
