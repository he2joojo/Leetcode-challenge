from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # 방법1.
        # nums2 = set(nums)
        # for i in nums2 :
        #     if nums.count(i) == 1:
        #         return i

        # 방법2.
        nums = [1,2,2,3,3,2,3,4,5,3,4,5,6,6]
        cnt = Counter(nums)
        result = 0;
        for k, v in cnt.items():
            if v == 1 :
                result = k
        return result
