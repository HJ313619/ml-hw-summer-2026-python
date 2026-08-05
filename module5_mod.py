class NumberCollection:
  def __init__(self):
    # Data initialization
    self.numbers = []

  def insert(self, value):
    # Data insertion
    self.numbers.append(value)

  def search(self, value):
    # Data search. Returns index of the first occurrence of "value" or -1 if not found.
    for index, number in enumerate(self.numbers):
      if number == value:
        return index + 1
    return -1
