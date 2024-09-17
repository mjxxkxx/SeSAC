from random import randint 

def random_player(x_or_o, x_positions, o_positions):
    move = (0, 0)
    while move in x_positions + o_positions:
        x = randint(0, 2)
        y = randint(0, 2)
        move = (x, y)
    return move 

def smart_player(x_or_o, x_positions, o_positions):
    x_pos = x_positions
    o_pos = o_positions
    
    winning_positions = [
        [(0,0),(0,1),(0,2)],
        [(0,0),(1,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(1,1),(0,2)],
        [(2,0),(2,1),(2,2)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
    ]
    
    def find_winning_move(player_positions, opponent_positions):
        for pos in winning_positions:
            positions_set = set(pos)
            if positions_set.issubset(player_positions):
                continue  # 이미 모두 채워진 위치는 건너뜀
            empty_positions = set(positions_set) - set(player_positions) - set(opponent_positions)
            if len(empty_positions) == 1:
                return empty_positions.pop()
        return None
    
    if len(x_pos) == 1 and len(o_pos) == 2:
        move = find_winning_move(o_pos, x_pos)
        if move:
            return move
    
    if len(x_pos) == 2 and len(o_pos) == 1:
        move = find_winning_move(x_pos, o_pos)
        if move:
            return move
    
    if len(x_pos) == 2 and len(o_pos) == 2:
        if x_or_o == 'X':  # X 차례일 때
            move = find_winning_move(x_pos, o_pos)
            if move:
                return move
        
        elif x_or_o == 'O':  # O 차례일 때
            move = find_winning_move(o_pos, x_pos)
            if move:
                return move

    return random_player(x_or_o, x_positions, o_positions)