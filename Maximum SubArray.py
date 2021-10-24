class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        SubA=nums[0]
        MaxSum =0
        for i in nums:
            if MaxSum <0:
                MaxSum=0
            MaxSum+=i
            SubA = max(MaxSum,SubA)
        return SubA    