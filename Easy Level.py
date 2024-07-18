lst_phi = [0, 1]
for _ in range(100):
    lst_phi.append(lst_phi[-1] + lst_phi[-2])

for i in range(1, 100):
    st = bin(i)[2:]
    if i in lst_phi:
        st = '11' + st[len(st) // 2:] + st[:len(st) // 2]
    else:
        st = st[:-1]
        st = '1' + st[len(st) // 2:] + st[:len(st) // 2] + '1'
    if int(st, 2) > 100:
        print(i)
        break
