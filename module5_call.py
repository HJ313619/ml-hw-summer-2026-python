from module5_mod import NumberCollection

def main():
  N = int(input("Enter a positive integer N for how many input numbers: "))

  collection = NumberCollection()

  for i in range(N):
    value = int(input(f"Enter number {i + 1}: "))
    collection.insert(value)

  X = int(input("Enter X to search for "))

  result = collection.search(X)
  print(result)

if __name__ == "__main__":
  main()
