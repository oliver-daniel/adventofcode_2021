import sys

N = open('input/1.txt').read().strip().split('\n')

# N = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263""".split('\n')

N = [int(x) for x in N]

def p1():
    t = 0
    for x, y in zip(N, N[1:]):
        if y > x:
            t += 1
    return t

def p2():
    psa = []
    for x, y, z in zip(N, N[1:], N[2:]):
        psa.append(x + y + z)
    
    t = 0
    for x, y in zip(psa, psa[1:]):
        if y > x:
            t += 1
    return t



if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())