'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''Main function'''
    str_1 = input()
    str_2 = 'bob'
    cnt = 0
    for i in range(len(str_1)-2):
        if str_1[i]+str_1[i+1]+str_1[i+2] == str_2:
            cnt = cnt+1
    print(cnt)
	

if __name__ ==  "__main__":
    main()
