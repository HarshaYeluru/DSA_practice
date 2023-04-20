nums = [11, 9, 29, 7, 2, 15, 28]
def partition(nums, start, end):
  pivot_index = start
  pivot = nums[pivot_index]
  while start < end:
    while start < len(nums) and nums[start] <= pivot:
      start += 1
    while nums[end] > pivot:
      end -= 1

    if start < end:
      nums[start], nums[end] = nums[end], nums[start]

  nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

  return end
def quickSort(nums, start, end):
  if start < end:
    pi = partition(nums, start, end)
    quickSort(nums, start, pi-1)
    quickSort(nums, pi+1, end)
    

quickSort(nums, 0, len(nums)-1)
print(nums)
# Test change
