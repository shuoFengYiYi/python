<<<<<<< HEAD
### 函数

---

- **ord()** 函数获取字符的整数表示

- **chr()** 函数把编码转换为对应的字符

- **encode()** 将编码为指定的bytes

- **decode()** 将bytes转换为指定编码

  ```python
  'ABC'.encode('ascii')
  b'ABC'.decode('ascii')
  ```

- **len()** 字符串中包含多少个字符

- **round(x[,d])** 四舍五入，d为保留小数位数

- **str()** 返回对应字符串形式

- **hex()\oct()** 十六进制、八进制

- **chr()** 返回Unicode编码字符

- **ord()** 返回字符对应Unicode码

- **str.lower()\str.upper()** 转换小写、大写

- **str.split(sep=None)** 返回一个列表，由str根据sep被分割的部分组成

- **str.count(sub)** 返回子串sub在str中出现的次数

- **str.replace(old,new)** 返回字符串副本，所有old子串被替换为new

- **str.center(width[,fillchar])** 字符串str根据宽度width居中，fillchar可选

- **str.strip(chars)** 从str中去掉在其左侧和右侧chars中列出的字符

- **str.join(iter)** 在iter变量除最后元素外每一个元素后增加一个str

- **time()** 获取当前时间戳，浮点数

- **ctime()** 获取当前时间并以易读方式表示，返回字符串

- **gmtime()** 获取当前时间，表示为计算机可处理的时间格式

- **strftime(tpl,ts)** ts为计算机内部时间类型变量

``` python
t = time.gmtime()
time.strftime("%Y-%m-%d  %H:%M:%S", t)
```

- **strptime(str,tpl)** str字符串形式的时间至 tpl格式化模板字符串，定义输入效果

```python
timeStr = '2018-01-26  12:55:20'
time.strptime(timeStr,"%Y-%m-%d  %H:%M:%S")
```

---
### 字符串格式化

|    :     |       填充       |            对齐             |       宽度       |       <,>        |              <.精度>               |
| :------: | :--------------: | :-------------------------: | :--------------: | :--------------: | :--------------------------------: |
| 引导符号 | 用于填充单个字符 | <左对齐  >右对齐  ^居中对齐 | 槽设定的输出宽度 | 数字的千位分隔符 | 浮点数小数精度或字符串最大输出长度 |

=======
### 函数

---

- **ord()** 函数获取字符的整数表示

- **chr()** 函数把编码转换为对应的字符

- **encode()** 将编码为指定的bytes

- **decode()** 将bytes转换为指定编码

  ```python
  'ABC'.encode('ascii')
  b'ABC'.decode('ascii')
  ```

- **len()** 字符串中包含多少个字符

- **round(x[,d])** 四舍五入，d为保留小数位数

- **str()** 返回对应字符串形式

- **hex()\oct()** 十六进制、八进制

- **chr()** 返回Unicode编码字符

- **ord()** 返回字符对应Unicode码

- **str.lower()\str.upper()** 转换小写、大写

- **str.split(sep=None)** 返回一个列表，由str根据sep被分割的部分组成

- **str.count(sub)** 返回子串sub在str中出现的次数

- **str.replace(old,new)** 返回字符串副本，所有old子串被替换为new

- **str.center(width[,fillchar])** 字符串str根据宽度width居中，fillchar可选

- **str.strip(chars)** 从str中去掉在其左侧和右侧chars中列出的字符

- **str.join(iter)** 在iter变量除最后元素外每一个元素后增加一个str

- **time()** 获取当前时间戳，浮点数

- **ctime()** 获取当前时间并以易读方式表示，返回字符串

- **gmtime()** 获取当前时间，表示为计算机可处理的时间格式

- **strftime(tpl,ts)** ts为计算机内部时间类型变量

``` python
t = time.gmtime()
time.strftime("%Y-%m-%d  %H:%M:%S", t)
```

- **strptime(str,tpl)** str字符串形式的时间至 tpl格式化模板字符串，定义输入效果

```python
timeStr = '2018-01-26  12:55:20'
time.strptime(timeStr,"%Y-%m-%d  %H:%M:%S")
```

---
### 字符串格式化

|    :     |       填充       |            对齐             |       宽度       |       <,>        |              <.精度>               |
| :------: | :--------------: | :-------------------------: | :--------------: | :--------------: | :--------------------------------: |
| 引导符号 | 用于填充单个字符 | <左对齐  >右对齐  ^居中对齐 | 槽设定的输出宽度 | 数字的千位分隔符 | 浮点数小数精度或字符串最大输出长度 |

>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
