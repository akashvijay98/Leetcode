class Solution:
    def breakPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return ""
        s1=""
        for i in range(n):
            j=n-1-i
            if (i==j): # to check the middle of the string because the middle letter cannot be manipulated
                continue
                
            if s[i]!='a':
                s1=s[:i]+"a"+s[i+1:] #replacing the i'th letter with a 
                return s1
            
        
        s1=s[:n-1]+"b" #replacing n-1'th letter with b
        
        
        return s1
