def removeVovels (word, list_of_vovels):
    for vovel in word:
        if vovel in list_of_vovels:
            word = word.replace(vovel,'')
    return word