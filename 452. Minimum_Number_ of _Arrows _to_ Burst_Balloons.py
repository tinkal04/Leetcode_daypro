class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        points.sort()
        
        prev = points[0]
        count = 1
        for i in range(1, n):
            currStart, currEnd = points[i]
            prevStart, prevEnd = prev
            
            if currStart > prevEnd:  
                count += 1
                prev = points[i]
            else:
            
                prev[0] = max(prevStart, currStart)
                prev[1] = min(prevEnd, currEnd)
        
        return count
