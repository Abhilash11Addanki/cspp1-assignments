#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	s = raw_input()
	num=0
        for letter in S1:
            if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
                num=num+1
        print(num)

if __name__== "__main__":
	main()
