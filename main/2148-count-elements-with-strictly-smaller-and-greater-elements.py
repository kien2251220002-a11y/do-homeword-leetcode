
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        mn = min(nums) 
        mx = max(nums)
        
        res = 0
        
        for i in nums:
            if i!=mn and i!=mx:
                res += 1
        
        return res