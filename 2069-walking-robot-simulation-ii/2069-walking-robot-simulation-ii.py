class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        self.per = 2 * (self.w + self.h) - 4

    def step(self, num: int) -> None:
        if self.per == 0:
            return

        num %= self.per

        # special case: full cycle
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3  # South
            return

        while num > 0:
            if self.dir == 0:  # East
                move = min(num, self.w - 1 - self.x)
                self.x += move
                num -= move
                if num > 0:
                    self.dir = 1

            elif self.dir == 1:  # North
                move = min(num, self.h - 1 - self.y)
                self.y += move
                num -= move
                if num > 0:
                    self.dir = 2

            elif self.dir == 2:  # West
                move = min(num, self.x)
                self.x -= move
                num -= move
                if num > 0:
                    self.dir = 3

            else:  # South
                move = min(num, self.y)
                self.y -= move
                num -= move
                if num > 0:
                    self.dir = 0

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        if self.dir == 0:
            return "East"
        elif self.dir == 1:
            return "North"
        elif self.dir == 2:
            return "West"
        else:
            return "South"      
