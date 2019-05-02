<<<<<<< HEAD
#TempConvert.py
tem = input("请输入带有符号的温度值:")
if tem[-1] in ['F','f']:
    c=(eval(tem[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(c))
elif tem[-1] in ['C','c']:
    f=1.8*eval(tem[0:-1])+32
    print("转换后的的温度是{:.2f}F".format(f))
else:
    print("输入格式错误")
=======
#TempConvert.py
tem = input("请输入带有符号的温度值:")
if tem[-1] in ['F','f']:
    c=(eval(tem[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(c))
elif tem[-1] in ['C','c']:
    f=1.8*eval(tem[0:-1])+32
    print("转换后的的温度是{:.2f}F".format(f))
else:
    print("输入格式错误")
>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
