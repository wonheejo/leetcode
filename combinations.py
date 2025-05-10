class Solution(object):
    def combine(self, n, k):
        # Initialize empty array to store all possible combinations
        result = []

        # Main function for recursion
        # start: where the index will start to look for combinations
        # path: this is where the current combination is located
        def backtrack(start, path):

            # If the number of items in the current combination is equal to the value of 'k' it will append to 
            # result array then backtrack to previous step
            if len(path) == k:
                result.append(list(path))
                return
            
            # Looks for combinations starting from 1 until 'n' is reached
            for i in range(start, n + 1):
                # Appends the current number to add into current combination 
                path.append(i)
                # Then starts the recursion
                backtrack(i + 1, path)
                # Once combination has been found or not found, it will backtrack and pop
                path.pop()
            
        # Start at 1 with empty combination array
        backtrack(1, [])
        return result