import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minheap=[]
        
        if len(intervals)==0:
            return 0
        
        intervals.sort(key=lambda x:x[0]) #----> we sort the list based on start time 
        
        heapq.heappush(minheap,intervals[0][1]) #---> we create a minheap based on end time 
                                                # min heap is used so that the meeting which will end early is kept at the top
        c=1
        for i in range(1,len(intervals)):
            start,end= intervals[i]
            
            if len(minheap)!=None and start>=minheap[0]: #we check if the start time of current element is after the earliest meeting finishes.
                                                          # if so we pop the earliest ending meeting and then push the current meeting as it starts later(this shows the same room can be used).
                heapq.heappop(minheap)
                heapq.heappush(minheap,end)
                
            else:
                heapq.heappush(minheap,end)
   
                c+=1 #c is used to show the size of the minheap(the number of rooms required)
            
            
            
        return c
