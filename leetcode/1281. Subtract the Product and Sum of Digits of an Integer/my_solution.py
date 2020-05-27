class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        for i in str(n):
            i = int(i)
            summ += i
            product *= i
        return (product - summ)
        