# 尚硅谷大数据全套视频教程40阶段（2019.6月线下班）

## [安装教程](https://www.bilibili.com/video/BV1BJ411U7hW?p=100)
Linux版本：[CentOS](http://mirrors.163.com/centos/6/isos/x86_64/CentOS-6.10-x86_64-bin-DVD1.iso)
+ 自定义分区
  * / ext4 6144mb 虽然官方推荐15G
  * /boot ext4 200mb
  * NA swap 使用剩余可用
+ 最小化安装，去除java
+ 在我的host中，取名为centos01
+ root用户，密码123456 
+ yuanwei用户，密码123456


## [目录结构](https://www.bilibili.com/video/BV1BJ411U7hW?p=101)
+ **/bin** 存放最经常使用的命令
+ /sbin Super User使用的程序
+ /home 普通用户的主目录
+ /rootroot用户的主目录
+ /lib 系统开机需要的最基本的动态链接共享库
+ /lost+found 一半是空的，非法关机后存放一些文件
+ **/etc** 所有的系统管理需要的配置文件和子目录
+ **/usr** 类似于windows下面的program files目录，存放用户的应用程序及相关文件
+ **/media** 系统自动识别u盘光驱等，挂载到这个目录下
+ **/mnt** 外部的存储的**临时**挂载位置，然后就可以访问外部存储的内容
+ **/opt** 主机额外安装软件所拜访的目录。默认为空。比如安装mysql数据库就可以安装在这儿
+ **/var** 存放日志文件，不管扩充，经常修改

## [网络配置](https://www.bilibili.com/video/BV1BJ411U7hW?p=105)
首先配置主机的信息
+ ip 192.168.1.10
+ mask 255.255.255.0
+ gateway 192.168.1.2
+ DNS 114.114.114.114,8.8.8.8

然后进入centos，
