class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        total = 0
        
        for i in range(1, len(timeSeries)):
            total += min(duration, timeSeries[i] - timeSeries[i-1])
        
        return total + duration