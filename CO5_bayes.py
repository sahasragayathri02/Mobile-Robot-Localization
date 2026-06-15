# ===============================
# CO5 - Bayes Filter
# ===============================

belief = {"A":0.25,"B":0.25,"C":0.25,"D":0.25}
likelihood = {"A":0.1,"B":0.9,"C":0.6,"D":0.2}

print("\n--- CO5: BAYES FILTER ---")
print("Initial Belief:", belief)

new_belief = {}
total = 0

for s in belief:
    new_belief[s] = belief[s] * likelihood[s]
    total += new_belief[s]

for s in new_belief:
    new_belief[s] /= total

print("Updated Belief:", new_belief)
print("Most Likely:", max(new_belief, key=new_belief.get))
