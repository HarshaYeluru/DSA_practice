class Node:
  def __init__(self, value):
    self.value = value
    self.prev=None
    self.next=None

class DoubleLinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def printList(self):
    curr = self.head
    out_data = str(curr.prev) + "-->"
    while curr != None:
      out_data = out_data + str(curr.value) + "-->"
      curr = curr.next
    out_data += "None"
    print(out_data)

  def printRev(self):
    curr = self.tail
    out_data = "<--" + str(curr.next)
    while curr != None:
      out_data = "<--" + str(curr.value) + out_data
      curr = curr.prev
    out_data = "None" + out_data
    print(out_data)

  def append(self, value):
    newNode = Node(value)
    newNode.prev = self.tail
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1

  def prepend(self, value):
    newNode = Node(value)
    newNode.next = self.head
    self.head.prev = newNode
    self.head = newNode
    self.length += 1
  
  def insertList(self, pos, newList):
    if pos == 0 or pos >= self.length:
      print("Can't append at the beginning or end")
      return False
    for item in newList[::-1]:
      newNode = Node(item)
      curr = self.head
      for ptr in range(pos-1):
        curr = curr.next
      newNode.next = curr.next
      curr.next.prev = newNode
      curr.next = newNode
      newNode.prev = curr
      self.length += 1
        

mydll = DoubleLinkedList(10)
mydll.printList()
mydll.append(15)
mydll.printList()
mydll.prepend(5)
mydll.printList()
mydll.append(20)
mydll.insertList(2, [11,12,13,14])
mydll.printList()
mydll.printRev()