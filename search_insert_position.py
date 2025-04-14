class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        if not nums:
            return 0
        
        while i< len(nums):
            if target <= nums[i]:
                return i
            i += 1
        
        return len(nums)