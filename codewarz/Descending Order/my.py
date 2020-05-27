def descending_order(num):
    res = [x for x in str(num)]
    new=sorted(res, reverse=True)
    return int(''.join(new))