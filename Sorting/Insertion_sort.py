nums = [8, 5, 7, 1, 4, 2, 6, 3]
def insertionSort(nums):
  print(nums)
  for ptr1 in range(1, len(nums)):
    while ptr1 > 0 and nums[ptr1] < nums[ptr1-1]:
        nums[ptr1], nums[ptr1-1] = nums[ptr1-1], nums[ptr1]
        ptr1 -= 1

  print(nums)

insertionSort(nums)