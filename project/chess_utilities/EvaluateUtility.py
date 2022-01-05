import chess
from project.chess_utilities.utility import Utility
from project.options.EvaluateOptions import EvaluateOptions


class EvaluateUtility(Utility):
    def __init__(self, options: EvaluateOptions) -> None:
        self.options = options

    def getAbsoluteValue(self, board: chess.Board, x):
        if board.pieces(piece_type=chess.PAWN, color=chess.WHITE):
            return 10 + (self.options.pawnEvalWhite[x])
        elif board.pieces(piece_type=chess.PAWN, color=chess.BLACK):
            return 10 + (self.options.pawnEvalBlack[x])
        elif board.pieces(piece_type=chess.ROOK, color=chess.WHITE):
            return 50 + (self.options.rookEvalWhite[x])
        elif board.pieces(piece_type=chess.ROOK, color=chess.BLACK):
            return 50 + (self.options.rookEvalBlack[x])
        elif board.pieces(piece_type=chess.BISHOP, color=chess.WHITE):
            return 30 + (self.options.BishopEvalWhite[x])
        elif board.pieces(piece_type=chess.BISHOP, color=chess.BLACK):
            return 30 + (self.options.BishopEvalBlack[x])
        elif board.pieces(piece_type=chess.QUEEN, color=chess.WHITE):
            return 90 + (self.options.evalQueen[x])
        elif board.pieces(piece_type=chess.QUEEN, color=chess.BLACK):
            return 90 + (self.options.evalQueen[x])
        elif board.pieces(piece_type=chess.KING, color=chess.WHITE):
            return 900 + (self.options.kingEvalWhite[x])
        elif board.pieces(piece_type=chess.KING, color=chess.BLACK):
            return 900 + (self.options.kingEvalBlack[x])

    def getPieceValue(self, board: chess.Board, x):
        if board.pieces(piece_type=chess.PAWN, color=chess.WHITE) | board.pieces(piece_type=chess.ROOK,
                                                                                 color=chess.WHITE | board.pieces(
                                                                                         piece_type=chess.BISHOP,
                                                                                         color=chess.WHITE) | board.pieces(
                                                                                         piece_type=chess.QUEEN,
                                                                                         color=chess.WHITE) | board.pieces(
                                                                                         piece_type=chess.KING,
                                                                                         color=chess.WHITE)):
            absolutevalue = self.getAbsoluteValue(board, x)
        elif board.pieces(piece_type=chess.PAWN, color=chess.BLACK) | board.pieces(piece_type=chess.ROOK,
                                                                                   color=chess.BLACK | board.pieces(
                                                                                           piece_type=chess.BISHOP,
                                                                                           color=chess.BLACK) | board.pieces(
                                                                                           piece_type=chess.QUEEN,
                                                                                           color=chess.BLACK) | board.pieces(
                                                                                           piece_type=chess.KING,
                                                                                           color=chess.BLACK)):
            absolutevalue = self.getAbsoluteValue(board, x)
        return absolutevalue

    def board_value(self, board: chess.Board):
        totalevaluation = 0
        for i in range(63):
            totalevaluation += self.getPieceValue(self, board.piece_at(i), i)
        return totalevaluation
