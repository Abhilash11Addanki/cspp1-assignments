'''This program evaluates square root of number using bisection method.'''
def main():
    '''Main function.'''
    num_1 = int(input())
    epsilon = 0.01
    low = 0
    high = num_1
    guess = (high + low)/2.0
    while abs(guess**2-num_1) >= epsilon:
        if guess**2 < num_1:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    print(guess)
if __name__ == "__main__":
    main()
