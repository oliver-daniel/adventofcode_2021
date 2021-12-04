import sys
N = open('input/2.txt').readlines()
def p1():
    x, y = 0, 0
    for line in N:
        match line.split():
            case "forward", n:
                x += int(n)
            case "down", n:
                y += int(n)
            case "up", n:
                y -= int(n) 
    return x * y


def p2():
    x, y, aim = 0, 0, 0
    for line in N:
        match line.split():
            case "forward", n:
                x += int(n)
                y += aim * int(n)
            case "down", n:
                aim += int(n)
            case "up", n:
                aim -= int(n) 
    return x * y


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())