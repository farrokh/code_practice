def count_smileys(arr):
    count = 0
    for item in arr:
        if len(item)==3:
            if item[1] not in ['-', '~']:
                continue
                
        if item[0] in [':',';'] and item[-1] in [')','D']:
            count += 1
    return count

    
    