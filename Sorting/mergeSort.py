nums = [8, 5, 7, 1, 4, 2, 6, 3, 9]
def mergeSort(list):
  if len(list) == 1:
    return list

  left = list[:int(len(list)/2)]
  right = list[int(len(list)/2):]   
  return merge(
    mergeSort(left),
    mergeSort(right)
  )

def merge(left, right):
  i = 0
  j = 0
  newList = []
  print(left, right)

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      newList.append(left[i])
      i+=1
    else:
      newList.append(right[j])
      j+=1

  while i < len(left):
    newList.append(left[i])
    i+=1

  while j < len(right):
    newList.append(right[j])
    j+=1

  return newList

print(mergeSort(nums))