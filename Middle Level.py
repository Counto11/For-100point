def sem(n):
    st = ''
    while n > 0:
        st += str(n % 7)
        n //= 7
    return st[::-1]


lst = []
for i in range(2, 101):
    st = sem(i)
    ost = str(sum([int(i) for i in st]) % 7)
    if len(st) % 3 == 0:
        st = sorted([int(st[:len(st) // 3]), int(st[len(st) // 3:(len(st) // 3) * 2]),
                     int(st[(len(st) // 3) * 2:])])
        st = ost + ''.join([str(i) for i in st]) + ost
    else:
        st = ost + st + ost
    lst.append(int(st, 7))

print(max([i for i in lst if i < 100]))
