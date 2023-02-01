## 基础
1. 字符串扩展名
   - data = text.rsplit('.', maxsplit=1) 
     - data[0]：文件名
     - data[1]: 扩展名
```python
text = '123.png'
data = text.rsplit('.', maxsplit=1)
```

2. 字符串连接
```python
l = ['v1', 'v2', 'v3']
con = '_'.join(l)
```

3. 去除首尾空白 strip
```python
text = '   你好，世界!   '
data = text.strip()
```

4. 是否是整数字符串
```python
data = '123a'
data.isdecimal()
```

5. 元组tuple
   - v1 = (11)    # v1 = 11
   - v2 = (11, )  # v2是元组
```python
v1 = (11)
v2 = (11, )
print(type(v1), type(v2)) 
# int, tuple
```

## 编码和字节
1. 编码
- ascii编码， 256种对应关系，1个字节表示对应关系
- GB2312/GBK编码，亚洲国家文字，2个字节表示对应关系
- unicode，万国码，4个字节表示对应关系
  - 好处：可以包括所有文字
  - 坏处：浪费存储空间
  - 网络传输或文件存储，将其进行压缩
- utf-8编码，对unicode进行压缩处理
  - v2 = v1.encode('utf-8') --- 字节类型 bytes
  - v1 = v2.decode('utf-8') --- 字符串类型 str -> unicode

2. 文件操作
```python
name = '你好'
data = name.encode('utf-8')
f = open('a.txt', mode='wb')
f.write(data)
f.close()
``` 
