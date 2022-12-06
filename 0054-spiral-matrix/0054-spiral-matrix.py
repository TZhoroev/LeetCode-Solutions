class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        left, right, up, down = 0, len(matrix[0]) -1, 0, len(matrix) - 1
        direction = "right"
        res = []
        while (left <= right) or (up <= down):
            match direction:
                case "right":
                    while j < right:
                        res.append(matrix[i][j])
                        j += 1
                    if up == down:
                        res.append(matrix[i][j])
                        return res
                    direction = "down"
                    up +=1
                case "down":
                    while i < down:
                        res.append(matrix[i][j])
                        i += 1
                    if left == right:
                        res.append(matrix[i][j])
                        return res
                    direction = "left"
                    right -= 1
                case "left":
                    while j > left:
                        res.append(matrix[i][j])
                        j -= 1
                    if up == down:
                        res.append(matrix[i][j])
                        return res
                    direction = "up"
                    down -= 1 
                case "up":
                    while i > up:
                        res.append(matrix[i][j])
                        i -= 1
                    if left == right:
                        res.append(matrix[i][j])
                        return res
                    direction = "right"
                    left +=1
        return res


        