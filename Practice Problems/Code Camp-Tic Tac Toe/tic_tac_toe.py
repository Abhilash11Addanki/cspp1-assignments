def rows(game_hand):
    winner_x = False
    winner_o = False
    for row in game_hand:
        if row.count('x') == 3:
            winner_x = True
        if row_count('o') == 3:
            winner_o = True
    if winner_x and winner_o:
        print("invalid game")
        exit()
    if winner_x:
        return (True, "x")
    if winner_o:
        return (True, "o")
    return (False, 0)
def column(game_hand):
    transpose = []
    for i in range(len(game_hand)):
        row = []
        for j in range(len(game_hand[0])):
            row.append(game_hand[j][i])
        transpose.append(row)
    return rows(transpose)
def diagnols(game_hand):
    d1 =[]
    for i in range(len(game_hand)):
	d1.append(game_hand[i][i])
    if d1.count("o")==3:
	return (True,"o")
    if  d1.count("x")==3:
	return (True,"x")
    d2 =[]
    j=len(game_hand[0])-1
    for i in range(len(game_hand)):
	d2.append(game_hand[i][j])
	j=j-1
    if d2.count("o")==3:
	return (True,"o")
    if  d2.count("x")==3:
	return (True,"x")
    return (False,0)
def win_hand(game_hand):
    if rows(game_hand)[0]:
        print(rows(game_hand)[1])
    elif column(game_hand)[0]:
        print(column(game_hand)[1])
    elif diagnols(game_hand)[0]:
        print(diagnols(game_hand)[1])
    else:
        print("draw")
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
    return True if abs(cnt_x-cnt_o) == 1 or abs(cnt_x-cnt_o) == 0 else False
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
