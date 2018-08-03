'''This program evaluates whether given number is a perfect cube or not'''
def main():
    '''Main function.'''
    num_1 = int(input())
    guess = 1
    while guess**3 < num_1:
        guess += 1
    if guess**3 == num_1:
        print(num_1, "is a perfect cube")
    else:
        print(num_1, "is not a perfect cube")
if __name__ == "__main__":
    main()

