while True:
    a1=input("请输入你的名字");
    print("你的名字是【%s】"%a1);
    
    a2=input("请输入你的班级");
    print("你的班级是【%s】"%a2);
    
    a3=input("请输入你的年级");
    print("你的年级是【%s】"%a3);
    
    a4=input("请输入你的性别");
    print("你的性别是【%s】"%a4);
    
    a5=input("请输入你的出生日期");
    print("你的出生日期是【%s】"%a5);
    
    a6=input("请输入你的年龄");
    print("你的年龄是【%s】"%a6);
    
    f=open("affff/个人信息.txt", "w+");
    f.write("你的名字是【%s】\n"%a1);
    f.write("你的班级是【%s】\n"%a2);
    f.write("你的年级是【%s】\n"%a3);
    f.write("你的性别是【%s】\n"%a4);
    f.write("你的出生日期是【%s】\n"%a5);
    f.write("你的年龄是【%s】\n"%a6);
    
    f.close()
    print("文件写入成功")
    