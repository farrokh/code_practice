class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_str = ""
        for i in range(len(address)):
            if address[i] == '.':
                new_str += "[.]"
            else:
                new_str += address[i]
        return new_str