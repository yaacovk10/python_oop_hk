from enum import Enum, auto

class PionPosition(Enum):
    pass

# Generate pawn positions from A2 to H7
positions = {}
for file in range(1, 9):
    for rank in range(2, 9):
        position = f"{chr(64 + file)}{rank}"
        positions[position] = (file, rank)

PionPosition = Enum('PionPosition', positions)

class PionColor(Enum):
    WHITE = 0
    BLACK = 1

class Pion:
    def __init__(self, position, color):
        self.position = position
        self.color = color
    
    def move(self, num_rows=1):
        file, rank = self.position.value
        new_rank = rank + num_rows if self.color == PionColor.WHITE else rank - num_rows
        new_position = f"{chr(64 + file)}{new_rank}"
        self.position = PionPosition[new_position]

    def kill(self, side_move_direction):
        file, rank = self.position.value
        new_file = file + side_move_direction
        new_rank = rank + 1 if self.color == PionColor.WHITE else rank - 1
        new_position = f"{chr(64 + new_file)}{new_rank}"
        self.position = PionPosition[new_position]

    def eaten(self):
        self.position = None

    def promote_to_queen(self):
        if self.color == PionColor.WHITE and self.position.value[1] == 8:
            self.position = None
        elif self.color == PionColor.BLACK and self.position.value[1] == 1:
            self.position = None

# Example usage
pion_position = PionPosition.A2
pion_color = PionColor.WHITE

pawn = Pion(pion_position, pion_color)
print(f"Initial pion position: {pawn.position.name}")

pawn.eaten()
print(f"Pion position after being eaten: {pawn.position}")

pawn = Pion(PionPosition.H8, PionColor.WHITE)
pawn.promote_to_queen()
print(f"Pion position after promotion to queen: {pawn.position}")
