data = open('input/7.txt').read()
N = [*map(int, data.split(','))]
X = max(N)


def p1():
    def _fuel(posn):
        return sum(abs(x - posn) for x in N)
    mn = min(map(_fuel, N))
    return mn

def p2():
    def _fuel(posn):
        return sum((k := abs(x - posn)) * (k + 1) for x in N) 
    mn = min(map(_fuel, range(X + 1)))
    return mn // 2
        

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())
