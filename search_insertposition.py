class Solution:
    def searchInsert(self, nums: List[int], k: int) -> int:
        l=0
        h=len(nums)-1
        
        while(l<=h):
            mid=(l+h)//2
            
            if k==nums[mid]:
                return mid
            elif k<nums[mid]:
                h=mid-1
            elif k>nums[mid]:
                l=mid+1
        if k>nums[mid]:
            return mid+1
        elif k<nums[mid]:
            return mid
        
        
