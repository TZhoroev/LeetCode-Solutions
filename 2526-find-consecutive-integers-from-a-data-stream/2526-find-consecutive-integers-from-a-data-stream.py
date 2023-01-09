class DataStream:
    def __init__(self, value: int, k: int):       
        self.value = value
        self.k = self.orig = k 

    def consec(self, num: int) -> bool:
        if num == self.value: self.k -= 1
        else: self.k = self.orig
        return self.k <= 0

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)