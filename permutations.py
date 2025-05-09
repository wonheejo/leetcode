# I believe there is a more efficient way to get this done using Heap's algorithm
# Will post a solution using heaps algorithm next time

class Solution(object):
    def permute(self, nums):
        # Initialize new array to store permutation combinations
        result = []

        # Main recursive function which takes two parameters:
        # paths: to track current combinations
        # used: to track if new item has been used or not with boolean variables
        def backtrack(paths, used):

            # if the length of paths is equal to nums then it means a new permutation combination has been found
            # so append it to the result array
            if len(paths) == len(nums):
                result.append(list(paths))
                return
            
            # loop through nums array 
            for i in range(len(nums)):
                # if used[i] is true then continue through loop
                if used[i]:
                    continue
                # have to add item of nums[i] into current combination array to check
                paths.append(nums[i])
                # also make used[i] True to track 
                used[i] = True
                # start recursion with newly added paths and used array
                backtrack(paths, used)
                # since recursion is finished and backtracked, remove last item from paths combination array
                paths.pop()
                # also make that spot where the item was removed into False 
                used[i] = False
        
        # Start off the recursion with empty combination array and all slots marked as False
        backtrack([], [False] * len(nums))
        return result