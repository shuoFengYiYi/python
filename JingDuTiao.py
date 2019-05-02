<<<<<<< HEAD
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
=======
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
print("\n"+"执行结束".center(scale//2,'-'))