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
    return

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
        if board.is_game_over():
            break
        elif(board.turn):
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
                value=ab_search(-10000,10000,board,depth)
                if value<=minvalue:
                    bestmove=move
                    minvalue=value
                board.pop()

            board.push(bestmove)

    print(board.result)
    board.clear()

main()
