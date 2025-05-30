class Solution:
    def dfs(self, edges, start):
        dist = [-1] * len(edges)
        d = 0
        while start != -1 and dist[start] == -1:
            dist[start] = d
            d += 1
            start = edges[start]
        return dist

    def closestMeetingNode(self, edges, node1, node2):
        dist1 = self.dfs(edges, node1)
        dist2 = self.dfs(edges, node2)
        result = -1
        min_dist = float('inf')

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i

        return result