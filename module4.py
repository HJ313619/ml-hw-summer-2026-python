"""
Assignment #4.2: Getting familiar with github and python

The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
"""
                                     
def find_index(numbers, x):
  """ Return the index of X in input numbers, or -1 if not found."""
  if x in numbers:
    return numbers.index(x) + 1
  return -1

def main():
  """Main program."""
  # Ask the user how many numbers they will enter.
  N = int(input("Please enter a positive integer N for how many input numbers: "))

  # Ask the user to provide N numbers (one by one).
  numbers = []
  for i in range (N):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

  # Ask the user for the input X.
  X = int(input(f"Please enter an integer X to check if it's among the {N} numbers: "))

  # Print the result: index of X if found, or -1 if not found.
  result = find_index(numbers, X)
  print (result)

if __name__ == "__main__":
  main()
