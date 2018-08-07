'''Power using recursion.'''
def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    return int(base*recur_power(base, exp-1))
def main():
    '''Main function.'''
    data = input()
    data = data.split(" ")
    print(recur_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
