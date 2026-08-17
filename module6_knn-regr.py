"""
Assignment #6.2: Numpy

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).
"""

import numpy as np

class kNNRegressor:
  def __init__(self, N_points):
    self.N_points = N_points
    # Numpy arrays to hold x and y values of the training data
    self.X = np.zeros(N_points, dtype = float)
    self.Y = np.zeros(N_points, dtype = float)
    # How many values have been stored so far
    self._count = 0

  def insert(self, x, y):
    # insert point (x, y) into the dataset.
    if self._count >= self.N_points:
      raise ValueError("All N points have already been inserted.")
    self.X[self._count] = x
    self.Y[self._count] = y
    self._count += 1
  
  def is_full(self):
    return self._count == self.N_points # Return true once all N points have been provided.
  
  def predict(self, x_query, k):
    """
    Predict Y value based on a given value x_query using k-NN Regression.
    """
    if k > self.N_points:
      raise ValueError("k cannot be greater than N.")
    distances = np.abs(self.X - x_query) # Compute absolute distance from x_query to every training point
    nearest_indices = np.argsort(distances)[:k] # Get the indices of k smallest distances
    prediction = np.mean(self.Y[nearest_indices]) # Predicted Y is the average of Y values of the k nearest neighbors
    return prediction

def main():
  try:
    N = int(input("Enter N number of training points: "))
    if N <= 0:
      print("Error: N must be a positive integer.")
      return

    k = int(input("Enter k number of neighbors: "))
    if k <= 0:
      print("Error: k must be a positive integer.")
      return

    model = kNNRegressor(N)
    print(f"Please enter {N} (x, y) points. One at a time: ")
    for i in range(N):
      x_val = float(input(f"Enter point {i+1} - x value: "))
      y_val = float(input(f"Enter point {i+1} - y value: "))
      model.insert(x_val, y_val)

    x_query = float(input("Enter value X to predict value Y for: "))

    if k <= N:
      y_predict = model.predict(x_query, k)
      print(f"Result Y of {k}-NN Regression is: {y_predict}")
    else:
      print("Error: k cannot be greater than N.")

  except ValueError as e:
    print(f"Error: invalue input ({e}).")

if __name__ == "__main__":
  main()
