# Andrew's code for Q-Learning Model, built from scratch
import numpy as np

# This is a 4x4 Maze using Machine States, in the form of unique letters

# 6 x 6 matrix
# Let A be the starting point.
# Let G be the goal.
# Let X be an obstacle.
A = np.array([['X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'A', 'X', 'C', 'X', 'X'],
              ['X', 'E', 'X', 'G', 'H', 'X'],
              ['X', 'I', 'X', 'X', 'L', 'X'],
              ['X', 'M', 'N', 'O', 'P', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X']])
print(A, "\n")

# Mapping of location to states
B = np.array([1, 2, 3, 4, 5, 6,
              7, 8, 9 , 10, 11, 12,
              13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 23, 24,
              25, 26, 27, 28, 29, 30,
              31, 32, 33, 34, 35, 36])
print("Locations: ", B)