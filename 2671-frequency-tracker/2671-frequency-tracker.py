class FrequencyTracker:

    def __init__(self):
        self.array = defaultdict(lambda: 0)
        self.frequencies = defaultdict(lambda: 0)

    def add(self, number: int) -> None:
        self.frequencies[self.array[number]] -=1
        self.array[number] += 1
        self.frequencies[self.array[number]] +=1
        

    def deleteOne(self, number: int) -> None:
        self.frequencies[self.array[number]] -=1
        self.array[number] -= 1
        self.frequencies[self.array[number]] +=1
        if self.array[number] <= 0:
            del self.array[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)