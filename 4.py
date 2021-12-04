_draws, *_boards = open('input/4.txt').read().split('\n\n')
_draws = [int(x) for x in _draws.split(',')]


boards = [
    [
        [int(x) for x in line.split()] 
        for line in board.split('\n')] 
    for board in _boards
    ]

M = len(boards)
K = len(boards[0][0])
J = len(boards[0])


def _col(B, i):
    return [row[i] for row in B]

def _row(B, i):
    return B[i][:]

def _unmarked(B, draws):
    unmarked = 0
    for row in B:
        unmarked += sum(x for x in row if x not in draws)
    return unmarked

winners = {i: [] for i in range(M)}
for i, board in enumerate(boards):
    for j in range(J):
        winners[i].append(set(_row(board, j)))
    for k in range(K):
        winners[i].append(set(_col(board, k)))


def generate_wins():
    draws = set()
    for d in _draws:
        draws.add(d)
        for i, opts in winners.items():
            if any(draws >= opt for opt in opts):
                yield i, d, draws

def p1():
    i, winning_draw, draws = next(generate_wins())
    return _unmarked(boards[i], draws) * winning_draw


def p2():
    won = [False for _ in range(M)]
    for i, d, draws in generate_wins():
        won[i] = True
        if all(won):
            return _unmarked(boards[i], draws) * d

if __name__ == '__main__':
    print('P1:', p1())
    print('P2:', p2())