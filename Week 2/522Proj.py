1. STRENGTHS OF LINKED LIST:

  1. Fast operations a both ends (head and tail)
  2. They can grow and shrink to accomodate the data


2. WHAT IS THE PRIMARY WEAKNESS OF A LINKED LIST DATA STRUCTURE:

  1. Costly search operations


3. ADD A VALUE TO A SORTED LINKED LIST (WHILE RETAINING SORTED):

  def insertValueIntoSortedLinkedList(head, value):
    new_Node = ListNode(value)
    # Empty Array
    if head == None:
        return new_Node
    #If value is less than current head replace head
    if value < head.value:
        new_Node.next = head
        return new_Node
    
    node = head
    while node.next != None:
        if value < node.next.value:
            break
        node = node.next

    new_Node.next = node.next
    node.next = new_Node

    return head


4. MERGE TWO SORTED SINGLY LL'S (RETAIN SORT):

  def mergeTwoLinkedLists(head1, head2): 
  
    temp = None
  
    if head1 is None: 
        return head2 
    if head2 is None: 
        return head1 

    if head1.value <= head2.value: 
  
        # assign temp to List1's value 
        temp = head1 
  
        # Again check List1's value is smaller or equal List2's  
        # value and call mergeLists function. 
        temp.next = mergeTwoLinkedLists(head1.next, head2) 
          
    else: 
        temp = head2 
        temp.next = mergeTwoLinkedLists(head1, head2.next) 

    return temp 


5. REVERSE NODES IN K-GROUP:

  ListNode* reverseKGroup(ListNode* head, int k) {
    if (!head || !head->next || k <= 1) {
        return head;
    }
    
    ListNode dummy(0), *prev = &dummy;
    prev->next = head;
    
    while (true) {
        ListNode* it = prev->next;
        int count = 0;
        while (it) {
            ++count;
            if (count == k) {
                break;
            }
            it = it->next;
        }
        if (count < k) {
            break;
        }
        
        ListNode* nextPrev = prev->next;
        
        ListNode* prev2 = NULL, *cur = prev->next, *next = NULL;
        for (int i = 0; i < k; ++i) {
            next = cur->next;
            cur->next = prev2;
            prev2 = cur;
            cur = next;
        }
        
        prev->next = prev2;
        nextPrev->next = cur;
        
        prev = nextPrev;
    }
    
    return dummy.next;
  }


  ---


  function reverseNodesInKGroups(l, k) {
      return calculate(l, k , Math.floor(sizeOf(l)/k))
  }
  const calculate = (l, k, numberOfInteractions) => {
      if(numberOfInteractions===0) { return l }
      let first = l
      let previous = l
      let current = l
      let lostLink = current.next 
      for(let i = 0; i < k-1; i++){
          current = lostLink
          lostLink = current.next
          current.next = previous
          previous = current
      }
      first.next = calculate(lostLink, k, numberOfInteractions-1)
      return current
  }
  const sizeOf = (l) => {
      let size = 0
      while(l){ size++; l = l.next }
      return size
  }