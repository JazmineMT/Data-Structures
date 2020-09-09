"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
	def __init__(self, value, prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next
  
  
	def get_value(self):
		return self.value
	
	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next




"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode( value, None , None)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        elif self.length == 1:
            head = self.head
            self.tail = None
            self.head = None
            self.length = 0
            return head.value
        else:
            self_head = self.head
            next_head = self.head.next
            next_head.prev = None
            self.head = next_head
            self.length = self.length -1
            return self_head.value        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None , None)
        if not self.head and self.tail:
            self.tail = new_node
            self.head = new_node
            self.length += 1
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1 
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length is None:
            return None
        elif self.length == 1:
            tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return tail.value
        else:
            tail1 = self.tail
            tail2 = self.tail.prev
            self.tail.prev = None
            self.tail = tail2
            self.length = self.length -1
            return tail1.value        
            
        
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)
            
                
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
        
           

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.head is node:
            self.head = node.next
            self.length -= 1
        elif self.tail is node:
            self.tail = node.prev
            self.length -= 1
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = None
            node.prev = None
            self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        
        
        max_value = self.head.get_value()
        current = self.head.get_next()
        
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
                
                
            
            
        return max_value
        