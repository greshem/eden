# def 定义函数
def getscore():
    f = open('1234.txt', mode='r')      
    context = f.read()                                        
    print(context)
    f.close()
    

#调用100次函数    
for each in range(0,100,1):
   getscore()
#write_score()