class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.arr = [None]*self.size
        
    def find_index(self,key):
        return key % self.size
                
    def put(self, key: int, value: int) -> None:
        idx = self.find_index(key)
        if self.arr[idx] is None:
            self.arr[idx] = ListNode((key, value), None)
            return 
        node = self.arr[idx]
        while node:
            if node.val[0]==key:
                node.val = (key, value)
                return
            node = node.next
        self.arr[idx] = ListNode((key, value), self.arr[idx])
        
    def get(self, key: int) -> int:
        idx = self.find_index(key)
        if self.arr[idx] is None: return -1
        node = self.arr[idx]
        while node:
            if node.val[0]==key:
                return node.val[1]
            node = node.next
        return -1
            
    def remove(self, key: int) -> None:
        idx = self.find_index(key)
        if self.arr[idx] is None: return
        node = self.arr[idx]
        if node.val[0]==key:
            self.arr[idx] = node.next
            return
        first, second = node, node.next
        while second:
            if second.val[0]==key:
                first.next = second.next
                return
            first, second = first.next, second.next