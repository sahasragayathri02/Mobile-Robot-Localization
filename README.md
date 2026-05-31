# Mobile-Robot-Localization


Project Title

Mobile Robot Localization using Search, CSP, Decision Making, and Bayesian Reasoning



## INTRODUCTION: 
Mobile Robot Localization is the process by which a robot estimates its position in an environment using:
* Observations from sensors
* Probabilistic motion updates
* Belief/state estimation
Instead of assuming perfect movement and perfect sensing, AI localization models uncertainty mathematically.
This is a core topic in:
* Artificial Intelligence
* Robotics
* Autonomous Vehicles
* Self-driving systems
* Drone navigation


## ALGORITHM OF THE PROJECT:
Initialize Environment
         ↓
Generate Candidate States
         ↓
Read Sensor Data
         ↓
CSP Pruning
         ↓
Bayes Filter Update
         ↓
Confidence ≥ 85% ?
       /        \
     No          Yes
      |            |
Decision Agent   A* Search
      |            |
Execute Action    Path Found
      |            |
      └────Repeat──┘
         ↓
        End

## CO WISE IMPLEMENTATION: 
## CO1 – Problem Formulation & Representation
Aim

To represent the mobile robot localization problem using states, actions, transition models, and goal conditions.

Concepts Used
State Representation: (x, y, heading)
Actions: FORWARD, TURN_LEFT, TURN_RIGHT
PEAS Framework
Transition Model
Goal Test (confidence ≥ 85%)


## CO2 – Graph Search Algorithms
Aim

To find an optimal path for the robot after localization.

Concepts Used
BFS for shortest path by moves
DFS for deep exploration
UCS for minimum-cost path
A* using Manhattan Distance heuristic
Path Planning and Cost Analysis


## CO3 – Constraint Satisfaction Problem (CSP)
Aim

To eliminate impossible robot positions using sensor observations and map constraints.

Concepts Used
Variables: Free cells in the grid
Domain: Possible robot locations
Constraints: Sensor readings
Backtracking Search
MRV and LCV Heuristics
Constraint Propagation


## CO4 – Decision Making Agent
Aim

To select the best action that maximizes information gain and minimizes movement cost.

Concepts Used
Utility-Based Agent
Entropy Reduction
Greedy One-Step Lookahead
Utility Function
Minimax and Alpha-Beta Pruning


## CO5 – Reasoning Under Uncertainty
Aim

To estimate the robot's position under uncertain movements and noisy sensor readings.

Concepts Used
Bayes Filter
Prediction Step
Correction Step
Belief State
Markov Assumption
Sensor Noise Model


## CO6 – Integrated AI Pipeline
Aim

To combine all AI techniques into a complete robot localization and navigation system.

Concepts Used
State Representation
CSP-based State Elimination
Bayes Filter Localization
Decision Agent
A* Path Planning
Explainable Reasoning Trace
