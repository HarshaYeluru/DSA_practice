numbers = [5, 3, 8, 6, 1, 2, 7, 4]
def selectionSort(nums):
  for ptr1 in range(len(nums)):
    s_index = ptr1
    for ptr2 in range(ptr1+1, len(nums)):
      if nums[ptr2] < nums[s_index]:
        s_index = ptr2
    nums[s_index], nums[ptr1] = nums[ptr1], nums[s_index]
  print(nums)
      
      

selectionSort(numbers)