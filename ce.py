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
    print(board)
    mv = chess.Move(8,16)
    board.push(mv)
    print(board)

main()
