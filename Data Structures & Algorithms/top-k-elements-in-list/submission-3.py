class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict = {}
        freqBuckets = [[] for i in range(len(nums) + 1)]
        result = []

        for i in nums:
            if i in freqdict:
                freqdict[i] += 1
            else:
                freqdict[i] = 1
        
        for key, value in freqdict.items():
            freqBuckets[value].append(key)

        for i in range(len(freqBuckets)-1, 0, -1):
            elements = freqBuckets[i]  
            for num in elements:
                result.append(num)
                resultLength = len(result)
                if resultLength == k:
                    return result

        return result