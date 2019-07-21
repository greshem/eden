def getscore():
    f = open('1234.txt', mode='r')      
    context = f.read()                                        
    print(context)
    f.close()
    
def write_score():
    f = open('1234.txt', mode='a')      
    context = f.write("333333")                                        
    print(context)
    f.close()
    
#for each in range(0,100,1):
#   getscore()
write_score()