"""This program evaluates the number of vowels in a string."""

def main():
    s = input()
    num = 0
    for letter in s:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            num = num+1
    print(num)
if __name__ == "__main__":
	main()
