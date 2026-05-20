class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        final = 0
        for i in range(len(s)):
            substr = ""
            longest = 0
            j = i
            while (j < len(s)):
                if s[j] in substr:
                    break
                else:
                    longest += 1
                    substr = substr + s[j]
                    j += 1
            if longest > final:
                final = longest 
        return final

        