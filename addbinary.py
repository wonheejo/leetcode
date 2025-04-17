class Solution(object):
    def addBinary(self, a, b):

        # create variables i and j to start at the end of each binary numbers for addition
        i, j = len(a)-1, len(b)-1
        
        # create an empty list to store the results of the addition
        result = []
        
        # the carry digit for which if the addition overflows 
        # since we are doing binary addition, it is either 0 + 0, 0 + 1 or 1 + 1 (overflow)
        # but the carry will be initialized as 0 at start only
        carry = 0

        # loop for which this addition will continue until there is no more digits to add
        while i >= 0 or j >= 0 or carry:

            # the binary digit to add will be assigned to variables digit_a and b
            # simple to see as it will be either 1 or 0 depending on the digit 
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # the addition of digit_a and digit_b plus the carry
            total = digit_a + digit_b + carry

            # if the addition is more or equal to 2, carry will 1. that is why we are using floor division
            carry = total // 2

            # the result of the modulo will be added to the result (but not as int, as str)
            result.append(str(total % 2))

            # since we are looping through the loop starting from the end, we have to decrement
            # at the end of each loop
            i -= 1
            j -= 1

        # now that we have the result array in place, we now have to return it, but in reversed
        return ''.join(reversed(result))