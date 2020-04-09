def combinator(k, u):
    l = len(k)
    for i in range(l ** u):
        s = ""
        for j in range(u):
            i, index = divmod(i,l)
            s += k[index]
        yield s

for n in range(1,6):
    for i in combinator("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890",n): print(i)
