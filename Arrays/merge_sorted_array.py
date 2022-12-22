#https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12309362#overview
def mergeSortedArray(arr1, arr2):
  if len(arr1) == 0 or len(arr2) == 0:
    print(arr1 + arr2)
  else:
    l1 = 0
    l2 = 0
    out_arr = []
    while l1 < len(arr1) and l2 < len(arr2):
      if arr1[l1] < arr2[l2]:
        out_arr.append(arr1[l1])
        l1+=1
      else:
        out_arr.append(arr2[l2])
        l2+=1
    print(out_arr + arr1[l1:] + arr2[l2:])
    

arr1 = [0,3,4,31]
arr2 = [4,6,30]
arr3 = []
mergeSortedArray(arr1, arr2) # Returns [0, 3, 4, 4, 6, 30, 31]
mergeSortedArray(arr1, arr3) # Returns [0, 3, 4, 31]
