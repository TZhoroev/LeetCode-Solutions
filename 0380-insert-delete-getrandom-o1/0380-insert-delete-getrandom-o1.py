import random
class RandomizedSet:

    def __init__(self):
        self.array = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.array:
            self.array[val] = True
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.array:
            del self.array[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.array.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()