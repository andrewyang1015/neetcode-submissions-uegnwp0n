class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        weights = defaultdict(int)

        for u, v, w in times:
            graph[u - 1].append(v - 1)
            weights[(u - 1, v - 1)] = w
        
        distances = [float("inf")] * n

        priority_queue = []
        heapq.heappush(priority_queue, (0, k - 1))
        distances[k - 1] = 0

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)

            if dist > distances[node]: continue

            for neighbor in graph[node]:
                weight = weights[(node, neighbor)]

                if distances[node] + weight < distances[neighbor]:
                    heapq.heappush(priority_queue, (weight, neighbor))
                    distances[neighbor] = distances[node] + weight
        
        return -1 if any(d == float("inf") for d in distances) else max(distances)