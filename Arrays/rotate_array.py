#https://leetcode.com/problems/rotate-array/description/
def rotate(nums, k):
  # Using O(n) space complexity
  out_nums = [1] * len(nums)
  for idx in range(len(nums)):
    out_nums[idx] = nums[idx-k]
  return(out_nums)

nums=[1,2,3,4,5,6,7]
k=3
print(rotate(nums, k))