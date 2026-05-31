# CO1 - Problem Formulation and Representation

class State:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def __str__(self):
        return f"({self.x},{self.y},{self.heading})"


ACTIONS = ["FORWARD", "TURN_LEFT", "TURN_RIGHT"]

robot = State(2, 3, "N")

print("\n--- MOBILE ROBOT STATE REPRESENTATION ---")
print("Current State:", robot)
print("Available Actions:", ACTIONS)

confidence = 0.87

print("\nGoal Test:")
if confidence >= 0.85:
    print("Localization Successful")
else:
    print("Continue Localization")
