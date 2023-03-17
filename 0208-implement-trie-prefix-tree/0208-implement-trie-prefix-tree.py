class Trie:
    def __init__(self):
        self.trie = defaultdict(lambda: {})
        self.total = 1
    def insert(self, word: str) -> None:
        word += "#"
        current_node = 0
        for symbol in word:
            if symbol in self.trie[current_node].keys():
                current_node = self.trie[current_node][symbol]
            else:
                self.trie[current_node][symbol] = self.total
                current_node = self.total
                self.total += 1

    def search(self, word: str) -> bool:
        word += "#"
        current_node = 0
        for symbol in word:
            if symbol not in self.trie[current_node].keys():
                return False
            current_node = self.trie[current_node][symbol]
        return True
        
    def startsWith(self, prefix: str) -> bool:
        current_node = 0
        for symbol in prefix:
            if symbol not in self.trie[current_node].keys():
                return False
            current_node = self.trie[current_node][symbol]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)