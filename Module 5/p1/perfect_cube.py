# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    s = int(input())
    guess=1
    while guess**3<s:
        guess+=1
    if guess**3==s:
        print(s,"is a perfect cube")
    else:
        print(s,"is not a perfect cube")
if __name__== "__main__":
	main()
