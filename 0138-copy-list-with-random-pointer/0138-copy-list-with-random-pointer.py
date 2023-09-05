# Approach-2:
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}
        iter = head
        while iter: # Create an empty lists
            oldToCopy[iter] = Node(iter.val) # Creating new node
            iter = iter.next
        
        iter = head
        while iter:
            new_node = oldToCopy[iter]
            new_node.next = oldToCopy[iter.next]
            new_node.random = oldToCopy[iter.random]
            iter = iter.next
            
        return oldToCopy[head]        