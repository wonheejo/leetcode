class Solution(object):
    def letterCombinations(self, digits):
        # mapping for number to letters
        keys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # empty case if no digits input then return empty list
        if not digits:
            return []

        result = []
        # main recursive function with input parameter of 'index' for current digits and 
        # 'path' for current combination of letters.
        def backtrack(index, path):
            # if the value of 'index' is equivalent to the length of 'digits' then all letters for that number 
            # has been traversed, so add it to the result list.
            # ie, index = 2 (3) is equal to length of digit '3' which is 3. so all letters should've been traversed
            if index == len(digits):
                result.append("".join(path))
                return
            
            # to be used in a for loop so that each letter in the digits can be traversed
            letters = keys[digits[index]]
            # index 'letter' processes through ie, 'def' letter by letter and adds to path one by one
            for letter in letters:
                # adds letter to path
                path.append(letter)
                # calls on backtrack function after adding one to index with current path => this is the recursive part
                backtrack(index+1, path)
                # since it has reached length of digit, it pops and would continue to traverse until all digits
                # have been traversed
                path.pop()
        
        # call on the backtrack function from 0
        backtrack(0, [])
        # return result
        return result
