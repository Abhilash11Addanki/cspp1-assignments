"""This program evaluates the number of vowels in a string"""
def main():
    S = input()
    num = 0
    for letter in S:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            num = num+1
    print(num)

if __name__== "__main__":
	main()
