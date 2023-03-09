class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for i in numsSet:
            if nums.count(i) >= len(nums)/2 :
                return i
