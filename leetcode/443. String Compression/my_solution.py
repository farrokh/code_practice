class Solution:
    def compress(self, chars: List[str]) -> int:
        new_chars = []
        curr, next = 0, 1
        
        while next < len(chars):  
            count = 1
            while next < len(chars) and chars[next] == chars[curr]:
                count += 1
                next += 1
            new_chars.append(chars[curr])            
            if count > 1:
                new_chars.extend(list(str(count)))
            curr = next
            next += 1
        if curr == len(chars)-1:
            new_chars.append(chars[curr])
        chars[:] = new_chars
        return len(chars)


                 