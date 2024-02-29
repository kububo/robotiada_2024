from src._input import instructions


class Program:
    def __init__(self):
        self.instructions = instructions.strip().split("\n")
        self.previous_distance = 0

    def get_current_instruction(self):
        instruction = self.instructions[0].split(" ")

        if (instruction[0] == "LINE"):
            return {
                "type": "LINE",
                "radius": None,
                "length": float(instruction[1]),
                "direction": None,
            }

        return {
            "type": "ARC",
            "radius": float(instruction[1]),
            "length": float(instruction[2]),
            "direction": instruction[3]
        }

    def move_to_next_instruction(self):
        if len(self.instructions) > 1:
            self.previous_distance += self.get_current_instruction()["length"]
            self.instructions.pop(0)
