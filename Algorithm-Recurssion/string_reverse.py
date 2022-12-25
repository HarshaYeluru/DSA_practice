def strReverseRecurssion(input):
  while len(input) != 0:
    return strReverseRecurssion(input[1:]) + input[0]
  return input

def strReverseIteration(input_str):
  input = list(input_str)
  ptr2 = len(input) - 1
  for ptr1 in range(len(input)):
    if ptr1 <= ptr2:
      print(ptr1, ptr2)
      input[ptr1], input[ptr2] = input[ptr2], input[ptr1]
      ptr2 -= 1
  print(input)
    

print(strReverseRecurssion("Hey there!"))
#strReverseIteration("Harsha")