1. DELETE NODE FROM LIST:

  #MY ATTEMPT:
  # def deleteNode(self, node):
  #       cur_node = self.head
        
  #       prev = None
  #       while cur_node and curr_node =! node:
  #           prev = cur_node
  #           cur_node = cur_node.next
            
  #       if cur_node is None:
  #           return
        
  #       prev = cur_node.next
  #       cur_node = None

  # LC SOLUTION:
  def deleteNode(self, node):
    # You are removing making node the value of the next node and then connecting to next next 
    # In a way this is like deleting node and node next and inserting a node that = node next in their place
    node.val = node.next.val
    node.next = node.next.next

  # https://www.youtube.com/watch?v=gXY_2wsQf3A
  llist = LinkedList()
  llist.append("A")
  llist.append("B")
  llist.append("C")
  llist.append("D")

  def delete_node(self, key):
    #HEAD
    cur_node = self.head

    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None
      return
    #NOT HEAD
    prev = None
    while cur_node and cur_node.data != key:
      prev = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev.next = cur_node.next
    cur_node = None

2. REMOVE NTH NODE FROM THE LIST:

  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Establish dummy list and 2pointers
        dummy = ListNode(0, head)
        left = dummy
        right = head
        #  keep shifting right one and decrement by 1
        while n > 0 and right:
            right = right.next
            n -= 1
        # keep shifting until right reaches end of list
        while right:
            left = left.next
            right = right.next
        # delete the node + return list w/out dummy 
        left.next = left.next.next
        return dummy.next


3. REVERSE A LINKED LIST:

  def reverseList(l) -> ListNode:
    new_l = None
          while l:
              l.next, l, new_l = new_l, l.next, l
          return new_l



