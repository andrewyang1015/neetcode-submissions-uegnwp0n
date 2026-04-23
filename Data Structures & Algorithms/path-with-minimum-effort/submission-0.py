class DSU:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
    
    def find_rep(self, i):
        if self.parent[i] == i: return i

        self.parent[i] = self.find_rep(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        u, v = self.find_rep(i), self.find_rep(j)

        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[v] > self.rank[u]:
            self.parent[u] = v
        else:
            self.parent[v] = u
            self.rank[u] += 1


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        disjoint_set = DSU(m * n)

        if m == 1 and n == 1: return 0

        edge_lst = []
        for row in range(m):
            for col in range(n):
                if row > 0:
                    difference = abs(heights[row - 1][col] - heights[row][col])
                    idx_start, idx_end = row * n + col, (row - 1) * n + col
                    edge_lst.append((difference, idx_start, idx_end))
                
                if col > 0:
                    difference = abs(heights[row][col - 1] - heights[row][col])
                    idx_start, idx_end = row * n + col, row * n + col - 1
                    edge_lst.append((difference, idx_start, idx_end))
        
        edge_lst.sort()

        for effort, idx_start, idx_end in edge_lst:
            u = disjoint_set.find_rep(idx_start)
            v = disjoint_set.find_rep(idx_end)

            if u != v: disjoint_set.union(u, v)

            if disjoint_set.find_rep(0) == disjoint_set.find_rep(m * n - 1): return effort

        return -1

'''


Time: 

Number of traversals only number of different weights or m * n

sort is m * n log (m * n)
Union is inverse ackerman aka constant

Overall is O(m * n log (m * n))


'''