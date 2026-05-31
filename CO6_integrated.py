# CO6 - Integrated AI Pipeline

states = [
    (0,0),
    (0,1),
    (1,0),
    (1,1)
]

print("\nSTEP 1 : Initial States")
print(states)

# CSP

valid_states = [
    s for s in states
    if s != (1,1)
]

print("\nSTEP 2 : CSP Pruning")
print(valid_states)

# Bayes

belief = {}

for s in valid_states:
    belief[s] = 1/len(valid_states)

print("\nSTEP 3 : Belief Distribution")
print(belief)

# Decision Agent

best_action = "FORWARD"

print("\nSTEP 4 : Decision Agent")
print("Selected Action =",best_action)

# Goal Test

confidence = 0.90

print("\nSTEP 5 : Goal Test")
print("Confidence =",confidence)

if confidence >= 0.85:

    print("\nRobot Localized")

    path = [
        (0,0),
        (0,1),
        (1,1),
        (2,1)
    ]

    print("\nSTEP 6 : A* Planned Path")
    print(path)

else:

    print("Continue Localization")
