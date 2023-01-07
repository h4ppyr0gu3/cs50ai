"""
Tic Tac Toe Player
"""

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
    xsum = 0
    osum = 0
    for i in board:
        for j in i:
            if j == X:
                xsum += 1
            if j == O:
                osum += 1

    if xsum > osum:
        return O
    if osum > xsum:
        return X
    if osum == xsum:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = []
    for i in board:
        for j in i:
            if j == None:
                moves.append((i, j))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if len(list(set(i))) == 1 && list(set(i)) != [None]:
            return list(set(i))[0]
        for i in range(0, 3):
            # last = None
            # count = 0
        # for j in i:

    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
