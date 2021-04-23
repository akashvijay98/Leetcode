class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        a=" "
        index=0
        
        if len(strs)==0:
            return a
        for i in strs[0]:
            for j in range(1,len(strs)):
                
                if index >= len(strs[j]) or i != strs[j][index]  :
                    
                    return a[1:]
                
            a+=i
            index+=1
            
        
        return a[1:]
            
                    
            
        

            
            
            
        
