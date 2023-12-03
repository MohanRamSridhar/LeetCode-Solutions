class Solution(object):
    def minTimeToVisitAllPoints(self, p):
        ans=0
        for i in range(len(p)-1):
            ans+=max(abs(p[i][0]-p[i+1][0]),abs(p[i][1]-p[i+1][1]))
        return ans