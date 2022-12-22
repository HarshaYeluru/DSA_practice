def maxSubarray(nums):
  #Brute force method --> O(n^2)
  length = len(nums)
  max = nums[0]
  for num1 in range(length):
    sum = 0
    for num2 in range(num1, length):
      sum += nums[num2]
      if sum > max:
        max = sum
  return max

def maxSubarray2(nums):
  #O(n)
  if not nums:
      return 0

  curSum = maxSum = nums[0]
  for num in nums[1:]:
      curSum = max(num, curSum + num)
      maxSum = max(maxSum, curSum)

  return maxSum
    
    
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [5,4,-1,7,8]
#nums=[-1]
nums=[-2,1,-3,4,-1]
print(maxSubarray2(nums))