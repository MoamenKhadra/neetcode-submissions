class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        k = 1
        longest = k
        j = nums[0]
        for i in range(1, len(nums)):
            if j == nums[i] - 1:
                k += 1
                if k > longest:
                    longest = k
            elif j == nums[i]:
                continue
            else:
                k = 1
            j = nums[i]
        return longest