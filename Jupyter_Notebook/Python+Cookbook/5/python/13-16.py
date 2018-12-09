
# coding: utf-8

# ### 你想获取文件系统中某个目录下的所有文件列表。

# In[6]:


import os
names = os.listdir('data')
print(names)


# ### 结果会返回目录中所有文件列表，包括所有文件，子目录，符号链接等等。如果你需要通过某种方式过滤数据，可以考虑结合os.path 库中的一些函数来使用列表推导。比如：

# In[5]:


import os.path

# Get all regular files
names = [name for name in os.listdir('data')
        if os.path.isfile(os.path.join('data', name))]
print(names)


# In[7]:


# Get all dirs
dirnames = [name for name in os.listdir('data')
           if os.path.isdir(os.path.join('data', name))]
print(dirnames)


# ### 字符串的startswith() 和endswith() 方法对于过滤一个目录的内容也是很有用的。比如：
# 

# In[9]:


txtfiles = [name for name in os.listdir('data')
           if name.endswith('.txt')]
print(txtfiles)


# #### 对于文件名的匹配，你可能会考虑使用glob 或fnmatch 模块。比如：

# In[13]:


import glob
pyfiles = glob.glob('data/*.txt')
print(pyfiles)

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('data')
          if fnmatch(name, '*.txt')]
print(pyfiles)


# ### 获取目录中的列表是很容易的，但是其返回结果只是目录中实体名列表而已。如果你还想获取其他的元信息，比如文件大小，修改时间等等，你或许还需要使用到os.path 模块中的函数或着os.stat() 函数来收集数据。比如：

# In[18]:


# Exmaple of getting a directory listing
import time
#time.ctime(os.path.getmtime('data'))
import os
import os.path
import glob

txtfiles = glob.glob('data/*.txt')

# Get file sizes and modification dates
name_sz_data = [(name, os.path.getsize(name), os.path.getmtime(name))
               for name in txtfiles]
for name, size, mtime in name_sz_data:
    print(name, size, time.ctime(mtime))
    
# Alternative: Get file metadata
file_metadata = [(name, os.stat(name)) for name in txtfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, time.ctime(meta.st_mtime))

