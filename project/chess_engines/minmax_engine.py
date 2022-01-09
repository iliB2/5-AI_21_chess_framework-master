from project.chess_agents.minimax_agent import MinimaxAgent
from project.chess_engines.uci_engine import UciEngine
from project.chess_utilities.UtilityFunction import UtilityFunction
from project.options.UtilityOptions import UtilityOptions

if __name__ == "__main__":
    # Create your utility
    options = UtilityOptions()
    utility = UtilityFunction(options)
    # Create your agent
    agent = MinimaxAgent(utility, 14.9, 4)
    # Create the engine
    engine = UciEngine("Minimax engine", "Jeoffrey, Max & Ilias", agent)
    # Run the engine (will loop until the game is done or exited)
    engine.engine_operation()
