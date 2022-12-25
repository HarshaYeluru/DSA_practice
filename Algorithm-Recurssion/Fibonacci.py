def fibonacciIter(n):
  a = 0
  b = 1
  for num in range(n):
    a, b = b, a+b
  return a

def fibonacciRec(n):
  if n < 2:
    return n
  return fibonacciRec(n-1) + fibonacciRec(n-2)

print(fibonacciIter(5))
print(fibonacciRec(5))