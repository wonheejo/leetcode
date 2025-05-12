class Solution(object):
    def findEvenNumber(self, digits):

        # Initialize result set. Not an array or list because it can continue duplicates
        result = set()
        # Since going to go through loops, might as well as simplify things 
        n = len(digits)

        # First loop for first digit
        for i in range(n):
            # Second loop for second digit
            for j in range(n):
                # Third loop for third digit
                for k in range(n):

                    # Since all three digits have to be different
                    if i == j or i == k or j == k:
                        continue
                    # First digit cannot be zero
                    if digits[i] == 0:
                        continue
                    # The three digit combination has to be an even number
                    if digits[k] % 2 != 0:
                        continue
                    
                    # Put the three digits into a single number
                    perm = digits[i] * 100 + digits[j] * 10 + digits[k]

                    # Add the three digit number into result
                    result.add(perm)

        # Return the sorted set
        return sorted(result)
    
