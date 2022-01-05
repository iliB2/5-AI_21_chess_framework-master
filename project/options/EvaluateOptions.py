from project.options.options import Options

class EvaluateOptions(Options):
    def __init__(self):
        super().__init__()
        self.pawnEvalWhite = [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
                              5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
                              1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
                              0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
                              0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
                              0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
                              0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5,
                              0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

        self.pawnEvalBlack = self.pawnEvalWhite.__reversed__()

        self.KnightEval = [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
                           -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
                           -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
                           -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
                           -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
                           -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
                           -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
                           -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]

        self.BishopEvalWhite = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
                                 -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
                                 -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
                                 -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
                                 -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
                                 -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
                                 -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
                                 -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]

        self.BishopEvalBlack = self.BishopEvalWhite.__reversed__()

        self.rookEvalWhite = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
                                0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
                               -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                               -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                               -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                               -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                               -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                                0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]

        self.rookEvalBlack = self.rookEvalWhite.__reversed__()

        self.evalQueen = [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
                           -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
                           -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
                           -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
                            0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
                           -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
                           -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
                           -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]

        self.kingEvalWhite = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                              -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                              -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
                              -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                               2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
                               2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]

        self.kingEvalBlack = self.kingEvalWhite.__reversed__()
        self.pawn_value = 10
        self.knight_value = 30
        self.bishop_value = 30
        self.rook_value = 50
        self.queen_value = 90
        self.king_value = 900

