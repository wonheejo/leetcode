class Solution(object):
    def combinationSum(self, candidate, target):

        # Initialize empty array to store the combinations that equal to target
        result = []

        # Main function for recursion to solve this problem which takes 3 parameters
        # start: where the search for combinations start
        # combinations: the primary list to store the combinations to sum 
        # sum: the total sum of the current combinations
        def backtrack(start, combinations, sum):

            # If the sum equals to target, it means that the combinations match to target
            if sum == target:
                # Append the combinations in list format to result array
                result.append(list(combinations))
                # End recursion here and go back to before recursion
                return
            # If the sum is greater than target then go back to previous recursion step
            if sum > target:
                return
            
            # Start the for loop from start and increment until last item in the candidate list
            for i in range(start, len(candidate)):
                # Append the current item to which 'i' is pointing to into combinations list 
                combinations.append(candidate[i])
                # Start recursion with current candidate[i] item + sum (in the beginning it will be just candidate[i]) 
                backtrack(i, combinations, sum + candidate[i])
                # Since python points back to previous step of recursion, eventually it will comeback
                # to this line which it will pop the last item appended
                combinations.pop()
        
        # This is the starting recursion parameters 
        # start = 0, empty list, sum = 0.
        backtrack(0, [], 0)
        # Once the recursion ends completely, it would return the 'result' array
        return result