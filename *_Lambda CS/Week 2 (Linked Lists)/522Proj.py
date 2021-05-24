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

--------

  def reverseNodesInKGroups(l, k):
    # go in groups of k
    # check if we need to reverse the next k nodes -- 
    # if we're at the end and we have fewer than k nodes left, then we don't need to reverse
    current_node = l
    prev_group_tail = None  # This is the tail of the previous group, we'll need it to connect it to the next group
    while True:   
        if should_reverse(current_node, k):
            # reverse k nodes
            # The first node of the original group becomes the tail of the reversed group; 
            # save it so that we have access to it later since we'll need it to connect to the next group
            cur_group_tail = current_node  
            prev = None
            for i in range(k): 
                next_node = current_node.next
                # set current.next = prev
                current_node.next = prev
                # update prev = current
                prev = current_node
                # set current = next
                current_node = next_node
            # link the previous group to the current reversed group
            # At this point, prev is the head of the reversed group
            if prev_group_tail: 
                prev_group_tail.next = prev
            else: 
                # if there is no previous group, set the head (l) to the new head of the reversed group
                l = prev
            prev_group_tail = cur_group_tail  # save the tail 
        else: 
            # There are fewer than k nodes left; they should remain as-is. 
            # Connect the previous group to the rest of the list
            prev_group_tail.next = current_node
            break
    return l
​
def should_reverse(current_node, k): 
    # check if there are at least k nodes left in the list
    count = 0
    while current_node is not None: 
        count += 1
        current_node = current_node.next
        if count == k: 
            return True
	return False



------ recursive version

def reverse_nodes_in_k_groups(l, k):
	current = l
	
	# advance k nodes to see if this sub-list is long enough
	for _ in range(k):
		if not current:
			return l
		current = current.next
		
	# set a return value reference and reset our `current` reference
	rv, current = l, l.next 
	
	# swap next k nodes 
	for _ in range(k - 1):
		current.next, current, rv = rv, current.next, current
		
	# recurse on the next section of the linked list 
	l.next = reverse_nodes_in_k_groups(current, k)
	
	return rv