import random

class RandomizedSet:

    def __init__(self):
       self.arr = [] 
       self.my_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.my_dict:
            return False 
        self.my_dict[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.my_dict:
            return False 
        val_idx = self.my_dict[val]
        tmp = self.arr[-1]
        self.my_dict[tmp] = val_idx
        self.arr[-1] = val 
        self.arr[val_idx] = tmp 
        # the idea is removing the array at the end is O(1) time
        self.arr.pop()
        del self.my_dict[val]
        return True 


    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()