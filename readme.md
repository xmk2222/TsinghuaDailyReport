## 清华日报

学生健康和出行情况报告每日自动提交

建议使用第二种方式，简单易行.


### 正常使用说明

* pip install -r requirements.txt
* 配置 conf.ini 输入清华info 用户名与密码
* python report.py
* 创建定时任务 Windows/Linux
> [Windows 创建定时任务](https://www.cnblogs.com/wensiyang0916/p/5773828.html)


### 非正常使用说明
> 如果你没有服务器，或者自己电脑也不能保证都开启，
那么使用Github Action可以作为你的服务器,并且非常安全。
>
#### 使用Github Action自动定时执行
* 创建github账户
* fork该仓库到你的项目，下面都是设置你的项目
* 设置-> Secrets-> 添加 USER_NAME 与 USER_PASS为你Info的用户名与密码
![添加Secrets](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/c.png)
* 进入 Action 点击 Understand

OK !

说明:
Github Action的配置文件(.github/workflows/deploy.yml)中配置了时间 
默认是北京时间10:00 可以自行修改



### 效果图
![效果图1](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/a.png) 
![效果图2](https://github.com/naihaishy/TsinghuaDailyReport/blob/master/results/b.png) 
