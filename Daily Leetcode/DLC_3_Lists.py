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


4. MERGE TWO SORTED LISTS:

  def mergeTwoLists(self, l1, l2):
    dummy = temp = ListNode(0)
    while l1 and l2:
      if l1.val < l2.val:
        temp.next = l1
        l1 = l1.next
      else:
        temp.next = l2
        l2 = l2.next
      temp = temp.next
    temp.next = l1 or l2
    return dummy.next

  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      if not l1 or not l2:
          return l1 or l2
      
      if l1.val <= l2.val: #1
          l1.next = self.mergeTwoLists(l1.next, l2)
          return l1
      else: #2
          l2.next = self.mergeTwoLists(l1, l2.next)
          return l2


5. PALINDROME LINKED LIST:

  # def isPalindrome(self, head):
  #     # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
  #     rev = None
  #     # initially slow and fast are the same, starting from head
  #     slow = fast = head
  #     while fast and fast.next:
  #         # fast traverses faster and moves to the end of the list if the length is odd
  #         fast = fast.next.next
  #         # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
  #         rev, rev.next, slow = slow, rev, slow.next
  #     if fast:
  #       # fast is at the end, move slow one step further for comparison(cross middle one)
  #         slow = slow.next
  #     # compare the reversed first half with the second half
  #     while rev and rev.val == slow.val:
  #         slow = slow.next
  #         rev = rev.next
  #     # if equivalent then rev become None, return True; otherwise return False 
  #     return not rev

  def isPalindrome(self, head):
    vals = []
    while head:
        vals += head.val,
        head = head.next
    return vals == vals[::-1]


6. 