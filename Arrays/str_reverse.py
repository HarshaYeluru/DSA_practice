#https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12308750#overview
def reverseString(input_str):
  print("Input: %s"%(input_str))
  output_str = ""
  for char in input_str:
    output_str = char+output_str
  print("Output: %s"%(output_str))


reverseString("Hi My name is Harsha")