from __future__ import annotations
from typing import List, Optional, Tuple
import copy

N = open('input/18.txt').read().splitlines()

DEBUG = False

class SnailNumber:
    _value: Optional[int]
    left: SnailNumber
    right: SnailNumber

    def __init__(self, s: str | int):
        if isinstance(s, int):
            self._value = int(s)
            self.left = None
            self.right = None
            return

        depth = 0
        lstart = lend = None
        rstart = rend = None
        for i, char in enumerate(s):
            if char == '[':
                depth += 1
                if depth == 1: lstart = i + 1
            elif char == ',' and depth == 1:
                lend = i
                rstart = i + 1
            elif char == ']':
                depth -= 1
                if depth == 0: 
                    rend = i
                    break
                
        left = s[lstart:lend]
        right = s[rstart:rend]
        
        if left.isnumeric(): left = int(left)
        if right.isnumeric(): right = int(right)

        # if DEBUG: print('left:', left)
        # if DEBUG: print('right:', right)

        self._value = None
        self.left = SnailNumber(left)
        self.right = SnailNumber(right)

    def __repr__(self):
        if self.is_regular: return repr(self._value)
        return f'[{self.left},{self.right}]'

    def __iadd__(self, other: SnailNumber):
        assert self.is_pair

        self.left = copy.deepcopy(self)
        self.right = copy.deepcopy(other)
        
        return self
    
    def __add__(self, other: SnailNumber):
        assert self.is_pair
        new = SnailNumber(0)
        new._value = None
        
        new.left = copy.deepcopy(self)
        new.right = copy.deepcopy(other)

        reduce(new)

        return new

    def in_order(self, depth=0):
        if self.left is not None: yield from self.left.in_order(depth + 1)
        yield (self, depth)
        if self.right is not None: yield from self.right.in_order(depth + 1)

    def add_value(self, n: int):
        assert self.is_regular
        self._value += n

    def modify(self, s: SnailNumber):
        self._value = s._value
        self.left = s.left
        self.right = s.right

    def split(self):
        assert self.is_regular
        k = self._value // 2
        if DEBUG: print('k', k, self._value - k, f'({self._value})')
        self.left = SnailNumber(k)
        self.right = SnailNumber(self._value - k)
        self._value = None
    

    @property
    def is_regular(self):
        return self._value is not None

    @property
    def is_pair(self):
        return self._value is None

    @property
    def magnitude(self):
        if self.is_regular: return self._value
        return \
            3 * self.left.magnitude + \
            2 * self.right.magnitude

def explode(L: List[Tuple[SnailNumber, int]], i: int):
    assert (s := L[i][0]).is_pair
    assert s.left.is_regular
    assert s.right.is_regular

    #first, check the left for next regular
    #we skip 2 bc we start from the parent node, so
    #the left literal is 1 to the left and
    #the right literal is 1 to the right.
    for j in range(i - 2, -1, -1):
        if (left := L[j][0]).is_regular:
            if DEBUG: print("Regular number found to the left", left, '+', s.left._value)
            left.add_value(s.left._value)
            break
    else:
        if DEBUG: print("No regular numbers found to the left")

    #then, check the right
    for j in range(i + 2, len(L)):
        if (right := L[j][0]).is_regular:
            if DEBUG: print("Regular number found to the right", right, '+', s.right._value)
            right.add_value(s.right._value)
            break
    else:
        if DEBUG: print("No regular numbers found to the right")

    #finally, modify in-place
    s.modify(SnailNumber(0))

def reduce(s: SnailNumber):
    while True:
        if DEBUG: print('running again')
        L = list(s.in_order())

        for i, (node, depth) in enumerate(L):
            if node.is_pair and depth >= 4:
                if DEBUG: print("Exploding pair found", node)
                explode(L, i)
                break
        else:
            if DEBUG: print("no explosions found")
            for i, (node, depth) in enumerate(L):
                if node.is_regular and node._value >= 10:
                    if DEBUG: print("Splitting node found", node)
                    node.split()
                    break
            else: 
                if DEBUG: print("no splits found; number settled")
                return
    
def p1():
    s = SnailNumber(N[0])
    for x in N[1:]:
        if DEBUG: print(" ", s)
        k = SnailNumber(x)
        if DEBUG: print("+", k)
        s += k
        reduce(s)
        if DEBUG: print("=", s)
        if DEBUG: print()
    
    return s.magnitude

def p2():
    from itertools import permutations
    opts = list(map(SnailNumber, N))
    return max((a + b).magnitude for a, b in permutations(opts, r=2))

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())