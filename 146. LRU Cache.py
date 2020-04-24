'''
This problem is sloved by double-linked lists and hash table.
Hash table helps us to find whether the element is in the cache for O(1) time complexity.
Link list help us to track the order (recently used) and remove the items in O(1) time complexity.
If using array, it requires O(N) time to remove.

The idea is to use hash table to track the node, 
and each node has prev and next features so that we can access to its previous node and next node when deleting it.
 Also we need to know the head and the tail of the linked list to avoid unnecessary traversal of the linked lists.
'''
class doubleLink():
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.link = doubleLink(-1,-1)
        self.tail = self.link

    def get(self, key: int) -> int:
        if key in self.dict:
            if self.dict[key].next:
                prev = self.dict[key].prev
                
                prev.next = self.dict[key].next
                self.dict[key].next.prev = prev
                
                self.dict[key].next = None
                self.tail.next = self.dict[key]
                self.dict[key].prev = self.tail
                self.tail = self.dict[key]
            return self.dict[key].val
        else:
            return -1
                
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            if self.dict[key].next:
                prev = self.dict[key].prev
                
                prev.next = self.dict[key].next
                self.dict[key].next.prev = prev
                
                self.dict[key].next = None
                self.tail.next = self.dict[key]
                self.dict[key].prev = self.tail
                self.tail = self.dict[key]
                
            self.dict[key].val = value
        else:
            if self.capacity==0:
                self.capacity += 1
                rm = self.link.next.key
                if self.dict[rm].next:
                    self.link.next = self.dict[rm].next
                    self.dict[rm].next.prev = self.link
                
                del self.dict[rm]

            
            self.capacity-=1
            self.dict[key] = doubleLink(key,value)
            self.tail.next = self.dict[key]
            self.dict[key].prev = self.tail
            self.tail = self.dict[key]
            
        
        #print(self.link.next.val)
            
            
        
        

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
