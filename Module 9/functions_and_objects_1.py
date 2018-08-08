'''Exercise : Function and Objects Exercise-1
   Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]'''
def apply_to_each(L_list, f_abs):
    l_len = len(L_list)
    l1_list = []
    for i in range(l_len):
        l1_list = l1_list+[f_abs(L_list[i])]
    return l1_list
def main():
    data = input()
    data = data.split()
    list_1 = []
    for j in data:
        list_1.append(int(j))
    print(apply_to_each(list_1, abs))
if __name__ == "__main__":
    main()
