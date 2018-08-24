def invalid_input(game_hand):
    cnt_x = 0
    cnt_o = 0
    for i in game_hand:
        cnt_x += i.count('x')
        cnt_o += i.count('o')
    return True if cnt_x-cnt_o > 1 or cnt_o-cnt_x > 1 else False
def play_game(game_hand):
    '''Function for playing the game'''
    if invalid_input(game_hand) is True:
        print("invalid game")
def read_input():
    read_input = [input().split(" ") for i in range(3)]
    return read_input
def main():
    '''Main function.'''
    hand_1 = read_input()
    print(play_game(hand_1))
if __name__ == '__main__':
    main()
