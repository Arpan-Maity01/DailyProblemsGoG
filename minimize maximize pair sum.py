class Solution:
    def minPairSum(self, nums: List[int]) -> int:
    
        return max(a + b for a, b in zip(sorted(nums)[:int(len(nums)//2)], sorted(nums)[int(len(nums)/2):][::-1]))