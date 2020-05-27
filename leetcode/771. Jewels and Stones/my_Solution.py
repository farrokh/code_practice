class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counts = 0
        for i in J:
            counts += S.count(i)
        return counts