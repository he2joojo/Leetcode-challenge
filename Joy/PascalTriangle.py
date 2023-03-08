class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]] if numRows == 1 else [[1],[1,1]]
        for i in range(2,numRows) :
            front = result[i-1]
            now = [front[i]+front[i+1] for i in range(len(front)-1)]
            now.insert(0,1)
            now.append(1)
            result.append(now)
        return result
