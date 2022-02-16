#!/usr/bin/env python
# coding: utf-8

# In[38]:


import os
def main(cd):
    name = os.listdir(cd)
    rr = len(name)
    for i in range(0,rr):
        nowcd = cd + r'/' + name[i]
        
        try:
            flag = 0
            newcd = cd + r'/' + name[i].encode("gbk").decode("shift-jis")
        except:
            flag = 1
            
        if flag == 1:
            try:
                flag = 0
                newcd = cd + r'/' + name[i].encode("shift-jis").decode("utf-8")
            except:
                flag = 1
                
            if flag == 1:
                print(r'reverse error!, cd %s' %nowcd)
                
        if flag == 0:
            if os.path.isdir(nowcd):
                main(nowcd)
            os.rename(nowcd,newcd)

cd = input("请输入要转换的文件夹完整目录：")
main(cd)


# In[ ]:




