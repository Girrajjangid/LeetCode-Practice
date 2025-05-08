class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq = [(0,0,0,1)]
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        moveTime[0][0] = -1
        while pq:
            time, i, j, cost = heapq.heappop(pq)
            if i == n-1 and j == m-1:
                return time
            for dx,dy in directions:
                x,y = i+dx,j+dy
                if 0<=x<n and 0<=y<m and moveTime[x][y] != -1:
                    new_time = moveTime[x][y] if time < moveTime[x][y] else time
                    new_time += cost
                    new_cost = 3-cost
                    moveTime[x][y] = -1
                    heapq.heappush(pq, (new_time, x, y, new_cost))
            
        return -1