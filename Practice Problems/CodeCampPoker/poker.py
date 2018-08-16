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
    cnt = 0
    list_1=[]
    for i in hand:
        list_1.append(i[1])
    set_1 = set(list_1)
    for i in set_1:
        if list_1.count(i)==5:
            cnt = 1
    if cnt == 1 and len(set_1) == 1:
        return True
    return False
def is_threeofakind(hand):
    '''
    Function for finding three of a kind
    '''
    cnt = 0
    list_1=[]
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in set_1:
        if list_1.count(i)==3:
            cnt = 1
    if cnt == 1 and len(set_1) == 3:
        return True
    return False
def is_fourofakind(hand):
    '''
    Function for finding four of a kind
    '''
    cnt = 0
    list_1=[]
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in list_1:
        if list_1.count(i)==4:
            cnt += 1
    if cnt == 4 and len(set_1) == 2:
        return True
    return False
def is_fullhouse(hand):
    '''Function for finding full house'''
    cnt = 0
    cnt1 = 0
    list_1=[]
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in list_1:
        if list_1.count(i)==3:
            cnt += 1
        if list_1.count(i)==2:
            cnt1 += 1
    if (cnt==3 and cnt1==2) and len(set_1)==2:
        return True
    return False
def is_twopair(hand):
    '''Function for finding two pair'''
    cnt = 0
    list_1=[]
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in set_1:
        if list_1.count(i)==2:
            cnt += 1
    if cnt==2 and len(set_1)==3:
        return True
    return False    
def is_onepair(hand):
    '''Function for finding one pair'''
    cnt = 0
    list_1=[]
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in list_1:
        if list_1.count(i)==2:
            cnt += 1
    if cnt == 2 and len(set_1) == 4:
        return True
    return False
def is_royalflush(hand):
    '''Function for finding royal flush'''
    cnt = 0
    list_1=[]
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in list_1:
        if i in 'AKQJT':
            cnt += 1
    if cnt == 5 and len(set_1) == 5:
        return True
    return False
def is_highcard(hand):
    '''Function for finding high card'''
    cnt = 0
    list_1 = []
    for i in hand:
        list_1.append(i[0])
    set_1 = set(list_1)
    for i in list_1:
        if i == 'A':
            cnt = 1
    if cnt == 1 and len(set_1) == 5:
        return True
    return False
def hand_rank(hand):
    '''
    Function for finding the rank of a hand
    '''
    if is_royalflush(hand) and is_flush(hand):
        return 10
    if is_straight(hand) and is_flush(hand):
        return 9
    if is_fourofakind(hand):
        return 8
    if is_fullhouse(hand):
        return 7
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_threeofakind(hand):
        return 4
    if is_twopair(hand):
        return 3
    if is_onepair(hand):
        return 2
    if is_highcard(hand):
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
