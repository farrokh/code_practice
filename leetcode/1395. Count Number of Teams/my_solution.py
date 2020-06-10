class Solution:
    def numTeams(self, rating: List[int]) -> int:
        #loop through the items
        #assume the item to be min
        #check if there is bigger item
        #if count is 2 add the combination to a list
        #if the item exisit in the list continue searching
        count = 0
        for i,item in enumerate(rating):
            for j,jtem in enumerate(rating[i+1:]):
                if jtem > item:
                    for ktem in rating[(j+i+2):]:
                        if ktem > jtem:
                            count += 1
        
        for i,item in enumerate(rating):
            for j,jtem in enumerate(rating[i+1:]):
                if jtem < item:
                    for ktem in rating[(j+i+2):]:
                        if ktem < jtem:
                            count += 1
        
        return(count)