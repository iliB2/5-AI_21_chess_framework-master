from project.chess_agents.agent import Agent
import chess
from project.chess_utilities.utility import Utility
import time
import random

from project.options.UtilityOptions import UtilityOptions
INFINITY = 9999


class MinimaxAgent(Agent):

    def __init__(self, utility: Utility, time_limit_move: float, maxDepth: int) -> None:
        super().__init__(utility, time_limit_move)
        self.maxDepth = maxDepth
        self.name = "Minimax search agent"
        self.nodes_explored = 0

    def calculate_move(self, board: chess.Board):
        start_time = time.time()

        flip_value = 1 if board.turn == chess.WHITE else -1
        bestMoveValue = -INFINITY
        bestMove = None
        for move in list(board.legal_moves):
            if time.time() - start_time > self.time_limit_move:
                bestMove = move
                break
            board.push(move)
            self.nodes_explored += 1
            value = max(bestMoveValue, self.minimax(self.maxDepth - 1, board, False, flip_value, -INFINITY, INFINITY))
            board.pop()
            if value > bestMoveValue:
                bestMove = move
                bestMoveValue = value

        print("Best move value: " + str(bestMoveValue))
        print("Best move: " + str(bestMove))
        print("Nodes explored: " + str(self.nodes_explored))
        return bestMove

    def minimax(self, currDepth, board, is_maximizing, flip_value, alpha, beta):
        if currDepth == 0:
            return self.utility.board_value(board) * flip_value
        if is_maximizing:
            bestMoveValue = -INFINITY
            for move in list(board.legal_moves):
                board.push(move)
                self.nodes_explored += 1
                value = self.minimax(currDepth - 1, board, not is_maximizing, flip_value, alpha, beta)
                bestMoveValue = max(bestMoveValue, value)
                alpha = max(alpha, bestMoveValue)

                board.pop()
                if beta <= alpha:
                    break
            return bestMoveValue
        else:
            bestMoveValue = INFINITY
            for move in list(board.legal_moves):
                board.push(move)
                self.nodes_explored += 1
                value = self.minimax(currDepth - 1, board, not is_maximizing, flip_value, alpha, beta)
                bestMoveValue = min(bestMoveValue, value)
                beta = min(beta, bestMoveValue)
                board.pop()
                if beta <= alpha:
                    break
            return bestMoveValue





