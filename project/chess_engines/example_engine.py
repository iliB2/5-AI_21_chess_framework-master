#!/usr/bin/python3
from project.chess_agents.minimax_agent import MinimaxAgent
from project.chess_engines.uci_engine import UciEngine
import chess
from project.chess_agents.example_agent import ExampleAgent
from project.chess_utilities.UtilityFunction import UtilityFunction
from project.chess_utilities.example_utility import ExampleUtility
from project.options.UtilityOptions import UtilityOptions

if __name__ == "__main__":
    # Create your utility
    options = UtilityOptions()
    utility = UtilityFunction(options)
    # Create your agent
    agent = MinimaxAgent(utility, 5.0, 2)
    # Create the engine
    engine = UciEngine("Minimax engine", "iliB", agent)
    # Run the engine (will loop until the game is done or exited)
    engine.engine_operation()
