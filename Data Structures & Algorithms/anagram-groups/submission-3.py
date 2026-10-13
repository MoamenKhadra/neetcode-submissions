class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subLists = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            subLists[key].append(string)
            
        return list(subLists.values())