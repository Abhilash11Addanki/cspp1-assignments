"""This program evaluates the number of vowels in a string."""

def main():
    S = input("Enter a string:")
    num = 0
    for letter in S:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            num = num+1
    print(num)
if __name__ == "__main__":
	main()
