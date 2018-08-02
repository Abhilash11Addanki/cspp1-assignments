'''Assume s is a string of lower case characters.'''
def main():
    '''Main function.'''
    str_1 = input()
    max_str = ""
    len_1 = len(str_1)
    for j in range(len_1):
        sub_str = ""
        t_1 = str_1[j]
        for i in range(j, len(str_1)):
            if t_1 <= str_1[i]:
                t_1 = str_1[i]
                sub_str += t_1
            else:
                break
        if len(max_str) < len(sub_str):
            max_str = sub_str
    print(max_str)
if __name__ == "__main__":
    main()
