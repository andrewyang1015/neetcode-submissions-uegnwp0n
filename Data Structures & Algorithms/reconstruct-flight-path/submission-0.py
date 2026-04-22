from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)


        stack = ["JFK"]
        itinerary = []

        while stack:
            src = stack[-1]
            has_edge = False

            # DFS step
            while graph[src]:
                dst = graph[src].pop()
                has_edge = True
                stack.append(dst)
                break
            
            if has_edge: continue
            
            stack.pop()
            # Finished processing children, add now
            itinerary.append(src)
        
        return itinerary[::-1]
            