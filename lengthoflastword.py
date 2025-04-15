class Solution(object):
    def lengthOfLastWord(self, s):

        # strip() helps to remove front and ending whitespaces
        s = s.strip()
        # split() helps to split the remaining words based on whtiespaces
        wordlist = s.split()
        # return the length of the last word in the wordlist
        return len(wordlist[-1])