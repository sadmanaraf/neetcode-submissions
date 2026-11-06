class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        groupmax = neededTime[0]
        totaltime = 0
        for i in range(1,len(colors)):

            if colors[i-1] == colors[i]:
                if groupmax > neededTime[i]:
                    totaltime += neededTime[i]
                else:
                    totaltime += groupmax
                    groupmax = neededTime[i]
                    
            else:
                groupmax = neededTime[i]
        return totaltime




