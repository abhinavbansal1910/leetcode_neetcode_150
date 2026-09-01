class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = k
                    k += 1

        target = (1 << k) - 1

        q = deque()
        q.append((start[0], start[1], energy, 0, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'R':
                    ne = energy

                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                state = (nr, nc, ne, nmask)

                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, ne, nmask, moves + 1))

        return -1