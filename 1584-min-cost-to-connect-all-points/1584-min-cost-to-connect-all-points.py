class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = [False] * n
        adj_list = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[i].append((dis, j))
                adj_list[j].append((dis, i))
        visited[0] = True
        pq = adj_list[0]
        heapify(pq)
        k = cost = 0
        while k < n - 1:
            dis, v = heappop(pq)
            if not visited[v]:
                visited[v] = True
                cost += dis
                k += 1
                for edge in adj_list[v]:
                    heappush(pq, edge)
        return cost