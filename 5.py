from collections import defaultdict

N = open('test/5lol.txt').read().splitlines()
data = []
for x, y in map(lambda x: x.split(' -> '), N):
    x = tuple(map(int, x.split(',')))
    y = tuple(map(int, y.split(',')))
    data.append((x, y))

def p1():
    G = defaultdict(int)
    for (x1, y1), (x2, y2) in data:
        if x1 != x2 and y1 != y2: continue
        # one of these only runs once
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                G[(x, y)] += 1

    return sum(1 for x in G.values() if x > 1)


def p2():
    G = defaultdict(int)
    for (x1, y1), (x2, y2) in data:
        if x1 != x2 and y1 != y2:
            xseq = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            yseq = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)

            for x, y in zip(xseq, yseq):
                G[(x, y)] += 1 
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    G[(x, y)] += 1

    return sum(1 for x in G.values() if x > 1)

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())