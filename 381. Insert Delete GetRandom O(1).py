'''
A hashmap and an array are created. Hashmap tracks the position of value in the array, and we can also use array to track the appearance in the hashmap.
The main trick is to swap the last element and the element need to be removed, and then we can delete the last element at O(1) cost.
Afterwards, we need to update the position of the original last element in the hashmap to its current position.
Therefore, that's why we need to record its space in the value of the hashmap.
ref: https://www.youtube.com/watch?v=mRTgft9sBhA
'''





import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.dict:
            self.dict[val] = [len(self.array)]
            self.array.append([val,0])
            return True
        else:
            self.dict[val].append(len(self.array))
            self.array.append([val,len(self.dict[val])-1])
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.dict:
            if not self.dict[val]:
                return False
            else:
                n = self.dict[val][-1]
                
                self.dict[self.array[-1][0]][self.array[-1][1]] = n
                n = self.dict[val].pop()
                self.array[n], self.array[-1] = self.array[-1],self.array[n]
                self.array.pop()

                return True
                

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        n = random.randint(0,len(self.array)-1)
        return self.array[n][0]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
