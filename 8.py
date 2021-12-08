data = open('input/8.txt').read().splitlines()
N = [tuple(x.strip().split(' | ')) for x in data]

SEGMENTS = {x: i for i, x in enumerate(["abcefg", "cf", "acdeg","acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"])}

_a = 'abcdefg'

def p1():
    t = 0
    for _a, b in N:
        t += sum (1 for x in b.split() if len(x) in [2, 3, 4, 7])
    return t

def p2():
    import itertools as it
    all_segs = set(SEGMENTS.keys())

    def decode(x):
        a, b = x
        tkns = a.split()

        mapping = None

        for perm in map("".join, it.permutations(_a, 7)):
            d = dict(zip(perm, _a))
            
            translated_tkns = ("".join(sorted(map(d.get, tk))) for tk in tkns)
            
            if all(tk in all_segs for tk in translated_tkns):
                mapping = d
                break
        translated_b = ("".join(sorted(map(mapping.get, tk))) for tk in b.split())

        decoded = map(str, map(SEGMENTS.get, translated_b))
        return int("".join(decoded))
    return sum(map(decode, N))


if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())

