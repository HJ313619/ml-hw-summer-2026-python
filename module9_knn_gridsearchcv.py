"""
Assignment #9.3: Scikit-learn Classification

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.

Then the program asks the user for input M (positive integer) and reads it.

Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.

In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks). 

Note: you can try the following range of k: 1 <= k <= 10.
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, KFold
 
 
def read_int(prompt):
    # Read a positive integer from the user, re-prompting on bad input.
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid integer, please try again.")
 
 
def read_float(prompt):
    # Read a real number (float) from the user, re-prompting on bad input.
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid real number, please try again.")
 
 
def read_nonneg_int(prompt):
    # Read a non-negative integer (class label) from the user.
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid integer, please try again.")
 
 
def read_pairs(count, set_name):
    """
    Reads `count` (x, y) pairs one by one from the user.
    x -> real number (input feature)
    y -> non-negative integer (class label)
 
    Returns two NumPy arrays: X (shape (count, 1)), y (shape (count,))
    """
    xs = np.empty(count, dtype=float)
    ys = np.empty(count, dtype=int)
 
    for i in range(count):
        print(f"--- {set_name} pair {i + 1}/{count} ---")
        x_val = read_float(f"  Enter x_{i + 1} (real number): ")
        y_val = read_nonneg_int(f"  Enter y_{i + 1} (non-negative integer class label): ")
        xs[i] = x_val
        ys[i] = y_val
 
    # scikit-learn expects a 2D array of shape (n_samples, n_features)
    X = xs.reshape(-1, 1)
    return X, ys
 
 
def main():
    print("=== kNN Classifier with Hyperparameter Search (GridSearchCV) ===\n")
 
    # ---- Training set ----
    print("Training set (TrainS)")
    N = read_int("Enter N (number of training pairs, positive integer): ")
    X_train, y_train = read_pairs(N, "TrainS")
 
    # ---- Test set ----
    print("\nTest set (TestS)")
    M = read_int("Enter M (number of test pairs, positive integer): ")
    X_test, y_test = read_pairs(M, "TestS")
 
    """
    Cross-validation folds: GridSearchCV needs cv >= 2, and each fold must have at least as many training samples as the largest k tried.
    We pick a safe number of folds based on how much data we have.
    """
    cv_folds = min(5, N)
    if cv_folds < 2:
        cv_folds = 2 if N >= 2 else None
 
    """
    ---- Hyperparameter grid: k in [1, 10] ----
    kNN requires k <= number of samples used to FIT each model. During cross-validation the fit set is smaller than N (one fold held out), so we cap k at the smallest training-fold size that KFold will produce, not just at N itself.
    """
    if cv_folds is not None and N >= 2:
        max_test_fold_size = -(-N // cv_folds)  # ceil(N / cv_folds)
        min_train_fold_size = N - max_test_fold_size
        k_upper_bound = min(N, min_train_fold_size)
    else:
        k_upper_bound = N
 
    k_candidates = [k for k in range(1, 11) if k <= k_upper_bound]
    if not k_candidates:
        k_candidates = [1]
 
    print("\nRunning hyperparameter search (GridSearchCV) over k =", k_candidates)
 
    knn = KNeighborsClassifier()
    param_grid = {"n_neighbors": k_candidates}
 
    if cv_folds is not None and N >= 2:
        # Plain KFold (not stratified) is used on purpose: with small,
        # user-typed datasets we cannot guarantee every class has enough
        # members for stratified folds, so a simple shuffled KFold keeps
        # the search robust regardless of class distribution.
        cv_splitter = KFold(n_splits=cv_folds, shuffle=True, random_state=42)
        grid_search = GridSearchCV(
            estimator=knn,
            param_grid=param_grid,
            cv=cv_splitter,
            scoring="accuracy",
        )
        grid_search.fit(X_train, y_train)
        best_k = grid_search.best_params_["n_neighbors"]
        best_model = grid_search.best_estimator_
    else:
        # Fallback for a single training sample: cannot cross-validate,
        # just use the only feasible k.
        best_k = k_candidates[0]
        best_model = KNeighborsClassifier(n_neighbors=best_k)
        best_model.fit(X_train, y_train)
 
    # Ensure the best model is fit on the FULL training set before testing
    best_model = KNeighborsClassifier(n_neighbors=best_k)
    best_model.fit(X_train, y_train)
 
    # ---- Evaluate on TestS ----
    test_accuracy = best_model.score(X_test, y_test)
 
    print("\n=== Results ===")
    print(f"Best k: {best_k}")
    print(f"Test accuracy: {test_accuracy:.4f}")
 
 
if __name__ == "__main__":
    main()
