class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num >= 1:
            if (num % 2) == 0:
                steps += 1
                num = num / 2
            else:
                steps += 1
                num -= 1
        return steps