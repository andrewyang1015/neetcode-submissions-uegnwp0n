class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist_to = [float("inf")] * n
        visited = [False] * n

        min_cost = 0
        edge_ct = 0

        min_dist_to[0] = 0

        while edge_ct < n:
            min_edge = float("inf")
            min_node = -1
            for node in range(n):
                if not visited[node] and min_edge > min_dist_to[node]:
                    min_edge = min_dist_to[node]
                    min_node = node

            min_cost += min_edge
            edge_ct += 1
            visited[min_node] = True 

            # Update adjacent nodes of current
            for neighbor in range(n):
                next_weight = abs(points[min_node][0] - points[neighbor][0]) + abs(points[min_node][1] - points[neighbor][1])
                if neighbor != min_node and not visited[neighbor] and min_dist_to[neighbor] > next_weight:
                    min_dist_to[neighbor] = next_weight
        
        return min_cost