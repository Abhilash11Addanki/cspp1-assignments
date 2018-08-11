# Assignment-3
'''
Checking whether the word is valid one or not!
'''

def is_validword(word, hand, word_list1):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    word_list = []
    cnt_1 = 0
    for i in word:
        word_list += i.split(",")
    for i in word_list:
        if i in hand.keys():
            cnt_1 += 1
    if cnt_1 == len(word) and word in word_list1:
        return True
    return False
def main():
    '''main function.'''
    word_1 = input()
    n_1 = int(input())
    a_dict = {}
    for l_1 in range(n_1):
        data_1 = input()
        l_1 = data_1.split()
        a_dict[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_validword(word_1, a_dict, l_2))
if __name__ == "__main__":
    main()
