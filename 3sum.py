class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort from decreasing
        nums.sort()
        result = []

        for i in range(len(nums)):
            # for checking duplicates of i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # left pointer (first pointer) from i + 1
            left = i + 1
            # right pointer (second pointer) from right end - 1
            right = len(nums) - 1

            # while left pointer is smaller than right pointer loop
            while left < right:
                # first get the total sum of the three pointers
                total = nums[i] + nums[left] + nums[right]

                # if the sum is smaller than 0, increment left pointer by one and try again
                if total < 0:
                    left += 1
                # if the sum is larger than 0, move right pointer to the left by one and try again
                elif total > 0:
                    right -= 1
                # then the sum must be 0 and append to end result
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # check for duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return result
        
        
