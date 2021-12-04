import sys
N = open('input/3.txt').read().splitlines()
K = len(N[0])

def _col(i):
    return _scol(N, i)

def _scol(G, i):
    return "".join(l[i] for l in G)

def _max(i):
    return max("01", key=_col(i).count)

def p1():
    gamma = [_max(i) for i in range(K)]
    gamma = int("".join(gamma), 2)
    epsilon = gamma ^ ((1 << K) - 1) # apparently this is how to NOT?
    return gamma * epsilon

def p2():
    water_candidates = N[:]
    co2_candidates = N[:]
    water = co2 = None

    for i in range(K):
        if not water:
            ct_1 = _scol(water_candidates, i).count("1")
            max_i = "01"[ct_1 >= len(water_candidates) / 2.]
            # print(len(water_candidates), max_i, ct_1)
            water_candidates = [x for x in water_candidates if x[i] == max_i]
            if len(water_candidates) == 1:
                water = water_candidates[0]
        if not co2:
            ct_1 = _scol(co2_candidates, i).count("1")
            max_i = "01"[ct_1 >= len(co2_candidates) / 2.]
            # print(len(co2_candidates), max_i, ct_1)
            co2_candidates = [x for x in co2_candidates if x[i] != max_i]
            if len(co2_candidates) == 1:
                co2 = co2_candidates[0]
    
    return int(water, 2) * int(co2, 2)


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())