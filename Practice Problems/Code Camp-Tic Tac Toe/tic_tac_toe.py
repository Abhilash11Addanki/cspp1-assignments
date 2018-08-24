def win_hand(game_hand):
    for i in game_hand:
        if i[0] == i[1] == i[2] == 'x':
            return 'x'
        if i[0] == i[1] == i[2] == 'o':
            return 'o'
        if i[0][0] == i[1][0] == i[2][0] == 'x':
            return 'x'
        if i[0][0] == i[1][0] == i[2][0] == 'o':
            return 'o'
        if i[0][0] == i[1][1] == i[2][2] == 'x':
            return 'x'
        if i[0][2] == i[1][1] == i[2][0] == 'x':
            return 'x'
        if i[0][0] == i[1][1] == i[2][2] == 'o':
            return 'o'
        if i[0][2] == i[1][1] == i[2][0] == 'o':
            return 'o'
def invalid_input(game_hand):
    for i in game_hand:
        if i[0] not in 'xo.' or i[1] not in 'xo.' or i[2] not in 'xo.':
            return True
def invalid_game(game_hand):
    cnt_x = 0
    cnt_o = 0
    for i in game_hand:
        cnt_x += i.count('x')
        cnt_o += i.count('o')
    return True if cnt_x-cnt_o > 1 or cnt_o-cnt_x > 1 else False
def play_game(game_hand):
    '''Function for playing the game'''
    if invalid_input(game_hand) is True:
        return "invalid input"
    elif invalid_game(game_hand) is True:
        return "invalid game"
    res_1 = win_hand(game_hand)
    return res_1
def read_input():
    read_input = [input().split(" ") for i in range(3)]
    return read_input
def main():
    '''Main function.'''
    hand_1 = read_input()
    print(play_game(hand_1))
if __name__ == '__main__':
    main()
