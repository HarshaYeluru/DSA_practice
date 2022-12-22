def two_sum(nums, target):
  temp_dict = {}
  for num in nums:
    if num in temp_dict :
      return num, target-num
    temp_dict[target-num] = True

def two_sum_index(nums, target):
  temp_dict = {}
  for index, num in enumerate(nums):
    if num in temp_dict :
      return index, temp_dict[num]
    temp_dict[target-num] = index

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target)) # Returns numbers
print(two_sum_index(nums, target)) # Returns indices