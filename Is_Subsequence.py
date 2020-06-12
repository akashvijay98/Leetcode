class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=len(s)
        n=len(t)
        
        i=0
        j=0
        
        if len(s)==0:
            return True
        
        if len(t)==1:
            if(s[0]!=t[0]):
                return False
        
        while(j<m and i<n):
            if(s[j]==t[i]):
                j+=1
            i+=1
        if(j<(m) and i==n ):
            return False
        else:
            return True
