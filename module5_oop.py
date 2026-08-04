"""
Assignment #5.2: Getting (more) familiar with python

The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.

The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)
"""

class NumberCollection:
  def __initialize__(self):
    # Data initialization
    self.numbers[]

  def insert(self, value):
    # Data insertion
    self.numbers.append(value)

  def search(self, value):
    # Data search. Returns index of the first occurrence of "value" or -1 if not found.
    for index, number in enumerate(self,numbers):
      if number == value:
        return index + 1
      return -1

def main():
  N = int(input("Enter a positive integer N: "))

  collection = NumberCollection()

  for i in range(N):
    value = int(input(f"Enter number {i + 1}"))
    collection.insert(value)

  X = int(input("Enter X to search for "))

  result = collection.search(X)
  print(result)

if __name__ == "__main__":
  main()
