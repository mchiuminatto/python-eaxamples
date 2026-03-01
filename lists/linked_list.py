from node import Node

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  def merge(l1, l2):
    # linked_list_a = a -> c -> x -> z
    # linked_list_b = b -> g -> u

    if l1.head.val < l2.head.val:
      l3 = l1.head
      l1 = l1.head.next
    else:
      l3 = l2.head
      l2 = l2.head.next

    l3c = l3.head
    while l1.head and l2.head:
      if l1.head.val < l2.head.val:
        l3c.next = l1.head
        l1.head = l1.head.next
      else:
        l3c.next = l2.head
        l2.head = l2.head.next

      l3c = l3c.next

    if l1 is not None:
      l3c.next = l1.head
    else:
      l3c.next = l2
    print(l3)
    return l3

    
  def add(self, val):
    new_head = Node(val)
    new_head.next = self.head
    self.head = new_head
    
  def traverse(self):
    head = self.head
    print("Starting traversal from head")
    while head:
      print("visiting node: {0}".format(head.val))
      head = head.next
    print("Traversal complete")
    
  def size(self):
    node_count = 0
    current_node = self.head
    while current_node:
      node_count += 1
      current_node = current_node.next
    return node_count
  
  def __repr__(self):
    text = ''
    head = self.head
    while head:
      text += str(head.val) + ' -> '
      head = head.next
    return text