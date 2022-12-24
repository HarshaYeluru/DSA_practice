class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class linkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.length = 1

  def printLL(self):
    curr = self.head
    out = ""
    while True:
      out = out + str(curr.value) + " --> "
      if curr.next == None:
        break
      curr = curr.next
    out += str(None)
    print("Linked List has %d nodes"%(self.length))
    print("Linked List: %s"%(out))
  
  def append(self, value):
    curr = self.head
    newNode = Node(value)
    while curr.next == None:
      curr.next = newNode
      curr.next.next = None
      self.length +=1

  def prepend(self, value):
    newNode = Node(value)
    newNode.next=self.head
    self.head = newNode
    self.length += 1

  def insert(self, value, pos):
    if pos > self.length:
      print("Position greater than Length of LL")
      return False
    newNode = Node(value)
    curr = self.head
    for ptr in range(pos-1):
      curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    self.length += 1

  def remove(self, pos):
    if pos > self.length:
      print("Position given is greater than length of LL")
      return False
    curr = self.head
    for ptr in range(pos-1):
      curr = curr.next
    curr.next = curr.next.next
    self.length -= 1

  def search(self, value):
    curr = self.head
    while curr != None:
      if curr.value == value:
        print("Found %s"%(value))
        return True
      curr = curr.next
    print("%s not in LL"%(value))
    

myLL = linkedList(10)
myLL.printLL()
myLL.append(5)
myLL.printLL()
myLL.prepend(16)
myLL.printLL()
myLL.insert(25, 2)
myLL.printLL()
myLL.remove(2)
myLL.printLL()
myLL.insert(25, 3)
myLL.printLL()
myLL.search(35)
