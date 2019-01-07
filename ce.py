#ce.py
#
#ce --- chess engine: a program that can play the chess
#   --- only following the basic rules of chess for now
#
#Author: Xuran Wang   Yuanzhe Liu
#
#2019/01/4

import chess

def main():
    print("Hello World!!")
    board = chess.Board()
    while not board.is_game_over:
        print(board)
        if(board.turn):
            # if it is white(lower)'s turn
        else:
            # if it is black(upper)'s turn
    print(result)


    print(board)
    mv = chess.Move(8,16)
    board.push(mv)
    print(board)

main()
