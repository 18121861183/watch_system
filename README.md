# 安装步骤

一：依赖环境安装<br/>
  1、python3+ <br/>
  2、pip3 <br/>
  3、pip install -r requirements.txt <br/>
  4、apt install mysql-server <br/>
 <br/>
 <br/>
Windows 安装<br/>
<br/>
一、python3.6版本安装：https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe<br/>
安装中选择安装全部组件并将Python应用于系统path中。验证方式：命令行敲击 	python， 成功则会进入到Python中，执行exit()退出Python系统。
Python的pip控件安装过程是自带的。正常情况下 pip list 会有相应的输出
<br/>
二、mysql数据库安装：参考https://blog.csdn.net/Liu68686868/article/details/79518471<br/>
三、解压watch_system-master.zip<br/>
四、命令行:  <br/>
	cd ./watch_system-master <br/>
	pip insatll -r requirements.txt<br/>
<br/>
五、修改配置：<br/>
	watch_system-master/watch_system/settings.py <br/>
文件中查找到下面内容，根据实际情况修改：<br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.mysql',<br/>
        'NAME': 'watch',	//数据库名<br/>
        'USER': 'root',		//数据库连接用户名<br/>
        'PASSWORD': '123456',	//数据库密码<br/>
        'HOST': '127.0.0.1',	//数据库地址<br/>
        'PORT': '3306',		//数据库端口<br/>
    }<br/>
}<br/>
<br/>
watch_system-master/agriculture/migrations 文件夹下除了__init__.py文件外，其它的文件要确保删除<br/>
<br/>
六、初始化数据库：<br/>
（1）mysql -u root -p <br/>
（2）CREATE DATABASE `'watch'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;<br/>
（3）show databases; 查看数据库是否创建成功<br/>
七、 在项目主目录下：<br/>
		python manage.py makemigrations<br/>
		python manage.py migrate<br/>
八、运行项目： python manage.py runserver 0.0.0.0:8000 <br/>
<br/>
<br/>
Linux环境安装<br/>
Ubuntu 下：(python3 默认安装的, 如果pip指令不存在，则： apt install python-pip3)<br/>
apt install mysql-server <br/>
<br/>
修改数据库密码方式：<br/>
mysql -u root -p<br/>
> use mysql <br/>
> update user set authentication_string=PASSWORD("tipDB@123") where User='root';<br/>
> update user set plugin="mysql_native_password";<br/><br/>
> flush privileges;<br/>
<br/>
解压watch_system-master.zip<br/>
命令行:  <br/>
cd ./watch_system-master <br/>
pip insatll -r requirements.txt<br/>
<br/>
修改配置：<br/>
watch_system-master/watch_system/settings.py <br/>
文件中查找到下面内容，根据实际情况修改：<br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.mysql',<br/>
        'NAME': 'watch',	//数据库名<br/>
        'USER': 'root',		//数据库连接用户名<br/>
        'PASSWORD': '123456',	//数据库密码<br/>
        'HOST': '127.0.0.1',	//数据库地址<br/>
        'PORT': '3306',		//数据库端口<br/>
    }<br/>
}<br/>
watch_system-master/agriculture/migrations 文件夹下除了__init__.py文件外，其它的文件要确保删除<br/>
<br/>
初始化数据库：<br/>
（1）mysql -u root -p <br/>
（2）CREATE DATABASE `'watch'` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;<br/>
（3）show databases; 查看数据库是否创建成功<br/>
 在项目主目录下：<br/>
		python manage.py makemigrations<br/>
		python manage.py migrate<br/>
运行项目： python manage.py runserver 0.0.0.0:8000 <br/>
<br/>
<br/>
<br/>
<br/>
# 初始化数据：
连接数据库：<br/>
agriculture_webinfo表中增加9条数据：<br/>
	id字段从1-9<br/>
	status选项：safe,leak,online,offline,danger<br/>
1	四川农业网	http://1.1.1.1	safe,leak,online<br/>
2	农信网	http://14324.fgds2	safe,danger,online<br/>
3	test3	test3	online,danger <br/>
4	test4	test4	online,safe <br/>
5	test5	test5	online,leak <br/>
6	test6	test6	offline,danger <br/>
7	test7	test7	online,safe <br/>
8	test8	test8	online,danger <br/>
9	test9	test9	online,safe <br/>
<br/>
<br/>

# 网站详细信息编辑：
参考 web详细信息编辑格式.json 格式



