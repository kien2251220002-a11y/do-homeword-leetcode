class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sumDigits(num: int) -> int:
            res = 0
            while num:
                res += (num % 10)
                num //= 10
            return res
        m = {}
        for num in range(lowLimit, highLimit+1, 1):
            m[sumDigits(num)] = m.get(sumDigits(num), 0) + 1
        return max(m.values())      