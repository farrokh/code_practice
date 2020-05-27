class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

        # not unsing the builtin method:
        # A = string.ascii_uppercase
        # a = string.ascii_lowercase
        # for i,ch in enumerate(str):
        #     if ch in A:
        #         str = str.replace(ch, a[A.index(ch)])
        # return str