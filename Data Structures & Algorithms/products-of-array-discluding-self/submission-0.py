class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0 for i in range(len(nums))]
        suffixes = [0 for i in range(len(nums))]
        products = [0 for i in range(len(nums))]

        prefixes[0] = 1
        suffixes[-1] = 1

        for i in range(1,len(nums)):
            prefixes[i] = (nums[i - 1] * prefixes[i - 1])

        for j in range(len(nums)-2,-1,-1):
            suffixes[j] = suffixes[j + 1] * nums[j + 1]
        
        
        for i in range(len(nums)):
            products[i]=(prefixes[i] * suffixes[i])
        
        return products
