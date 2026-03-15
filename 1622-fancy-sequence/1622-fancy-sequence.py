class Fancy:

    def __init__(self):
        self.mod = 10**9 + 7  
        self.val = []  
        self.a = 1  
        self.b = 0  

    def append(self, val: int) -> None:
        x = (val - self.b + self.mod) % self.mod
        self.val.append(x * pow(self.a, self.mod - 2, self.mod) % self.mod)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.val):
            return -1  
        return (self.a * self.val[idx] + self.b) % self.mod

