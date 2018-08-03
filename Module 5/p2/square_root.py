'''This program evaluates the square root of a number.'''
def main():
    '''Main function.'''
    num_1 = int(input())
    epsilon = 0.01
    step = 0.1
    guess = 0
    while abs(guess**2-num_1) >= epsilon:
        guess += step
    if abs(guess**2-num_1) >= epsilon:
        print("Failed on square root of", num_1)
    else:
        print(guess)
if __name__ == "__main__":
    main()
