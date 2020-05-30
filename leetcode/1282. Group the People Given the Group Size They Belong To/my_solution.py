class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dictionary = {}
        output = []
        for i,size in enumerate(groupSizes):
            if size in dictionary:
                if len(dictionary[size]) < size:
                    dictionary[size].append(i)
                else:
                    output.append(dictionary[size])
                    dictionary[size] = [i]
            else:
                dictionary[size] = [i]
        for key in dictionary:
            output.append(dictionary[key])
        return output
                