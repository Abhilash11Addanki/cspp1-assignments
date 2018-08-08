'''Exercise : Function and Objects Exercise-2
   Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8].'''
def apply_to_each(L, f):
    l=len(L)
    list_1=[]
    for i in range(l):
        list_1+=[L[i]+f]
    return list_1
def main():
    data = input()
    data = data.split()
    list1 = []
    inc = 1
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
