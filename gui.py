import wx
import chess
import ce

class BoardFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Chess AI", size=(450, 450))
        self.board=chess.Board()
        self.point=wx.Point()
        self.panel = wx.Panel(self, size=wx.Size(400, 400))
        self.dc=None
        self.start=-1
        self.end=-1
        self.depth=2
        # state=True: waiting for the first click(i.e. move a piece from board
        # state=False: waiting for the second click(i.e. put the previous piece on the board
        # after state 1, if this move is legal, AI should play a move, else once again. Then reset it to True
        self.state=True
        self.panel.Bind(wx.EVT_PAINT, self.draw_board)
        self.panel.Bind(wx.EVT_LEFT_DOWN,  self.onMove)

    # takes in a Point Object
    # return an integer indicates the location on the board
    def getLoc(self):
        x=self.point.x//50
        y=self.point.y//50
        return ((-1*y)+7)*8+x

    # deal with each click
    def onMove(self, event):
        self.point = event.GetPosition()
        if self.state:
            # waiting for the first click(i.e.move a piece from board
            self.start=self.getLoc()
            self.state=False
        else:
            # waiting for the second click(i.e. put the previous piece on the board
            # after state 1, if this move is legal, AI should play a move, else once again. Then reset it to True
            self.end=self.getLoc()
            self.state = True
            move = chess.Move(self.start, self.end)
            if self.board.is_legal(move):
                # push the users' move
                self.board.push(move)
                # print the board after user's move
                print("user moved")
                self.Refresh(True)
                self.panel.Bind(wx.EVT_PAINT, self.draw_board)
                self.test_game_over()
                # AI choose move that has the best value(min)
                minvalue = 10000
                bestmove = chess.Move(0, 1)
                for move in self.board.legal_moves:
                    self.board.push(move)
                    piece = self.board.piece_at(6)
                    self.depth = 6
                    value = ce.ab_search(self.board, -10000, 10000, self.depth)
                    if value <= minvalue:
                        bestmove = move
                        minvalue = value
                    self.board.pop()
                self.board.push(bestmove)

                # print the board after AI's move
                print("AI moved")
                self.Refresh(True)
                self.panel.Bind(wx.EVT_PAINT, self.draw_board)
                self.test_game_over()
            else:
                # indicate the move is illegal and start again
                print("illegal")


    # test the game is over or not, if so, print who is the winner
    def test_game_over(self):
        if self.board.is_game_over():
            print(self.board.result)
            self.board.clear()



    # draw the whole board according to the Board object
    def draw_board(self,event):
        # draw the grid of chessboard
        print("Hey")
        self.dc = wx.PaintDC(event.GetEventObject())
        self.dc.Clear()
        self.dc.SetBrush(wx.Brush(wx.Colour(255, 206, 158), style=wx.BRUSHSTYLE_SOLID))
        self.dc.SetPen(wx.Pen(wx.BLACK, width=0, style=wx.PENSTYLE_TRANSPARENT))
        x=0
        y=0
        for i in range(1,9):
            for j in range(1,9):
                if i%2==1:
                    if j%2==1:
                        self.dc.SetBrush(wx.Brush(wx.Colour(255, 206, 158), style=wx.BRUSHSTYLE_SOLID))
                    else:
                        self.dc.SetBrush(wx.Brush(wx.Colour(209, 139, 71), style=wx.BRUSHSTYLE_SOLID))
                else:
                    if j%2==1:
                        self.dc.SetBrush(wx.Brush(wx.Colour(209, 139, 71), style=wx.BRUSHSTYLE_SOLID))
                    else:
                        self.dc.SetBrush(wx.Brush(wx.Colour(255, 206, 158), style=wx.BRUSHSTYLE_SOLID))
                self.dc.DrawRectangle(x, y, 50, 50)
                x=x+50
            y=y+50
            x=0

        # draw all Pieces
        # dc2 = wx.ClientDC(event.GetEventObject())
        pict = wx.Image()

        loc=0
        x=0
        y=350
        while loc<=63:
            p = self.board.piece_at(loc)
            if self.board.piece_at(loc):
                if p.color: # if this piece is white
                    if p.piece_type==1: # PAWN
                        pict = wx.Image("pic/pawnW.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==2: # KNIGHT
                        pict = wx.Image("pic/knightW.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==3: # BISHOP
                        pict = wx.Image("pic/bishopW.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==4: # ROOK
                        pict = wx.Image("pic/rookW.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==5: # QUEEN
                        pict = wx.Image("pic/queenW.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==6: # KING
                        pict = wx.Image("pic/kingW.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                else: # if this piece is black
                    if p.piece_type==1: # PAWN
                        pict = wx.Image("pic/pawnB.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==2: # KNIGHT
                        pict = wx.Image("pic/knightB.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==3: # BISHOP
                        pict = wx.Image("pic/bishopB.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==4: # ROOK
                        pict = wx.Image("pic/rookB.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==5: # QUEEN
                        pict = wx.Image("pic/queenB.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
                    if p.piece_type==6: # KING
                        pict = wx.Image("pic/kingB.png", type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()

                self.dc.DrawBitmap(pict, x, y)
            if x==350:
                y=y-50
                x=0
            else:
                x=x+50
            loc=loc+1



def main():
    app = wx.App(False)
    frame = BoardFrame()
    frame.Show(True)
    app.MainLoop()

main()