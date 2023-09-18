from copy import deepcopy
from checkers.pieces import Piece
import pygame
import math

RED = (255,0,0)
WHITE = (255,255,255)
EMPTY = 0

def minimax(position, depth, maxPlayer):
    if depth == 0:
        return position.evaluate(), position
    
    if maxPlayer == True:
        return max_player(position, depth)

    else:
        return min_player(position, depth)

def max_player(position, depth):
    if depth == 0:
        return position.evaluate(), position
    move = position
    moves = getAllMoves(position, WHITE)
    v_max = -math.inf
    for i in moves:
        eval_ = min_player(i, depth-1)[0]
        if v_max <= eval_:
            v_max = eval_
            move = i
    return v_max, move

def min_player(position, depth):
    if depth == 0:
        return position.evaluate(), position
    move = position
    moves = getAllMoves(position, RED)
    v_min = math.inf
    for i in moves:
        eval_ = max_player(i, depth-1)[0]
        if v_min >= eval_:
            v_min = eval_
            move = i
    return v_min, move
    
def simulateMove(piece, move, board, skip):
    row = move[0]
    col = move[1]
    
    board.move(piece, row, col)
    
    if skip:
        board.remove(skip)
    return board

def getAllMoves(board, color):
    all_moves = []
    pieces = board.getAllPieces(color)
    
    for p in pieces:
        valid_moves = board.getValidMoves(p)
        for move, skipped in valid_moves.items():
            board_copy = deepcopy(board)
            piece_copy = board_copy.getPiece(p.row, p.col)
            new_move_board = simulateMove(piece_copy, move, board_copy, skipped)
            all_moves.append(new_move_board)
    return all_moves