class Solution:
    def two_sum(self, nums: List[int], target:int) -> List[List[int]]:
        seen = set()
        pairs = []
        for num in nums:
            difference = target - num
            if difference in seen:
                pairs.append([num, difference])
            else:
                seen.add(num)
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for i in range(len(nums)):
            target = nums[i]
            new_nums = nums[:i] + nums[i + 1:]
            two_sums = self.two_sum(new_nums,-target)
            for pair in two_sums:
                triplets.add(tuple(sorted([target,*pair])))
        
        return [list(t) for t in triplets]
        