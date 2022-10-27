class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []
        self.n = 0
        

    def push(self, x: int) -> None:
        self.a.append(x)
        self.n += 1
    def pop(self) -> int:
        self.n -= 1
        if self.b: return self.b.pop()
        elif self.a: 
            while self.a:
                self.b.append(self.a.pop())
            return self.b.pop()
        else: return "Empty queue"

    def peek(self) -> int:
        if self.b: return self.b[-1]
        elif self.a: 
            while self.a:
                self.b.append(self.a.pop())
            return self.b[-1]
        else: return "Empty queue"
    def empty(self) -> bool: return self.n == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()