
from ast import List
from functools import reduce

from numpy import concat


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        it = iter(sorted(nums))
        return reduce(concat, [(b, a) for a, b in zip(it, it)])