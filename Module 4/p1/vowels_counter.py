"""This program evaluates the number of vowels in a string."""

def main():
    str_1 = input()
    num = 0
    for letter in str_1:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            num = num+1
    print(num)
if __name__ == "__main__":
    main()
