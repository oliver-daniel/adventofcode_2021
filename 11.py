N = open('input/11.txt').read().splitlines()
N = [[int(x) for x in row] for row in N]

H = len(N)
W = len(N[0])

def _neighbours(r, c):
    for dy in range(-1, 2):
        if not 0 <= (y := r + dy) < H: continue
        for dx in range(-1, 2):
            if not 0 <= (x := c + dx) < W: continue
            elif dx == dy == 0: continue
            yield y, x


def _evolve(B):
        flashed = set()
        # first pass: increment
        ret = [[x + 1 for x in ln] for ln in B]

        while True:
            any_flashed = False
            for r, ln in enumerate(ret):
                for c, x in enumerate(ln):
                    if x > 9 and (r, c) not in flashed:
                        flashed.add((r, c))
                        for rr, cc in _neighbours(r, c):
                            ret[rr][cc] += 1
                        any_flashed = True
            if not any_flashed:
                # print(len(flashed), "flashed this round")
                for r, c in flashed:
                    ret[r][c] = 0
                return len(flashed), ret

def p1():
    curr = [ln[:] for ln in N]

    t = 0
    for i in range(100):
        tot_flashed, curr = _evolve(curr)
        t += tot_flashed

    return t

def p2():
    import itertools as it
    curr = [ln[:] for ln in N]

    expected = H * W

    for i in it.count():
        tot_flashed, curr = _evolve(curr)
        if tot_flashed == expected: return i + 1

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())