import heapq as q
N = open('input/15.txt').read().splitlines()
N = [[int(x) for x in ln] for ln in N]

H = len(N)
W = len(N[0])

def _get(H, W, y, x):
    ytiles, r = divmod(y, H)
    xtiles, c = divmod(x, W)

    node = (N[r][c] + ytiles + xtiles)
    if node >= 10: node = (node % 10) + 1
    return node



def _traverse(_H = H, _W = W, start=(0, 0), goal=(H - 1, W - 1)):
        visited = set()
        queue = []
        q.heappush(queue, (0, start))

        while queue:
            cost, pos = q.heappop(queue)
            if pos == goal: return cost
            elif pos in visited: continue
            
            visited.add(pos)
            row, col = pos
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if not 0 <= (y := row + dy) < _H: continue
                elif not 0 <= (x := col + dx) < _W: continue

                node = _get(H, W, y, x)

                # print(y, x, G[r][c], xtiles, ytiles, node)

                q.heappush(queue, (cost + node, (y, x)))

def p1():
    return _traverse()
        
def p2():
    return _traverse(_H = H * 5, _W = W * 5, goal=(H * 5 - 1, W * 5 - 1))


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())