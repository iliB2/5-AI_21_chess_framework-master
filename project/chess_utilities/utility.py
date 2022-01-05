from abc import ABC
import chess

from project.options.UtilityOptions import UtilityOptions

"""A generic utility class"""


class Utility(ABC):

    # Determine the value of the current board position (high is good for white, low is good for black, 0 is neutral)
    def board_value(self, board: chess.Board):
        pass

    def evaluateboard(self, board: chess.Board):
        pass
