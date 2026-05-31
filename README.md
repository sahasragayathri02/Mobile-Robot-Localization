# Mobile Robot Localization using Artificial Intelligence

## Project Overview

This project implements a Mobile Robot Localization system using core Artificial Intelligence concepts covered in the Computational Foundations for Artificial Intelligence (CFAI) course.

The robot operates in a 2D grid environment and estimates its position using sensor observations, probabilistic reasoning, constraint satisfaction, and decision-making techniques. Once the robot is localized with sufficient confidence, path planning is performed using search algorithms.

---

## Objectives

* Represent robot states and actions in a grid environment.
* Perform path planning using graph search algorithms.
* Apply Constraint Satisfaction Problems (CSP) for candidate state elimination.
* Implement Bayesian reasoning for localization under uncertainty.
* Use a utility-based decision agent for action selection.
* Integrate all modules into a complete AI localization pipeline.

---

## AI Concepts Used

### CO1 – Problem Formulation & Representation

* State Space Representation
* PEAS Framework
* Transition Model
* Goal Test

### CO2 – Graph Search Algorithms

* Breadth First Search (BFS)
* Depth First Search (DFS)
* Uniform Cost Search (UCS)
* A* Search

### CO3 – Constraint Satisfaction Problem (CSP)

* Candidate State Elimination
* Backtracking
* MRV and LCV Heuristics

### CO4 – Decision Making Agent

* Utility-Based Agent
* Greedy Action Selection
* Information Gain

### CO5 – Reasoning Under Uncertainty

* Bayes Filter
* Belief State Update
* Sensor Noise Modeling

### CO6 – Integrated AI Pipeline

* CSP + Bayes Filter + Decision Agent + A* Search

---

## Project Structure

Mobile-Robot-Localization-CFAI/

├── CO1_representation.py

├── CO2_search.py

├── CO3_csp.py

├── CO4_decision_agent.py

├── CO5_bayes_filter.py

├── CO6_integrated.py

├── Project_Report.pdf

├── PPT_Presentation.pptx

└── README.md

---

## How to Run

Run any module using Python:

python CO1_representation.py

python CO2_search.py

python CO3_csp.py

python CO4_decision_agent.py

python CO5_bayes_filter.py

python CO6_integrated.py

---

## System Workflow

Sensor Reading
↓
CSP Pruning
↓
Bayes Filter Update
↓
Decision Agent
↓
Execute Action
↓
Localization Check
↓
A* Path Planning

---

## Applications

* Autonomous Vehicles
* Warehouse Robots
* Delivery Robots
* Rescue Robots
* Indoor Navigation Systems

---

## Technologies Used

* Python 3.x
* Artificial Intelligence Algorithms
* Graph Search Techniques
* Bayesian Reasoning
* Constraint Satisfaction

---


## Course Details

Course: Computational Foundations for Artificial Intelligence (CFAI)

