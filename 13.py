# coding: utf-8 -*-
# 罗马数字转整数

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        b={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        result=[]
        if not s:
            return 0
        i=0
        while i<(len(s)-1):
            c=s[i]+s[i+1]
            if c in b:
                result.append(b[c])
            else:
                if i==(len(s)-2):
                    result.append(b[s[i]])
                    result.append(b[s[i+1]])
                else:
                    result.append(b[s[i]])
            i += 1

        return result

s=Solution()
print(s.romanToInt("MDCXCV"))



