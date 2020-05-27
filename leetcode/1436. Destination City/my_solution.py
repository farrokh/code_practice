class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_dic = defaultdict(set)
        for k,v in paths:
            paths_dic[k].add(v)
        for k,v in paths:
            if not paths_dic[v]:
                return v