def per_37(n):
    lst = []
    while n > 0:
        lst.append(n % 37)
        n //= 37
    return lst[::-1]


lst = []
for i in range(100_001, 400_000):
    st = sorted(per_37(i), reverse=True)
    if len(st) % 2 == 0:
        st = st[:len(st) // 2] + [0] + st[len(st) // 2:]
    else:
        st += [0]
        st = st[:len(st) // 2] + [1] + st[len(st) // 2:]
    int_st = 0
    for j in st:
        int_st += (j * 37 ** (len(st) - 1))
    if str(st).count('7') == 4:
        lst.append(i)

print(min(lst))