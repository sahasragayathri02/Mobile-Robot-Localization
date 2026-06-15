# ===============================
# CO1 - Problem Representation
# ===============================

class State:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def __str__(self):
        return f"({self.x},{self.y},{self.heading})"


ACTIONS = ["FORWARD", "TURN_LEFT", "TURN_RIGHT"]

robot = State(2, 3, "N")
confidence = 0.87

print("\n--- CO1: STATE REPRESENTATION ---")
print("Robot State:", robot)
print("Actions:", ACTIONS)

print("Goal Test:", "Localized" if confidence >= 0.85 else "Continue")
