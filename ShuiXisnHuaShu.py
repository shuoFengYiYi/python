<<<<<<< HEAD

l = []
for x in range(100):
    #判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x <2:
        continue
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        l.append(x)
print(sum(l))

=======

l = []
for x in range(100):
    #判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x <2:
        continue
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        l.append(x)
print(sum(l))

>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
