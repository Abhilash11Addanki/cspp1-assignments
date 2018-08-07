'''Power using iteration.'''
def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    res_num = 1
    i = 1
    while i <= exp:
        res_num *= base
        i += 1
    return int(res_num)
def main():
    '''Main function'''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
