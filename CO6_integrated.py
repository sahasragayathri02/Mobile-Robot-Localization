# ===============================
# CO6 - Integrated Pipeline
# ===============================

states = [(0,0),(0,1),(1,0),(1,1)]

print("\n--- CO6: INTEGRATED PIPELINE ---")
print("Initial States:", states)

valid_states = [s for s in states if s != (1,1)]
print("CSP Filtered:", valid_states)

belief = {s:1/len(valid_states) for s in valid_states}
print("Belief:", belief)

best_action = "FORWARD"
confidence = 0.90

print("Action:", best_action)
print("Confidence:", confidence)

if confidence >= 0.85:
    print("Robot Localized ✔")

    path = [(0,0),(0,1),(1,1),(2,1)]
    print("Planned Path:", path)
else:
    print("Continue Localization")
