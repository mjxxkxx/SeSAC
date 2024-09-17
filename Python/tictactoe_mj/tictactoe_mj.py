game_status = {'x_positions' : [], 'o_positions' : []} 
x_pos = game_status['x_positions']
o_pos = game_status['o_positions']

def empty_board(x_size = 3, y_size = 3, x_cell_size = 7, y_cell_size = 3):
    hline = (' '+ '-' * (x_cell_size)) * x_size
    for y in range(y_size):
        print(hline)
        for z in range(y_cell_size):
            for x in range(x_size):
                print('|'+' '* x_cell_size, end = '')
            print("|")
    print(hline)

    # """Create an empty board. 

    # The board is made of horizontal lines, made with - and vertical lines, made with |. 

    # (optional) When there are no x_cell_size and y_cell_size arguments, default to arbitary size of your choice. Just make it consistent. 
    # """   


# game_status = {'x_positions' : [], 'o_positions' : []} 
def play(game_status, x_or_o, coordinate):
    
    """Main function for simulating tictactoe game moves. 

    Tictactoe game is executed by two player's moves.
    In each move, each player chooses the coordinate to place their mark. 
    It is impossible to place the mark on already taken position. 

    A move in the tictactoe game is composed of two components; 
    whether who ('X' or 'O') made the move, and how the move is made - the coordinate of the move. 

    Coordinate in our tictactoe system will use the coordinate system illustrated in the example below. 
    
    Example 1. 3 * 4 tictactoe board. 
    
         ---------- ---------- ----------
        |          |          |          |
        |  (0,0)   |  (1,0)   |  (2,0)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,1)   |  (1,1)   |  (2,1)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,2)   |  (1,2)   |  (2,2)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,3)   |  (1,3)   |  (2,3)   |
        |          |          |          |
         ---------- ---------- ----------
        """
    # if len(game_status['x_positions']) < len(game_status['o_positions']):
    #     game_status['x_positions'].append(coordinate)
    # # else: game_status['o_positions'].append(coordinate)

    # game_status['x_positions'] : 이때까지 X가 놓인 위치들
    # game_status['o_positions'] : 이때까지 O가 놓인 위치들
    # play(game_status, x_or_o, coordinate): 이번에 x_or_o를 coordinate에 두었다.
    # game_status['x_positions'].append(coordinate): 놓은 위치 추가

    if coordinate in game_status['x_positions'] + game_status['o_positions']:
        print("error")
      
    if x_or_o == 'X':
        game_status['x_positions'].append(coordinate)

    elif x_or_o == 'O':
        game_status['o_positions'].append(coordinate)   
    
    else:
        raise ValueError(f'x_or_o should be one of X or O, now got {x_or_o}.')

def check_winlose(game_status):
    """Check the game status; game status should be one of 'X wins', 'O wins', 'tie', 'not decided'. 
    """

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
    def determine_if_x_wins(game_status, winning_positions):
       for win in winning_positions:
            a,b,c = win # 이름에다 값을 넣는거다!! 
            if a in x_pos and b in x_pos and c in x_pos:
                return True
            return False
       
    def determine_if_o_wins(game_status, winning_positions):
       for win in winning_positions:
            a,b,c = win
            if a in o_pos and b in o_pos and c in o_pos:
                return True
            return False
       
    if determine_if_x_wins(game_status, winning_positions):
        return 'X wins'
    elif determine_if_o_wins(game_status, winning_positions):
        return 'O wins'       
    elif len(x_pos) + len(o_pos) == 9:
        return 'tie'
    else:   
        return 'undecided'
    
def display(game_status, x_size = 3, y_size = 3, x_cell_size = 7, y_cell_size = 3):
    """Display the current snapshot of the board. 

    'Snapshot' should contain following components. 

    - The board itself 
    - Moves that are already made

    For clarification, see provided examples. 

    Example 1. 
    When TictactoeGame instance t have following attributes; 
    - x_positions = [(0,0), (2,0), (2,1), (1,2)]
    - o_positions = [(1,0), (1,1), (0,2), (2,2)]

    t.display()
    >> 
     ---------- ---------- ----------
    |          |          |          |
    |    X     |    O     |    X     |
    |          |          |          |
     ---------- ---------- ----------
    |          |          |          |
    |          |    O     |    X     |
    |          |          |          |
     ---------- ---------- ----------
    |          |          |          |
    |    O     |    X     |    O     |
    |          |          |          |
     ---------- ---------- ----------

    """

    hline = (' '+ '-' * (x_cell_size)) * x_size
    x_pos = game_status['x_positions']
    o_pos = game_status['o_positions']
    
    for y in range(y_size):
        print(hline)
        for z in range(y_cell_size):
            for x in range(x_size):
                if z == 1:
                    if (x, y) in x_pos:
                        print('|'+' '*(x_cell_size - 1)+ 'X', end = '') 
                    elif (x, y) in o_pos:
                        print('|'+' '*(x_cell_size - 1)+ 'O', end = '')
                    else: print('|'+' '*x_cell_size, end = '')
                else: print('|'+' '*x_cell_size, end = '')
            print('|')
    print(hline)