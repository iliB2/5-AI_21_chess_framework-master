from project.chess_agents.agent import Agent
import chess
from project.chess_utilities.utility import Utility
import time
import random

from project.options.UtilityOptions import UtilityOptions


class MinimaxAgent(Agent):

    def __init__(self, utility: Utility, time_limit_move: float, maxDepth: int) -> None:
        super().__init__(utility, time_limit_move)
        self.maxDepth = maxDepth
        self.name = "Minimax search agent"

    def calculate_move(self, board: chess.Board):
        start_time = time.time()

        flip_value = 1 if board.turn == chess.WHITE else -1
        bestMoveValue = -9999
        bestMove = None
        for move in list(board.legal_moves):
            if time.time() - start_time > self.time_limit_move:
                bestMove = move
                break
            board.push(move)
            value = max(bestMoveValue, self.minimax(self.maxDepth - 1, board, False, flip_value))
            board.pop()
            if value > bestMoveValue :
                bestMove = move
                bestMoveValue = value

        print("Best move value: " + str(bestMoveValue))
        print("Best move: " + str(bestMove))
        return bestMove

    def minimax(self, currDepth, board, is_maximizing, flip_value):
        if currDepth == 0:
            return self.utility.board_value(board) * flip_value
        if is_maximizing:
            bestMove = -9999
            for move in list(board.legal_moves):
                board.push(move)
                bestMove = max(bestMove, self.minimax(currDepth - 1, board, not is_maximizing, flip_value))
                board.pop()
            return bestMove
        else:
            bestMove = 9999
            for move in list(board.legal_moves):
                board.push(move)
                bestMove = min(bestMove, self.minimax(currDepth - 1, board, not is_maximizing, flip_value))
                board.pop()
            return bestMove





