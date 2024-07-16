for i in range(1, 100):
    st = bin(i)[2:]
    if len(st) % 2 == 0:
        st = '1' + st[len(st) // 2:] + st[:len(st) // 2] + '0'
    else:
        st = st[:-1]
        st = '1' + st[len(st) // 2:] + st[:len(st) // 2] + '1'
    if int(st, 2) > 100:
        print(i)
        break