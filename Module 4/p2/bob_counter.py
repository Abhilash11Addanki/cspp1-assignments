'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    s = input()
    s1='bob'
    len1=len(s1)
    cnt=0
    for i in range(len(s)-2):
        if s[i]+s[i+1]+s[i+2]==s1:
            cnt=cnt+1
    print(cnt)
	

if __name__== "__main__":
	main()
