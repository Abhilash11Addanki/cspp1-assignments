'''
#Exercise: Integer Division Exercise
'''
def integer_division(x_1, a_int):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x_1 >= a_int:
        count += 1
        x_1 = x_1 - a_int
    return count
def main():
    '''
    Main function.
    '''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
