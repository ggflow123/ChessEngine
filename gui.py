import wx
import chess
import ce

class BoardFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Chess AI", size=(450, 450))
        self.board=chess.Board()
        panel = wx.Panel(self, size=wx.Size(400, 400))

        depth = 2
        board = chess.Board()
        while True:
            # draw the whole interface once again
            panel.Bind(wx.EVT_PAINT, self.draw_board)
            b_or_w = board.turn  # whether it is the white turn of black turn
            if board.is_game_over():
                break
            elif b_or_w:
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
                # choose move that has the best value(min)
                minvalue = 10000
                bestmove = chess.Move(0, 1)

                for move in board.legal_moves:
                    board.push(move)
                    piece = board.piece_at(6)
                    depth = 6
                    value = ce.ab_search(board, -10000, 10000, depth)
                    if value <= minvalue:
                        bestmove = move
                        minvalue = value
                    board.pop()

                board.push(bestmove)

        # Show who is the winner
        print(board.result)
        board.clear()














        panel.Bind(wx.EVT_LEFT_DOWN,  self.OnMove)
        wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10),size=(200,50),style=wx.CB_READONLY)
        font = wx.Font(30,wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.posCtrl.SetFont(font)
        self.posCtrl.SetBackgroundColour('black')
        self.posCtrl.SetForegroundColour('white')


    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s : %s" % (pos.x, pos.y))

    # draw the whole board according to the Board object
    def draw_board(self,event):
        # draw the grid of chessboard
        dc = wx.PaintDC(event.GetEventObject())
        dc.Clear()
        dc.SetBrush(wx.Brush(wx.Colour(255, 206, 158), style=wx.BRUSHSTYLE_SOLID))
        dc.SetPen(wx.Pen(wx.BLACK, width=0, style=wx.PENSTYLE_TRANSPARENT))
        x=0
        y=0
        for i in range(1,9):
            for j in range(1,9):
                if i%2==1:
                    if j%2==1:
                        dc.SetBrush(wx.Brush(wx.Colour(255, 206, 158), style=wx.BRUSHSTYLE_SOLID))
                    else:
                        dc.SetBrush(wx.Brush(wx.Colour(209, 139, 71), style=wx.BRUSHSTYLE_SOLID))
                else:
                    if j%2==1:
                        dc.SetBrush(wx.Brush(wx.Colour(209, 139, 71), style=wx.BRUSHSTYLE_SOLID))
                    else:
                        dc.SetBrush(wx.Brush(wx.Colour(255, 206, 158), style=wx.BRUSHSTYLE_SOLID))
                dc.DrawRectangle(x, y, 50, 50)
                x=x+50
            y=y+50
            x=0

        # draw all Pieces
        dc2 = wx.ClientDC(event.GetEventObject())
        pict = wx.Image("pic/xx.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        dc2.DrawBitmap(pict, 0, 0)


# takes in a Point Object
# return an integer indicates the location on the board
def getLocation(p):
    return 5


def main():
    app = wx.App(False)
    frame = BoardFrame()
    frame.Show(True)
    app.MainLoop()

main()