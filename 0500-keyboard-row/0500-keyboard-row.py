class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row, second_row, third_row = ("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        def possible(word, row):
            i = 1
            while i < len(word):
                if word[i].lower() not in row : return False
                i += 1
            return True
        res = []
        for word in words:
            if word[0].lower() in first_row:
                if possible(word, first_row): res.append(word) 
            elif word[0].lower() in second_row:
                if possible(word, second_row): res.append(word)       
            elif word[0].lower() in third_row:
                if possible(word, third_row): res.append(word)
        return res
                    
            
        