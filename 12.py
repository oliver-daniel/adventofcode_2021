from collections import defaultdict
data = open('input/12.txt').read().splitlines()
N = [tuple(ln.split('-')) for ln in data]

G = defaultdict(set)

for src, dest in N:
    G[src].add(dest)
    if src != 'start' and dest != 'end':
        G[dest].add(src)
G['end'] = set()


def p1():
    def _traverse(node, visited=None, path=None, goal='end'):
        if path is None: path = []
        path.append(node)
        if visited is None: 
            visited = set()
        elif node == goal: yield ",".join(path)
        elif node in visited: return False
        
        if node == node.lower(): visited.add(node)

        for dst in G[node]:
            yield from _traverse(dst, visited.copy(), path[:])
    
    k = set(_traverse('start'))
    # print("\n".join(k))
    return len(k)
            

def p2():
    def _traverse(node, visited=None, path=None, goal='end', special=None):
        if path is None: path = []
        path.append(node)
        if visited is None: 
            visited = set()
        elif node == goal: 
            yield ",".join(path)
        elif node in visited:
            if node + "." in visited: return False
            elif node == special: visited.add(node + ".")
            else: return False
        
        if node == node.lower(): visited.add(node)

        for dst in G[node]:
            yield from _traverse(dst, visited.copy(), path[:], special=special)

    k = set()
    for special in G.keys():
        if special in ('start', 'end') or special == special.upper(): continue
        k.update(_traverse('start', special=special))
    # print("\n".join(k))
    return len(k)

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())