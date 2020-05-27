class Solution:
    def balancedStringSplit(self, s: str) -> int:
        check = {'R': 0, 'L': 0}
        count=0
        for word in s:
            check[word] += 1
            if check['R'] == check['L']:
                count += 1
                check['R'] = 0
                check['L'] = 0
        return count


# or:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        counter = 0
        for character in s:
            if character == "R":
                balance -= 1
            else:
                balance += 1
                
            if balance == 0:
                counter += 1
        
        return counter 