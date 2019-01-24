import ce
from ce import *

def main():
    depth = 2
    board = chess.Board()
    while True:
        print(board)
        print(board.fullmove_number)
        # x, y = int_to_cor(9)
        # print(x, y)
        boolean = board.turn  # whether it is the white turn of black turn
        # print(b)
        # piece = board.piece_at(0)
        # print(piece.color)
        # T = [[0, 1, 2], [1, 2, 3]]
        # S = list(reversed(T))
        # print(S[0][0])
        #        PawnWhite = [ [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0], [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0], [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5], [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0], [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5], [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] ]
        #        print(PawnWhite[1][0])
        if board.is_game_over():
            break
        elif boolean:
            # if white(lower)'s turn
            print("Please enter the move\n")
            fromm = eval(input("from\n"))
            too = eval(input("to\n"))
            move = chess.Move(fromm, too)
            if board.is_legal(move):
                board.push(move)
            else:
                print("Invalid Input")
                continue
        else:
            # if black's turn

            # make random move
            # index = random.randint(0,board.legal_moves.count())
            # the_iter=iter(board.legal_moves)
            # move=next(the_iter)
            # for i in range(1,index-1):
            #    move=next(the_iter)

            # choose move that has the best value(min)
            minvalue = 10000
            bestmove = chess.Move(0, 1)

            for move in board.legal_moves:
                board.push(move)
                piece = board.piece_at(6)
                # print(6, piece.color)
                # piece2 = board.piece_at(34)
                # if piece2 == None:
                #   print(34, "None!")
                depth = 6
                value = ab_search(board, -10000, 10000, depth)
                if value <= minvalue:
                    bestmove = move
                    minvalue = value
                board.pop()

            board.push(bestmove)

    print(board.result)
    board.clear()

main()