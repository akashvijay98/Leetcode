class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        res=0

        
        indices=sorted(costs,key= lambda c:c[0]-c[1])
        
        
        for i in range(0,n//2):
            res+=indices[i][0]
            res+=indices[n-i-1][1]
        return res
            
            
