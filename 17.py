from functools import lru_cache

N = [x[2:].split('..') for x in open('input/17.txt').read()[13:].split(', ')]
(mX, MX), (mY, MY) = [(int(a), int(b)) for a, b in N]

@lru_cache(200)
def _tri(n):
    if n <= 1: return n
    return n + _tri(n-1)

def f(x, y, t):
    return sum([max(x - i, 0) for i in range(t)]), t * y - _tri(t - 1)

def candidates():
    # a lot of these limits were determined by brute-force
    # and then optimized for speed
    LIMIT = 400
    for x in range(1, LIMIT):
        for y in range(mY, abs(mY)):
            highest_y = None
            valid=False
            for t in range(1, LIMIT // 2): # don't expect to need to go further than this
                _x, _y = f(x, y, t)
                if _x > MX or _y < mY: 
                    break
                elif highest_y is None or highest_y < _y: 
                    highest_y = _y
                if mX <= _x <= MX and mY <= _y <= MY:
                    valid = True
                    break

            if valid and highest_y is not None: yield (x, y, highest_y)

S = list(candidates())

def p1():
    return max([x[2] for x in S])

# print("min X:", min(x[0] for x in S))
# print("max X:", max(x[0] for x in S))
# print("min Y:", min(x[1] for x in S))
# print("max Y:", max(x[1] for x in S))

def p2():
    return len(S)

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())
