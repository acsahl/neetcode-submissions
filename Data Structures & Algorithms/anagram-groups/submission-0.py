class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = []
        for string in strs:
            added = False
            for i,anagram in enumerate(anagramList):
                if sorted(anagram[0]) == sorted(string):
                    anagramList[i].append(string)
                    added = True
            if not added:
                anagramList.append([string])
            
        return anagramList
        
        