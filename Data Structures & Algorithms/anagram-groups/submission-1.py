class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)
            groups[key].append(str) # the key for the dict should be hashable -> immutable
        return list(groups.values())



        