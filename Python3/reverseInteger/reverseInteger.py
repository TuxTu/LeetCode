#44ms,13.9MB
class Solution:
    def reverse(self, x: int) -> int:
        num, res = abs(x), 0
        max = (1 << 31) - 1 if x > 0 else 1 << 31

        while num > 0:
            res = res * 10 + num % 10
            num //= 10

        if res > max:
            return 0
        else:
            return res if x > 0 else -res

print(Solution().reverse(int(input())))