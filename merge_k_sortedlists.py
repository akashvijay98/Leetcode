# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq
class Solution:
    
 
 
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        minheap=[]
        a=None
        p=None
        q=None
  
        for a in lists:
            while(a):
                heapq.heappush(minheap,a.val)
                
                a=a.next
                
        
        if  minheap == None :
            return 
        
        elif len(minheap)>0:
            h=heapq.heappop(minheap)
            p=ListNode(h)
            q=p
        
        
            while(minheap):
                h=heapq.heappop(minheap)
                p.next=ListNode(h)
                p=p.next
            
    
        return q
            
            
