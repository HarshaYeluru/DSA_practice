nums = [2,5,1,2,3,5,1,2,4]
#nums = [1,2,3,4,5]
#nums = [1]
def recurringCharacter(nums):
  # Brute Force O(n^2)
  for ptr1 in range(len(nums)):
    for ptr2 in range(ptr1+1, len(nums)):
      if nums[ptr1] == nums[ptr2]:
        return nums[ptr1]
  return False

def recurringCharacter2(nums):
  #O(n)
  numDict = {}
  for num in nums:
    if num in numDict:
      return num
    else:
      numDict[num] = True
  return False

print(recurringCharacter(nums))
print(recurringCharacter2(nums))
