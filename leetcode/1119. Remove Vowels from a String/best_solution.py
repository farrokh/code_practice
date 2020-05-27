def removeVovels (word, list_of_vovels):
    reformatted = ''
    for vovel in word:
        if vovel not in list_of_vovels:
            reformatted += vovel
        
    return word