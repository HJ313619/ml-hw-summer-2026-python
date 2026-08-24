"""
Assignment #7.2: Scikit-learn intro

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

Additionally, provide the variance of labels in the training dataset.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous task).
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def read_positive_integer(prompt):
  # Keep asking the user until they enter a valid positive integer.
  while True:
    raw_value = input(prompt)
    try:
      value = int(raw_value)
    except ValueError:
      print("Invalid input: please enter an integer.")
      continue

    if value <= 0:
      print("Invalid input: please enter a positive integer.")
      continue

    return value

def main():
  # Read N (number of points)
  N = read_positive_integer("Enter a positive integer N (number of points): ")

  # Read k (number of neighbors)
  k = read_positive_integer("Enter a positive integer k (number of neighbors): ")

  # Initialize numpy arrays
  X_data = np.zeros(N, dtype = float)
  Y_data = np.zeros(N, dtype = float)

  # Read N (x, y) points one by one
  for i in range(N):
    x_val = float(input(f"Enter x value for point {i + 1}: "))
    y_val = float(input(f"Enter y value for point {i + 1}: "))
    X_data[i] = x_val
    Y_data[i] = y_val

  # Read the query point X
  query_X = float(input("Enter X to predict Y: "))

  # Variance of labels (y values) in the training dataset
  labels_variance = np.var(Y_data)
  print(f"Variance of labels in training dataset: {labels_variance}")

  # Perform k-NN Regression if k <= N, otherwise show an error
  if k <= N:
    # scikit-learn expects a 2D array of shape (n_samples, n_features)
    X_train = X_data.reshape(-1, 1)
    y_train = Y_data

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    query_point = np.array([[query_X]])
    prediction = model.predict(query_point)

    print(f"k-NN Regression result for X={query_X}: Y={prediction[0]}")
  else:
    print("Error: k cannot be greater than N.")

if __name__== "__main__":
  main()
