'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
    Function for finding straight
    '''
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6,
              '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    list_1 = []
    for card in hand:
        list_1.append(a_dict[card[0]])
    list_1.sort()
    for each in range(len(list_1)-1):
        if (list_1[each]-list_1[each+1]) != -1:
            return False
        return True
def is_flush(hand):
    '''
    Function for finding flush
    '''
    cnt1 = 0
    if (hand[0][1] == 'D' and hand[1][1] == 'D' and hand[2][1] == 'D'
        and hand[3][1] == 'D' and hand[4][1] == 'D'):
        cnt1 = 1
    elif (hand[0][1] == 'C' and hand[1][1] == 'C' and hand[2][1] == 'C'
          and hand[3][1] == 'C' and hand[4][1] == 'C'):
        cnt1 = 1
    elif (hand[0][1] == 'H' and hand[1][1] == 'H' and hand[2][1] == 'H'
          and hand[3][1] == 'H' and hand[4][1] == 'H'):
        cnt1 = 1
    elif (hand[0][1] == 'S' and hand[1][1] == 'S' and hand[2][1] == 'S'
          and hand[3][1] == 'S' and hand[4][1] == 'S'):
        cnt1 = 1
    if cnt1 == 1:
        return True
    return False
def is_threeofakind(hand):
    '''
    Function for finding three of a kind
    '''
    cnt = 0
    list_1=[]
    for i in hand[0]:
        list_1.append(i[0])
    for i in hand[0]:
        if list_1.count(i[0])==3:
            return True
        return False
def is_fourofakind(hand):
    '''
    Function for finding four of a kind
    '''
    list_1=[]
    for i in hand[0]:
        list_1.append(i[0])
    for i in hand[0]:
        if list_1.count(i[0])==4:
            return True
        return False
def hand_rank(hand):
    '''
    Function for finding the rank of a hand
    '''
    if is_straight(hand) and is_flush(hand):
        return 5
    if is_fourofakind(hand):
        return 4
    if is_flush(hand):
        return 3
    if is_straight(hand):
        return 2
    if is_threeofakind(hand):
        return 1
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
