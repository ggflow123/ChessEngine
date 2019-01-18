#ce.py
#
#ce --- chess engine: a program that can play the chess
#   --- only following the basic rules of chess for now
#
#Author: Xuran Wang   Yuanzhe Liu
#
#2019/01/4

import chess
import random

# the evaluation function
def eval_func(board):
    totalEval = 0
    for i in range(0, 63):
       # piece = board.piece_at(i)
       # print(i)
       # print(piece.color)
        totalEval = totalEval + getPieceValue(i, board)
    return totalEval

def PawnWhiteValue():
    PawnWhite = [ [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0], [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5], [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0], [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5], [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] ]
    return PawnWhite


def getAbsolutePieceValue(i, board):
    if board.piece_type_at(i) == 1:#if the piece is Pawn
        return 10
    elif board.piece_type_at(i) == 2:#if the piece is Knight
        return 30
    elif board.piece_type_at(i) == 3:#if the piece is Bishop
        return 30
    elif board.piece_type_at(i) == 4:#if the piece is Rook
        return 50
    elif board.piece_type_at(i) == 5:#if the piece is Queen
        return 90
    elif board.piece_type_at(i) == 6:#if the piece is King
        return 900

def getPieceValue(i, board):
    piece = board.piece_at(i)
    #print("Get Piece value", i)
    #print(piece.color)
    if piece == None:
        return 0
    else:
        value = getAbsolutePieceValue(i, board)
        if board.piece_at(i).color:
            return value
        else:
            value = -value
            return value


# the value of search value
def ab_search(board,a,b,depth):
    if depth==0:
        return eval_func(board)
    elif board.turn:
        # if white
        v=-10000
        for move in board.legal_moves:
            board.push(move)
            v=max(v,ab_search(board,a,b,depth-1),a,b)
            if v>=b:
                board.pop()
                return v
            a=max(a,v)
            board.pop()
        return v
    else:
        # if black
        v=10000
        for move in board.legal_moves:
            board.push(move)
            v=min(v,ab_search(board,a,b,depth-1),a,b)
            if v<=a:
                board.pop()
                return v
            b=min(b,v)
            board.pop()
        return v


def main():
    depth=2
    board = chess.Board()
    while True:
        print(board)
        print(board.fullmove_number)
        boolean = board.turn #whether it is the white turn of black turn
       # print(b)
       # piece = board.piece_at(0)
       # print(piece.color)
       # T = [[0, 1, 2], [1, 2, 3]]
       # print(T[0][2])
#        PawnWhite = [ [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0], [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5], [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0], [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5], [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] ]
#        print(PawnWhite[1][0])
        if board.is_game_over():
            break
        elif boolean:
            # if white(lower)'s turn
            print("Please enter the move\n")
            fromm = eval(input("from\n"))
            too = eval(input("to\n"))
            move = chess.Move(fromm,too)
            if board.is_legal(move):
                board.push(move)
            else:
                print("Invalid Input")
                continue
        else:
            # if black's turn

            # make random move
            #index = random.randint(0,board.legal_moves.count())
            #the_iter=iter(board.legal_moves)
            #move=next(the_iter)
            #for i in range(1,index-1):
            #    move=next(the_iter)
            
            # choose move that has the best value(min)
            minvalue=10000
            bestmove=chess.Move(0,1)
            
            for move in board.legal_moves:
                board.push(move)
                piece = board.piece_at(6)
                #print(6, piece.color)
                #piece2 = board.piece_at(34)
                #if piece2 == None:
                 #   print(34, "None!")
                depth = 2
                value=ab_search(board,-10000,10000,depth)
                if value<=minvalue:
                    bestmove=move
                    minvalue=value
                board.pop()

            board.push(bestmove)

    print(board.result)
    board.clear()

main()
