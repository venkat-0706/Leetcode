class Solution:
    def checkOverlap(self, r: int, cx: int, cy: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = max(x1, min(cx, x2)) - cx
        y = max(y1, min(cy, y2)) - cy

        return x * x + y * y <= r * r