'''Exercise: Assignment-2
Implement the updateHand function. Make sure this function has no side effects:
'''

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    word_list = []
    for i in word:
        word_list += i.split(",")
    for i in hand.keys():
        if i in word_list:
            hand[i] = hand[i]-word_list.count(i)
    return hand
def main():
    '''Main Fucntion'''
    n_1 = input()
    adict = {}
    for l_1 in range(int(n_1)):
        data = input()
        l_1 = data.split()
        adict[l_1[0]] = int(l_1[1])
    data1 = input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
    main()
