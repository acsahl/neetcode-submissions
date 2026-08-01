class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for s in strs:
            sortedname = ''.join(sorted(s))
            final[sortedname].append(s)
        return list(final.values())


            
        