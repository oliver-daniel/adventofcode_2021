points, folds = open('input/13.txt').read().split('\n\n')
points = [(int(a), int(b)) for a, b in (ln.split(',') for ln in points.split('\n'))]
folds = [(dirn, int(x)) for dirn, x in (ln.split()[-1].split('=') for ln in folds.split('\n'))]

W = max(x[0] for x in points)
H = max(x[1] for x in points)

grid = [[0 for _ in range(W + 1)] for __ in range(H + 1)]

for x, y in points:
    grid[y][x] = 1

def _print(G):
    for ln in G:
        print("".join('.#'[x] for x in ln))

def _fold(G, dirn, axis):
    if dirn == 'y':
        for dy, ln in enumerate(G[axis + 1:], start=1):
            for c, x in enumerate(ln):
                G[axis - dy][c] |= x
                ln[c] = 0
    else:
        for r, ln in enumerate(G):
            for dx, x in enumerate(ln[axis + 1:], start=1):
                G[r][axis - dx] |= x
                ln[axis + dx] = 0


def p1():
    gg = [ln[:] for ln in grid]

    dirn, axis = folds[0]
    _fold(gg, dirn, axis)

    return sum(map(sum, gg))



def p2():
    gg = [ln[:] for ln in grid]
    for dirn, axis in folds:
        _fold(gg, dirn, axis)
    
    _print([ln[:5 * 8] for ln in gg[:7]])

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())