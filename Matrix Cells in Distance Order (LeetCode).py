class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        matrix = []
        output = []
        d = {}
        for i in range(rows):
            for j in range(cols):
                matrix.append([i,j])
        for i in matrix:
            dist = abs(rCenter - i[0]) + abs(cCenter - i[1])
            if dist in d:
                d[dist].append(i)
            else:
                d[dist] = []
                d[dist].append(i)
        for i in range(len(d)):
            for j in d[i]:
                output.append(j)
        return output