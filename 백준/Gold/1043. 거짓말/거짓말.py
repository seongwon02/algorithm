import sys

def root(a):
    if people[a] != a:
        people[a] = root(people[a])
    return people[a]

n, m = map(int, sys.stdin.readline().split())
people = [i for i in range(n+1)]

x = list(map(int, sys.stdin.readline().split()))
truth = x[1:] if x[0] != 0 else []

for p in truth:
    people[p] = 0

party = []

for _ in range(m):
    y = list(map(int, input().split()))
    if y[0] > 1:
        pl = [root(p) for p in y[1:]]
        num = min(pl)
        for p in pl:
            people[p] = num
    else:
        pl = y[1:]
        num = root(pl[0]) if pl else float("inf")

    if num != 0:
        party.append(y[1:])

answer = 0
known_roots = {root(p) for p in truth}

while party:
    z = party.pop()
    if all(root(p) not in known_roots for p in z):
        answer += 1

print(answer)
