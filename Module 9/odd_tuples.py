'''Exercise : Odd Tuples'''
def odd_tuples(a_tup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    l_1 = len(a_tup)
    res_1 = ()
    for i in range(0, l_1, 2):
        res_1 += (a_tup[i],)
    return res_1
def main():
    '''Main Function.'''
    data = input()
    data = data.split()
    a_tup = ()
    for j in range(len(data)):
        a_tup += (data[j],)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
