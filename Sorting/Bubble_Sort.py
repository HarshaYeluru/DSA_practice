numbers = [1, 5, 3, 8, 6, 2, 7, 4]
def bubbleSort(numbers):
  sorted = True
  for num in range(len(numbers)):
    if sorted: 
      sorted = False
      for idx in range(len(numbers)-num-1):
        if numbers[idx] > numbers[idx+1]:
          sorted = True
          numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
    else:
      break
  return numbers

print(bubbleSort(numbers))