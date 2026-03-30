class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even1, odd1 = "", ""
        even2, odd2 = "", ""
        
        for i in range(len(s1)):
            if i % 2 == 0:
                even1 += s1[i]
                even2 += s2[i]
            else:
                odd1 += s1[i]
                odd2 += s2[i]
        
        even1 = sorted(even1)
        even2 = sorted(even2)
        odd1 = sorted(odd1)
        odd2 = sorted(odd2)
        
        return even1 == even2 and odd1 == odd2