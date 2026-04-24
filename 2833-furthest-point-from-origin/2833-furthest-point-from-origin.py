class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d,r = 0,0
        for ch in moves:
            val = ord(ch)
            one = val&1
            two = (val>>1)&1
            r += one
            d += one^(two|-(1^two))

        return abs(d) + r