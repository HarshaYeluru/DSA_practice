#https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(nums):
  #Brute force method
  for num in range(len(nums)):
    for check in range(num+1, len(nums)):
      if nums[num] == nums[check]:
        return True
  return False

def containsDuplicate2(nums):
  #Faster method
  dict = {}
  for num in nums:
    if num in dict:
      return True
    else:
      dict[num] = True
  return False

nums = [1,2,3,4]
print(containsDuplicate2(nums))