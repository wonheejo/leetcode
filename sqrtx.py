class Solution(object):
    def sqrtx(self, x):

        # for the case when x is 1
        if x < 2:
            return x
        
        # since this is a binary search we are going to start from between 1 to half of x since we know that 
        # the sqrt of x is never going to be larger than half of x
        left = 1
        right = x // 2

        # the loop will go on until the left pointer is equal or larger than the right pointer
        while left <= right:

            # we use another pointer 'mid' being 'r' from the equation such that: r * r <= x < (r - 1) * (r + 1)
            # where mid is 'r'.
            mid = (left + right) // 2

            # if that mid * mid is x, then just return mid
            if mid * mid == x:
                return mid
            # else if mid * mid is smaller than x, then increase the left side to mid + 1 
            # idea of binary search! since we know that it is smaller than x, then we can increase the left pointer
            # to something greater than the mid point and start from there
            elif mid * mid < x:
                left = mid + 1
            # since mid * mid is larger than x, then the right pointer will start from something less than the mid point
            # and repeat the whole loop again
            else:
                right = mid - 1
        
        # since the loop ended meaning we have an answer (to just this question) return right. 
        # because right is the largest number whose square is smaller or equal to x
        return right