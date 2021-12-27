import chess
from project.chess_utilities.utility import Utility
from project.options.UtilityOptions import UtilityOptions


class UtilityFunction(Utility):

    def __init__(self) -> None:
        pass

    def board_value(self, board: chess.Board, options: UtilityOptions):
        n_white = 0
        n_white += len(board.pieces(piece_type=chess.PAWN, color=chess.WHITE)) * options.pawn_value
        n_white += len(board.pieces(piece_type=chess.BISHOP, color=chess.WHITE)) * options.bishop_value
        n_white += len(board.pieces(piece_type=chess.KNIGHT, color=chess.WHITE)) * options.knight_value
        n_white += len(board.pieces(piece_type=chess.ROOK, color=chess.WHITE)) * options.rook_value
        n_white += len(board.pieces(piece_type=chess.QUEEN, color=chess.WHITE)) * options.queen_value

        n_black = 0
        n_black += len(board.pieces(piece_type=chess.PAWN, color=chess.BLACK)) * options.pawn_value
        n_black += len(board.pieces(piece_type=chess.BISHOP, color=chess.BLACK)) * options.bishop_value
        n_black += len(board.pieces(piece_type=chess.KNIGHT, color=chess.BLACK)) * options.knight_value
        n_black += len(board.pieces(piece_type=chess.ROOK, color=chess.BLACK)) * options.rook_value
        n_black += len(board.pieces(piece_type=chess.QUEEN, color=chess.BLACK)) * options.queen_value
        return n_white - n_black
