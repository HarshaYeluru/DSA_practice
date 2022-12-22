# https://coderbyte.com/editor/Longest%20Word:Python3

import re
def LongestWord(sen):

  longWord = ""
  def getLength(word):
    return len(normal_word)

  for word in sen.split():
    normal_word = re.sub("[^A-Za-z0-9]", "", word,0,re.IGNORECASE)
    if getLength(normal_word) > len(longWord):
      longWord = normal_word
  return longWord

# keep this function call here 
print(LongestWord("I love123 dogss!!!"))