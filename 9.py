data = open('input/9.txt').read().splitlines()
N = [[int(x) for x in row] for row in data]
H = len(N)
W = len(N[0])


def _neighbours(G, r, c):
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not 0 <= (y:= r + dy) < H: continue
        elif not 0 <= (x := c + dx) < W: continue
        yield G[y][x]

def _low_points():
    for r, row in enumerate(N):
        for c, x in enumerate(row):
            if all(x < y for y in _neighbours(N, r, c)) and N[r][c] != 9:
                yield x, r, c

def p1():
    return sum(x + 1 for x, *_ in _low_points())

def p2():
    visited = set()
    def _traverse(r, c, _debug=False, in_basin=None):
        if in_basin is None: in_basin = {(r, c)}
        if (r, c) in visited or N[r][c] == 9: return 0
        visited.add((r, c))
        t = 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if not 0 <= (y:= r + dy) < H: continue
            elif not 0 <= (x := c + dx) < W: continue
            elif N[r][c] != min(_neighbours(N, y, x)): continue

            t += (k := _traverse(y, x, False, in_basin))
            if k: in_basin.add((y, x))
        if _debug and len(in_basin) >= 70:
            for r in range(H):
                print("".join(('.', str(N[r][c]))[(r, c) in in_basin] for c in range(W)))
            print(t, len(in_basin))
        return t

    basins = sorted(_traverse(r, c, False) for _low, r, c in _low_points())
    
    from math import prod
    return prod(basins[-3:])
        


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())