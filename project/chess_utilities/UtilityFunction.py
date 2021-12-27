import chess
from project.chess_utilities.utility import Utility
from project.options.UtilityOptions import UtilityOptions


class UtilityFunction(Utility):

    def __init__(self, options: UtilityOptions) -> None:
        self.options = options

    def board_value(self, board: chess.Board):
        n_white = 0
        n_white += len(board.pieces(piece_type=chess.PAWN, color=chess.WHITE)) * self.options.pawn_value
        n_white += len(board.pieces(piece_type=chess.BISHOP, color=chess.WHITE)) * self.options.bishop_value
        n_white += len(board.pieces(piece_type=chess.KNIGHT, color=chess.WHITE)) * self.options.knight_value
        n_white += len(board.pieces(piece_type=chess.ROOK, color=chess.WHITE)) * self.options.rook_value
        n_white += len(board.pieces(piece_type=chess.QUEEN, color=chess.WHITE)) * self.options.queen_value

        n_black = 0
        n_black += len(board.pieces(piece_type=chess.PAWN, color=chess.BLACK)) * self.options.pawn_value
        n_black += len(board.pieces(piece_type=chess.BISHOP, color=chess.BLACK)) * self.options.bishop_value
        n_black += len(board.pieces(piece_type=chess.KNIGHT, color=chess.BLACK)) * self.options.knight_value
        n_black += len(board.pieces(piece_type=chess.ROOK, color=chess.BLACK)) * self.options.rook_value
        n_black += len(board.pieces(piece_type=chess.QUEEN, color=chess.BLACK)) * self.options.queen_value
        return n_white - n_black
