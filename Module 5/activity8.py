'''This program tells the number that user has guessed.'''
def main():
    """guess my number"""
    mid_n = 50
    high_n = 100
    low_n = 0
    guess_n = 0
    inp_n = 'l'
    while(inp_n != 'c'):
        print(mid_n)
        inp_n = input("Enter 'h' if guess is too high,'l' if its too low.'c' to indicate I guessed correctly")
        if(inp_n == 'h'):
            high_n = mid_n
            mid_n = (high_n + low_n) // 2
        elif(inp_n == 'l'):
            low_n = mid_n
            mid_n = (high_n + low_n) // 2
    print('your guess number is :',mid_n)
if __name__== "__main__":
    main()
