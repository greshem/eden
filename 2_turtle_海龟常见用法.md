
#2019_06_10_09:55:57   Monday   add by greshem

# 1. range 奇数打印 
## python代码
``` python
for each in range(1,100,1)
    print each
```


## shell代码
``` bash
    for each in $(seq  1 100)
    do
        echo $each
    done
```
        
# 2. range 偶数打印 
## python代码
``` python
for each in range(0,99,2)
    print each
```


## shell代码
``` bash
    for each in $(seq  0 99 2 )
    do
        echo $each
    done
```

# 3. 随机 #
## 随机画圆

    - [随机画圆]()
    - [pygame 随机画圆]()
    - [随机线条]


# 4.  markdown 部署任务 
    docker run -p 8889:33333   -it -v /root/bin/swcloud/:/tmp/mkdocs/markdown_docs/docs/       qianzhongjie/mkdocs  



# 5. 网盘的搭建 
``` bash
    file boswer  和目录之间的管理  文件的创建 等等   显示一下 

    3. 二进制执行:
    wget https://github.com/filebrowser/filebrowser/releases/download/v2.0.12/linux-amd64-filebrowser.tar.gz
    cd /mnt/ &&  filebrowser  -r ./ -a 0.0.0.0  -p 33331
```

# 6. devpi的搭建  
``` bash
docker run -d --name devpi \
    --publish 3141:3141 \
    --volume /opt/devpi_data:/data \
    --env=DEVPI_PASSWORD=devapiPasswd \
    --restart always \
    muccg/devpi
```

    

# 7. gitlab 的搭建 

# 8.  github 代码下载克隆 
        项目的提交  

# 9. mkdocs 的搭建 
    任务列表的搭建 

# 10. 在线 平台的搭建

# 11. 算法可视化平台搭建 
