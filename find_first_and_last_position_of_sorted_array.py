class Solution(object):
    def searchRange(self, nums, target):

        # Uses two basic binary searches to find first and second
        # first function finds the first value
        def left_search():
            left, right = 0, len(nums) - 1
            # since in the condition, if no value is found, to return [-1, -1], 
            # first is set to -1
            first = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        first = mid
                    right = mid - 1
            
            return first
        
        # second function finds the second value
        def right_search():
            left, right = 0, len(nums) - 1
            # since in the condition, if no value is found, to return [-1, -1], 
            # second is set to -1
            second = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        second = mid
                    left = mid + 1
            
            return second
        
        return [left_search(), right_search()]