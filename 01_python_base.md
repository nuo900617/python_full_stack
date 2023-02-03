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

## 文件
1. 文件编码
- 字符串->字节  
  - 'xx'.encode('utf-8')
- 字节->字符串
  - 'xx'.decode('gbk') 

2. 打开文件/操作文件/关闭文件
```python
f = open('文件路径', mode='wb/ab')
f.write('xx'.encode('utf-8'))
f.flush()
f.close()
```
```python
f = open('文件路径', mode='rb)
data = f.read()
f.close()
content = data.decode('utf-8')
```

3. 关于模式  
**mode = 'w'**，encoding='utf-8'时，可以直接写入字符串，内部给做转换
```python
f = open('文件路径', mode='w', encoding='utf-8')
f.write('xx')
f.close()
```
```python
f = open('文件路径', mode='r', encoding='utf-8')
content = f.read()
f.close()
```

- 如果文档写入的是字符串、文本，建议mode='w'/'r'
- 图片/视频/gif文件, 建议mode='wb'/'rb'

4. 大文件  
```python
f = open('文件路径', mode='r', encoding='utf-8')
content = f.read()  # 所有内容直接读取到内存
f.close()
```

```python
f = open('文件路径', mode='r', encoding='utf-8')
# 一行一行的读取文件
for line in f:
  line = line.strip()
  if not line:
    continue
  print(line)
f.close()
```

- 网络传输大文件
```python
import os 
total_size = os.stat('**.mp4').st_size #获取文件大小
f = open('**.mp4', mode='rb')
has_read_size = 0
while has_read_size < total_size:
  chunk = f.read(3) # 读3个字节
  has_read_size += len(chunk)

f.close()
```