from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[float("inf") for _ in range(n)] for _ in range(n)]
        costs = [float("inf")] * n

        for start, end, price in flights:
            graph[start][end] = price
        
        # We only start having stops for paths with > 2 nodes
        queue = deque([(0, src, 0)]) # Price, city, steps
        costs[src] = 0

        while queue:
            price, city, step = queue.popleft()

            if step > k: continue # over k stops

            for neighbor in range(n):
                weight = graph[city][neighbor]
                next_cst = price + weight
                if neighbor != city and weight != float("inf") and next_cst < costs[neighbor]:
                    costs[neighbor] = next_cst
                    queue.append((next_cst, neighbor, step + 1))
        
        return costs[dst] if costs[dst] != float("inf") else -1
