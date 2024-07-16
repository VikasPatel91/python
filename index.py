class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str3=""
        for i in range(len(str2)):
            if str2 not in str2:
                return ""
        
        
a=Solution()
str1 = "ABCDEF"
str2 = "ABC"
print(a.gcdOfStrings(str1,str2))
