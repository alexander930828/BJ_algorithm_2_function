#1

def solve(a):
    return sum(a)

def solve(a):
    total = 0
    for x in a:
        total += x
    return total


#2

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)


#3

n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:
        ns = list(map(int, str(i)))
        if ns[0] - ns[1] == ns[1] - ns[2]:
            han += 1
print(han)