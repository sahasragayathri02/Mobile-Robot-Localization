# CO5 - Bayes Filter

belief = {
    "A":0.25,
    "B":0.25,
    "C":0.25,
    "D":0.25
}

likelihood = {
    "A":0.1,
    "B":0.9,
    "C":0.6,
    "D":0.2
}

print("\nInitial Belief")
print(belief)

new_belief = {}

total = 0

for state in belief:

    new_belief[state] = (
        belief[state] *
        likelihood[state]
    )

    total += new_belief[state]

for state in new_belief:
    new_belief[state] /= total

print("\nUpdated Belief")
print(new_belief)

most_likely = max(
    new_belief,
    key=new_belief.get
)

print("\nMost Likely State:",most_likely)
