# 扫描某个github仓库的所有文件，将文件名保存到本地

import requests
import re
import os
# 仓库地址
url = 'https://github.com/liwangshengya/PyTorch-and-TF-learn'
#设置代理
proxies = {'http': 'http://127.0.0.1:10809', 'https': 'http://127.0.0.1:10809'}
r = requests.get(url, proxies=proxies)
# 读取该页面下的所有文件名
print(r.text)
with open('colab.py', 'w') as f:
    f.write(r.text)
#  href="/liwangshengya/PyTorch-and-TF-learn/blob/main/README.md">README.md</a>
file_names = re.findall(r'href="/liwangshengya/PyTorch-and-TF-learn/blob/mian/*?"', r.text)
print(file_names)
