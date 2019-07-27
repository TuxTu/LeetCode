#124ms,14.1MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        length = len(str(x))
        while length >= 2 and x // (10 ** (length - 1)) == x % 10:
            x = x % (10 ** (length - 1)) // 10
            length -= 2

        if length < 2:
            return True

        return False

#92ms,14.1MB
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10

        return x == revertedNumber or x == revertedNumber // 10

print(Solution2().isPalindrome(int(input())))
