"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt_X = 0
    cnt_O = 0
    for row in board:
        cnt_X += row.count(X)
        cnt_O += row.count(O)
    if cnt_X <= cnt_O:
        return X
    else:
        return O
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == None:
                action.add((i,j))
    return action
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """


    new_board = deepcopy(board)
    (i,j) = action
    if board[i][j] != EMPTY:
        raise Exception("invalid opetation")
    new_board[i][j] = player(board)
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY:
        return board[1][1]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        move = ()
        if terminal(board):
            return utility(board), move
        t = -5
        for action in actions(board):
            max_v = min_value(result(board, action))[0]
            if max_v > t:
                t = max_v
                move = action
        return t, move
    
    def min_value(board):
        move = ()
        if terminal(board):
            return utility(board), move
        t = 5
        for action in actions(board):
            min_v = max_value(result(board,action))[0]
            if min_v < t:
                t = min_v
                move = action
        return t,move
    
    c_player = player(board)
    if terminal(board):
        return None
    if c_player == X:
        return max_value(board)[1]
    return min_value(board)[1]


    raise NotImplementedError
