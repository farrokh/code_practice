class Solution:
    def reverse(self, x: int) -> int:
        const = 1
        if x < 0:
            const = -1
        x = str(abs(x))
        if x[-1] == 0:
            x = x.pop()
        x = x[::-1]
        x = int(x) * const
        if x < -2 **31 or x > ((2 ** 31) - 1):
            return 0
        else:
            return x 