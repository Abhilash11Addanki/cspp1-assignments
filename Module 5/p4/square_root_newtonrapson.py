'''This program evaluates the square root of number using Newton Raphson method'''
def main():
    '''Main function.'''
    num_1 = input()
    epsilon = 0.01
    guess = num_1/2.0
    while abs(guess**2-y) >= epsilon:
        guess = guess-(((guess**2)-y)/(2*guess))
    print(guess)
if __name__ == "__main__":
    main()
