class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subLists = defaultdict(list)
        for string in strs:
            key = tuple(sorted(string))
            subLists[key].append(string)
        return list(subLists.values())