class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class linkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.length = 1

  def printLL(self):
    curr_node = self.head
    if self.head is None:
        print("Empty Linked List!")
    else:
        while curr_node is not None:
            print(curr_node.value, end=" ")
            curr_node = curr_node.next
    print()
  
  def append(self, value):
    curr = self.head
    newNode = Node(value)
    while curr.next != None:
      curr = curr.next
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

  def reverse(self):
    if self.length == 1:
      return self.head
    ptr1 = self.head
    ptr2 = self.head.next
    while ptr2 is not None:
      temp = ptr2.next
      ptr2.next = ptr1
      ptr1 = ptr2
      ptr2 = temp
    self.head.next = None
    self.head = ptr1
    self.printLL()
      

myLL = linkedList(1)
myLL.append(2)
myLL.append(3)
myLL.append(4)
myLL.append(5)
myLL.printLL()
myLL.reverse()