"""
Assignment #8.2: Scikit-learn intro (a bit deeper)

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.

In the end, the program outputs: the Precision and Recall based on the inputs.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_positive_integer(prompt):
  # Keep asking until the user provides a positive integer.
  while True:
    try:
      value = int(input(prompt))
      if value > 0:
        return value
      print("Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter a positive integer.")

def get_binary_value(prompt):
  # Keep asking until the user provides 0 or 1.
  while True:
    try:
      value = int(input(prompt))
      if value in (0, 1):
        return value
      print("Please enter 0 or 1 only.")
    except ValueError:
      print("Invalid input. Please enter 0 or 1.")

def main():
  N = get_positive_integer("Please enter a positive number N (number of points): ")
  
  x_values = np.empty(N, dtype = int) # ground truth (correct) class label
  y_values = np.empty(N, dtype = int) # predicted labels

  for i in range(N):
    print(f"\nPoint {i+1}/{N}: ")
    x_val = get_binary_value("Enter x (ground truth label, 0 or 1): ")
    y_val = get_binary_value("Enter y (predicted label, 0 or 1): ")
    
    x_values[i] = x_val
    y_values[i] = y_val

  precision = precision_score(x_values, y_values, pos_label=1, zero_division=0)
  recall = recall_score(x_values, y_values, pos_label=1, zero_division=0)

  print("\n----- Results -----")
  print(f"Precision: {precision:.2f}")
  print(f"Recall: {recall:.2f}")

if __name__ = "__main__":
  main()
