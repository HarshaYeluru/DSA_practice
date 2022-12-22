def containsDuplicate(nums):
  dict = {}
  for num in nums:
    if num in dict:
      return True
    else:
      dict[num] = True
  return False

nums = [1,2,3,4]
print(containsDuplicate(nums))