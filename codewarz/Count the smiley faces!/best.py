from re import findall
def count_smileys(arr):
    return len(findall(r"[:;][-~]?[)D]", " ".join(arr)))