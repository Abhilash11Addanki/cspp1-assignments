# Write a python program to find the square root of the given number 
# using approximation method

def main():
    s = input()
    epsilon=0.001
    guess=1
    increment=0.0001
    while abs(guess**2-n)>=epsilon:
        guess+=increment
    if abs(guess**2-n)>=epsilon:
        print("Failed on square root of",n)
    else:
        print(guess,"is close to the square root of",n)
if __name__== "__main__":
	main()
