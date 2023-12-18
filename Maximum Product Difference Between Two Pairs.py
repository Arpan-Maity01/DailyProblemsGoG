class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return (X:=sorted(nums))[-1]*X[-2]-X[1]*X[0]