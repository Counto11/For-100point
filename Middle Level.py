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
    if len(st) % 2 == 0:
        st = ost + st[len(st) // 2:] + st[:len(st) // 2] + ost
    else:
        st += ost
        st = st[len(st) // 2:] + st[:len(st) // 2]
    lst.append((int(st, 7), i))

print(min(lst)[1])
