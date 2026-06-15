# ===============================
# CO4 - Decision Agent
# ===============================

actions = {
    "FORWARD": {"info_gain":5, "cost":1},
    "TURN_LEFT":{"info_gain":3, "cost":0.5},
    "TURN_RIGHT":{"info_gain":2, "cost":0.5}
}

def utility(info_gain, cost):
    return info_gain - 0.2 * cost

best_action = None
best_score = -999

print("\n--- CO4: DECISION AGENT ---")

for a, data in actions.items():
    score = utility(data["info_gain"], data["cost"])
    print(a, "=>", score)

    if score > best_score:
        best_score = score
        best_action = a

print("Best Action:", best_action)
