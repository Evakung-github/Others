
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
