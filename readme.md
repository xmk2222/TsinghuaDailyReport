### 清华日报

学生健康和出行情况报告每日自动提交

### 使用说明

* pip install -r requirements.txt
* 配置 conf.ini 输入清华info 用户名与密码
* python report.py
* 创建定时任务 Windows/Linux

如果你没有服务器，或者自己电脑也不能保证都开启，
那么使用Github Action可以作为你的服务器,并且非常安全。

下面介绍如何使用Github Action 定时执行该项目
* 创建github账户
* fork该仓库到你的项目，下面都是设置你的项目
* 设置-> Secrets-> 添加 USER_NAME 与 USER_PASS为你Info的用户名与密码
![添加Secrets](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/c.png)
* 

[Windows 创建定时任务](https://www.cnblogs.com/wensiyang0916/p/5773828.html)

### 效果图
![效果图1](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/a.png) 
![效果图2](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/b.png) 
