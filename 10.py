N = open('input/10.txt').read().splitlines()
M = len(N)

d = dict(zip(')]}>', '([{<'))
_d = dict(zip('([{<', ')]}>'))


def incomplete_chars():
    for i, line in enumerate(N):
        stack = []
        for x in line:
            if x in '([{<': stack.append(x)
            elif stack.pop() != d[x]:
                yield x, i


def p1():
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    t = sum(scores[x] for x, _ in incomplete_chars())
    return t

def p2():
    corrupted_lines = {i for _, i in incomplete_chars()}
    incomplete_lines = (N[i] for i in {*range(M)} - corrupted_lines)

    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    vals = []

    for ln in incomplete_lines:
        t = 0
        stack = []
        for x in ln:
            if x in '([{<': stack.append(x)
            else: stack.pop()

        while stack:
            k = stack.pop()
            t *= 5
            t += scores[_d[k]]
        vals.append(t)
    
    assert len(vals) % 2
    return sorted(vals)[len(vals) // 2]



if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())