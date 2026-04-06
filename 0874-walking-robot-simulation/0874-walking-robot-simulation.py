class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # store obstacles
        st = set()
        for x, y in obstacles:
            st.add((x, y))

        # directions: N, E, S, W
        dir = [(0,1), (1,0), (0,-1), (-1,0)]

        d = 0  # facing North
        x, y = 0, 0
        ans = 0

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                for _ in range(cmd):
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]

                    if (nx, ny) in st:
                        break

                    x, y = nx, ny
                    ans = max(ans, x*x + y*y)

        return ans