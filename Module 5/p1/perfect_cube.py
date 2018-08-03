'''This program evaluates whether given number is a perfect cube or not'''
def main():
    '''Main function.'''
    s = int(input())
    guess = 1
    while guess**3 < s:
        guess += 1
    if guess**3 == s:
        print(s, "is a perfect cube")
    else:
        print(s, "is not a perfect cube")
if __name__ == "__main__":
    main()
