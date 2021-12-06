N = [*map(int, open('input/6.txt').read().split(','))]

D = [N.count(i) for i in range(9)]

def _evolve(arr):
    arr = [*arr[1:7], arr[7] + arr[0], arr[8], arr[0]]
    return arr



def p1():
    _curr = D[:]
    for _ in range(80):
        _curr = _evolve(_curr)
    return sum(_curr)

def p2():
    _curr = D[:]
    for _ in range(256):
        _curr = _evolve(_curr)
    return sum(_curr)

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())