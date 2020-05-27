class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashSet = set()
        for pair in paths:
            hashSet.add(pair[0])
            
        for pair in paths:
            if pair[1] not in hashSet:
                return pair[1]