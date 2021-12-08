import sys
N = open('input/2.txt').readlines()
def p1():
    x, y = 0, 0
    for line in N:
        tk, n = line.split()
        n = int(n)
        if tk == "forward":
            x += n
        elif tk == "down":
            y += n
        else:
            y -= n
    return x * y



def p2():
    x, y, aim = 0, 0, 0
    for line in N:
        tk, n = line.split()
        n = int(n)
        if tk == "forward":
            x += n
            y += aim * n
        elif tk == "down":
            aim += n
        else:
            aim -= n 
    return x * y


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())