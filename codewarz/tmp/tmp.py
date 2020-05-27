from collections import Counter
def destCity(n = 2, m = 3, indices = [[0,1],[1,1]]):
    R, C = map(list, zip(*indices))
    print(R)
    print(C)
    R, C = Counter(R), Counter(C)
    print(R)
    print(C)

destCity()        
