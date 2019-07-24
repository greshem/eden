# -*- coding: utf-8 -*-
#!/usr/bin/python

a=input("输入你的名字");
print("你的名字是%s"%a)

fh = open("个人信息", 'a')
fh.write("你的名字是%s"%a)
fh.close();
print("个人信息文件.txt 生成 ")

