import chess
from project.chess_utilities.utility import Utility
from project.options.EvaluateOptions import EvaluateOptions


class EvaluateUtility(Utility):
    def __init__(self, options: EvaluateOptions) -> None:
        self.options = options

    def getAbsoluteValue(self, board: chess.Board, x):
        if board.piece_at(x).piece_type == 1 & board.piece_at(x).color == chess.WHITE:
            return self.options.pawn_value + (self.options.pawnEvalWhite[x])
        elif board.piece_at(x).piece_type == 1 & board.piece_at(x).color == chess.BLACK:
            return self.options.pawn_value + (self.options.pawnEvalBlack[x])
        elif board.piece_at(x).piece_type == 2 & board.piece_at(x).color == chess.WHITE:
            return self.options.knight_value + (self.options.KnightEval[x])
        elif board.piece_at(x).piece_type == 2 & board.piece_at(x).color == chess.BLACK:
            return self.options.knight_value + (self.options.KnightEval[x])
        elif board.piece_at(x).piece_type == 4 & board.piece_at(x).color == chess.WHITE:
            return self.options.rook_value + (self.options.rookEvalWhite[x])
        elif board.piece_at(x).piece_type == 4 & board.piece_at(x).color == chess.BLACK:
            return self.options.rook_value + (self.options.rookEvalBlack[x])
        elif board.piece_at(x).piece_type == 3 & board.piece_at(x).color == chess.WHITE:
            return self.options.bishop_value + (self.options.BishopEvalWhite[x])
        elif board.piece_at(x).piece_type == 3 & board.piece_at(x).color == chess.BLACK:
            return self.options.bishop_value + (self.options.BishopEvalBlack[x])
        elif board.piece_at(x).piece_type == 5 & board.piece_at(x).color == chess.WHITE:
            return self.options.queen_value + (self.options.evalQueen[x])
        elif board.piece_at(x).piece_type == 5 & board.piece_at(x).color == chess.BLACK:
            return self.options.queen_value + (self.options.evalQueen[x])
        elif board.piece_at(x).piece_type == 6 & board.piece_at(x).color == chess.WHITE:
            return self.options.king_value + (self.options.kingEvalWhite[x])
        elif board.piece_at(x).piece_type == 6 & board.piece_at(x).color == chess.BLACK:
            return self.options.king_value + (self.options.kingEvalBlack[x])
        else:
            return 0

    def board_value(self, board: chess.Board):
        totalevaluation = 0
        for i in range(64):
            if board.piece_at(i):
                totalevaluation += self.getAbsoluteValue(board, i)
        return totalevaluation
