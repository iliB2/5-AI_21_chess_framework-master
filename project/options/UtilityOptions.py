from project.options.options import Options


class UtilityOptions(Options):
    def __init__(self):
        super().__init__()
        self.pawn_value = 10
        self.knight_value = 30
        self.bishop_value = 30
        self.rook_value = 50
        self.queen_value = 90
        self.king_value = 900
