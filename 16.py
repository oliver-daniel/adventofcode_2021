from collections import namedtuple

data = open('input/16.txt').read().splitlines()[0]
# print(data)
N = bin(int(data, 16))[2:].zfill(len(data)*4)

Packet = namedtuple('Packet', 'version typeid length_type length value')

def parse(s):
    version = int(s[:3], 2)
    typeid = int(s[3:6], 2)
    # print(version, 'type', typeid)
    
    
    seek = 6

    if typeid == 4:
        groups = []
        while True:
            last_group = s[seek] == "0"
            group = s[seek + 1 : seek + 5]
            groups.append(group)
            seek += 5
            if last_group: break  
        value = int("".join(groups), 2)
        return Packet(version, typeid, None, None, value), seek

    length_type = int(s[6], 2)
    seek = 7

    if length_type == 0:
        length = int(s[seek:seek + 15], 2)
        # print(0, version, 'length', length)
        # print(s)
        # print('VVVTTTI', 'L'*15, sep="")
        seek += 15
        contents = []
        d = 0
        while d < length:
            p, delt = parse(s[seek:])
            contents.append(p)
            d += delt
            seek += delt
        return Packet(version, typeid, length_type, length, contents), seek
    else:
        length =int(s[seek:seek + 11], 2)
        # print(1, version, 'length', length)
        seek += 11
        contents = []
        for _ in range(length):
            p, delt = parse(s[seek:])
            contents.append(p)
            seek += delt
        return Packet(version, typeid, length_type, length, contents), seek
        
    raise Exception

    

def p1():
    packet, _ = parse(N)
    # print(packet)
    def _traverse(p):
        # print(p.version, p.value)
        if not isinstance(p.value, list):
             return p.version
        return p.version + sum(map(_traverse, p.value))
    return _traverse(packet)


def p2():
    packet, _ = parse(N)
    from math import prod

    def _traverse(p):
        return [
            lambda: sum(map(_traverse, p.value)),
            lambda: prod(map(_traverse, p.value)),
            lambda: min(map(_traverse, p.value)),
            lambda: max(map(_traverse, p.value)),
            lambda: p.value,
            lambda: int(_traverse(p.value[0]) > _traverse(p.value[1])),
            lambda: int(_traverse(p.value[0]) < _traverse(p.value[1])),
            lambda: int(_traverse(p.value[0]) == _traverse(p.value[1])),
        ][p.typeid]()
    return _traverse(packet)

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())