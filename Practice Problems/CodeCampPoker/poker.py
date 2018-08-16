'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def get_faceval(hand):
    return sorted(['--23456789TJQKA'.index(face) for face,suite in hand], reverse=True)
def is_straight(hand):
    '''Function for finding straight'''
    face_val = get_faceval(hand)
    if face_val == [14,5,4,3,2]:
        face_val = [5,4,3,2,1]
    set_1 = set(face_val)
    return (len(set_1)==5) and ((max(set_1)-min(set_1)) == 4)
def is_flush(hand):
    '''Function for finding flush'''
    set_1 = set([suite for face, suite in hand])
    return len(set_1) == 1
def kind(face_val, n_1):
    for face in face_val:
        if face_val.count(face) == n_1:
            return face
def hand_rank(hand):
    '''Function for finding the rank of a hand'''
    face_val = get_faceval(hand)
    return ((8, face_val) if is_flush(hand) and is_straight(hand) else
            (7, kind(face_val, 4), face_val) if kind(face_val, 4) else
            (6, kind(face_val, 3), kind(face_val, 2)) if kind(face_val, 3) and
             kind(face_val, 2) else
            (5, face_val) if is_flush(hand) else
            (4, face_val) if is_straight(hand) else
            (3, kind(face_val, 3), face_val) if kind(face_val, 3) else
            (2, kind(face_val, 2), kind(sorted(face_val), 2), face_val)
            if kind(face_val, 2) and kind(sorted(face_val), 2) else
            (1, kind(face_val, 2), face_val) if kind(face_val, 2) else
            (0, face_val))

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
