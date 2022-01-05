import chess
from project.chess_utilities.utility import Utility
from project.options.EvaluateOptions import EvaluateOptions


class EvaluateUtility(Utility):
    def __init__(self, options: EvaluateOptions) -> None:
        self.options = options

    def getAbsoluteValue(self, board: chess.Board, x):

        if board.pieces(piece_type=chess.PAWN, color=chess.WHITE):
            return self.options.pawn_value + (self.options.pawnEvalWhite[x])
        elif board.pieces(piece_type=chess.PAWN, color=chess.BLACK):
            return self.options.pawn_value + (self.options.pawnEvalBlack[x])
        elif board.pieces(piece_type=chess.ROOK, color=chess.WHITE):
            return self.options.rook_value + (self.options.rookEvalWhite[x])
        elif board.pieces(piece_type=chess.ROOK, color=chess.BLACK):
            return self.options.rook_value + (self.options.rookEvalBlack[x])
        elif board.pieces(piece_type=chess.BISHOP, color=chess.WHITE):
            return self.options.bishop_value + (self.options.BishopEvalWhite[x])
        elif board.pieces(piece_type=chess.BISHOP, color=chess.BLACK):
            return self.options.bishop_value + (self.options.BishopEvalBlack[x])
        elif board.pieces(piece_type=chess.QUEEN, color=chess.WHITE):
            return self.options.queen_value + (self.options.evalQueen[x])
        elif board.pieces(piece_type=chess.QUEEN, color=chess.BLACK):
            return self.options.queen_value + (self.options.evalQueen[x])
        elif board.pieces(piece_type=chess.KING, color=chess.WHITE):
            return self.options.king_value + (self.options.kingEvalWhite[x])
        elif board.pieces(piece_type=chess.KING, color=chess.BLACK):
            return self.options.king_value + (self.options.kingEvalBlack[x])

    def getPieceValue(self, board: chess.Board, position: int):
        absoluteValue = 0
        if board.piece_at(position).color == chess.WHITE:
            absoluteValue = self.getAbsoluteValue(board, position)
        elif board.piece_at(position).color == chess.BLACK:
            absoluteValue = self.getAbsoluteValue(board, position)
        return absoluteValue

    def board_value(self, board: chess.Board):
        totalevaluation = 0
        for i in range(63):
            totalevaluation += self.getPieceValue(board, i)
        return totalevaluation
