class RandomizedCollection:

    def __init__(self):
        self.array = {}
        self.rnd = True
        

    def insert(self, val: int) -> bool:
        self.rnd = True
        if val not in self.array:
            self.array[val] = 1
            return True
        else:
            self.array[val] += 1
            return False
        

    def remove(self, val: int) -> bool:
        self.rnd = True
        if val in self.array:
            self.array[val] -= 1
            if self.array[val] == 0:
                del self.array[val]
            return True
        return False
        

    def getRandom(self) -> int:
        if self.rnd:
            self.rnd = False
            self.nums = []
            for key, val in self.array.items():
                self.nums.extend([key]*val)
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()