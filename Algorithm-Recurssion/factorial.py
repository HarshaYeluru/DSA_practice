def factorialRecursive(num):
  if num == 2:
    return 2
  return num * factorialRecursive(num-1)

def factorialIterative(num):
  print("Iterative")
  result = 1
  for idx in range(2, num+1):
    result *= idx
  return result

print(factorialIterative(5))
print(factorialRecursive(5))