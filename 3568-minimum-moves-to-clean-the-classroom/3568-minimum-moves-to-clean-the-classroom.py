from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        id = [[-1] * n for _ in range(m)]

        k = 0
        sr = 0
        sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr = r
                    sc = c
                elif classroom[r][c] == 'L':
                    id[r][c] = k
                    k += 1

        if k == 0:
            return 0

        total_mask = (1 << k) - 1

        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        queue = deque()

        best[sr][sc][0] = energy
        queue.append((sr, sc, 0, energy, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, moves = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1

                if ne < 0:
                    continue

                nmask = mask

                if classroom[nr][nc] == 'R':
                    ne = energy

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << id[nr][nc]

                if nmask == total_mask:
                    return moves + 1

                if ne <= best[nr][nc][nmask]:
                    continue

                best[nr][nc][nmask] = ne

                queue.append((nr, nc, nmask, ne, moves + 1))

        return -1