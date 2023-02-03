class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""]*numRows
        direction = "down"
        row = 0
        for c in s:
            rows[row] += c
            match direction:
                case "down":
                    if row + 1 == numRows:
                        row -= 1
                        direction = "up"
                    else:
                        row += 1
                case "up":
                    if row - 1 == -1:
                        row += 1
                        direction = "down"
                    else:
                        row -= 1
        return "".join(rows)  


            
        