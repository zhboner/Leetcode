class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {}
        longestString = ""
        subString = ""

        for i in s:
            if i not in dict:
                subString += i
                dict[i] = 1
            else:
                if len(subString) > len(longestString):
                    longestString = subString
                subString = i
                dict.clear()
                dict[i] = 1
        if len(subString) > len(longestString):
                    longestString = subString
        return len(longestString)