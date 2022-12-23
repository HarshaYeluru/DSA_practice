class HashTable:
  def __init__(self, size):
    self.size = size
    self.myTable = [[] for i in range(size)]

  def getHash(self, key):
    sum = 0
    for char in key:
      sum += ord(char)
    return sum%self.size

  def getTable(self):
    out_value = ""
    for item in self.myTable:
      if item != []:
        for sub_item in item:
          out_value = out_value + sub_item[0] + "--->" + sub_item[1] + "\n"
    return out_value

  def set(self, key, value):
    self.myTable[self.getHash(key)].append([key,value])

  def get(self, key):
    address = self.myTable[self.getHash(key)]
    if address == []:
      return None
    for item in address:
      if item[0] == key:
        return item[1]

  def delete(self, key):
    address = self.myTable[self.getHash(key)]
    for item in address:
      if item[0] == key:
        address.remove(item)

  def keys(self):
    key_list=[]
    for item in self.myTable:
      for sub_item in item:
        key_list.append(sub_item[0])
    return key_list

  def values(self):
    value_list=[]
    for item in self.myTable:
      for sub_item in item:
        value_list.append(sub_item[1])
    return value_list

table1 = HashTable(5)
table1.set("Name", "Harsha")
table1.set("Profession", "Software")
table1.set("Surname", "Yeluru")
table1.set("Mobile", "1234567")
print(table1.get("Surname") + " " + table1.get("Name"))
print("***********")
print(table1.getTable())
table1.delete("Mobile")
print("***********")
print(table1.getTable())
print("***********")
print(table1.keys())
print("***********")
print(table1.values())