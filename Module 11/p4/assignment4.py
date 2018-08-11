#Exercise: Assignment-4
'''calculate handlen function.'''

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    cnt_1 = 0
    for i in hand.keys():
        cnt_1 += hand[i]
    return cnt_1
def main():
    '''main fucntion.'''
    n_1 = input()
    a_dict = {}
    for l_1 in range(int(n_1)):
        data = input()
        l_1 = data.split()
        a_dict[l_1[0]] = int(l_1[1])
    print(calculate_handlen(a_dict))
if __name__ == "__main__":
    main()
