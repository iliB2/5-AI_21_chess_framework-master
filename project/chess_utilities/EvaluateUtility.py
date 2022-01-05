import chess
from project.chess_utilities.utility import Utility
from project.options.EvaluateOptions import EvaluateOptions

class EvaluateUtility(Utility):
    def __init__(self, options: EvaluateOptions) -> None:
        self.options = options


    def getAbsoluteValue(self, board: chess.Board, x, y):
        if(board.pieces(piece_type=chess.PAWN, color=chess.WHITE)):
            return 10 + (self.options.pawnEvalWhite[y][x])
        elif(board.pieces(piece_type=chess.PAWN, color=chess.BLACK)):
            return 10 + (self.options.pawnEvalBlack[y][x])
        elif(board.pieces(piece_type=chess.ROOK, color=chess.WHITE)):
            return 50 + (self.options.rookEvalWhite[y][x])
        elif(board.pieces(piece_type=chess.ROOK, color=chess.BLACK)):
            return 50 + (self.options.rookEvalBlack[y][x])
        elif(board.pieces(piece_type=chess.BISHOP, color=chess.WHITE)):
            return 30 + (self.options.BishopEvalWhite[y][x])
        elif(board.pieces(piece_type=chess.BISHOP, color=chess.BLACK)):
            return 30 + (self.options.BishopEvalBlack[y][x])
        elif(board.pieces(piece_type=chess.QUEEN, color=chess.WHITE)):
            return 90 + (self.options.evalQueen[y][x])
        elif(board.pieces(piece_type=chess.QUEEN, color=chess.BLACK)):
            return 90 + (self.options.evalQueen[y][x])
        elif(board.pieces(piece_type=chess.KING, color=chess.WHITE)):
            return 900 + (self.options.kingEvalWhite[y][x])
        elif(board.pieces(piece_type=chess.KING, color=chess.BLACK)):
            return 900 + (self.options.kingEvalBlack[y][x])













