class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict = {}
        freqBuckets = {}
        mostFreqList = []

        for i in range(len(nums)+1):
            freqBuckets[i]=[]

        for i in nums:
            if i in freqdict:
                freqdict[i] += 1
            else:
                freqdict[i] = 1
        
        for key, value in freqdict.items():
            freqBuckets[value].append(key)

        for i in range(len(nums), 0, -1):
            elements = freqBuckets[i]
            mostFreqList = mostFreqList + elements
            overflow = len(mostFreqList) - k
            if overflow > 0:
                for i in range(overflow):
                    mostFreqList.pop()

        return mostFreqList