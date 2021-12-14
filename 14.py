polymer, rules = open('input/14.txt').read().split('\n\n')

rules = dict(ln.split(' -> ') for ln in rules.split('\n'))

def _evolve(pairs):
    deltas = {p: 0 for p in rules.keys()}
    for (a, b), ct in pairs.items():
        if not ct: continue
        gen = rules[a + b]
        prefix = a + gen
        suffix = gen + b

        deltas[prefix] += ct
        deltas[suffix] += ct
        deltas[a + b] -= ct
    for pr, delt in deltas.items():
        pairs[pr] += delt

def p1():
    pairs = {p: polymer.count(p) for p in rules.keys()}
    
    for _ in range(10): _evolve(pairs)

    tots = {x: 0 for x in rules.values()}

    for (a, _b), ct in pairs.items():
        tots[a] += ct

    tots[polymer[-1]] += 1 # always going to be last

    mx = max(tots.values())
    mn = min(tots.values())

    return mx - mn 


def p2():
    pairs = {p: polymer.count(p) for p in rules.keys()}
    
    for _ in range(40): _evolve(pairs)

    tots = {x: 0 for x in rules.values()}

    for (a, _b), ct in pairs.items():
        tots[a] += ct
    tots[polymer[-1]] += 1

    mx = max(tots.values())
    mn = min(tots.values())

    return mx - mn
    


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())