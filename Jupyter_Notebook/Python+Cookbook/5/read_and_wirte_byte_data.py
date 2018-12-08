
# coding: utf-8

# In[1]:


# Read the entire file as a single byte string
with open('data.bin', 'rb') as f:
    data = f.read()
    print(data)


# In[2]:


# Write binary data to a file 
with open('data.bin', 'wb') as f:
    f.write(b'Hello World')


# 在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个
# 潜在的陷阱。特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符
# 串。比如：

# In[3]:


# Text string
t = 'Hello World'
for i in t:
    print(i)


# In[4]:


# Byte string
b = b'Hello World'
for i in b:
    print(i)


# 如果你想从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编
# 码操作。比如：

# In[5]:


with open('data.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
    print(text)

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))


# 二进制I/O 还有一个鲜为人知的特性就是数组和C 结构体类型能直接被写入，而
# 不需要中间转换为自己对象。比如：

# In[ ]:


测试一下

