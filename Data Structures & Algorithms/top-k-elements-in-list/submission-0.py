class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict = {}
        for i in nums:
            if i in freqdict:
                freqdict[i] += 1
            else:
                freqdict[i] = 1
        sorted_data = dict(sorted(freqdict.items(), key=lambda item: item[1],reverse=True))
        keys = list(sorted_data.keys())
        return keys[0:k]