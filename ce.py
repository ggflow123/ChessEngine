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

def main():
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
            index = random.randint(0,board.legal_moves.count())
            the_iter=iter(board.legal_moves)
            move=next(the_iter)
            for i in range(1,index-1):
                move=next(the_iter)
            board.push(move)

    print(board.result)
    board.clear()

main()
