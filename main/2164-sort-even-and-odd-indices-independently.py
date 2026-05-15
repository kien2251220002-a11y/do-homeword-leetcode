from collections import deque

class Solution:
    def sortEvenOdd(self, nums):
        len_nums = len(nums)
        even_indices_nums = [nums[e] for e in range(0, len_nums) if e % 2 == 0]
        odd_indices_nums = [nums[o] for o in range(0, len_nums) if o % 2 != 0]
        even_indices_nums = deque(sorted(even_indices_nums))
        odd_indices_nums = deque(sorted(odd_indices_nums, reverse=True))

        ret_val = []

        is_even_turn = True
        while (len(even_indices_nums) > 0 or len(odd_indices_nums) > 0):
            if (is_even_turn and len(even_indices_nums) > 0):
                ret_val.append(even_indices_nums.popleft())
                is_even_turn = False
            elif (not is_even_turn and len(odd_indices_nums) > 0):
                ret_val.append(odd_indices_nums.popleft())
                is_even_turn = True

        return ret_val