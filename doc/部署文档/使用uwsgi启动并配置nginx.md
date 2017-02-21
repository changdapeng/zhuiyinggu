# 一、使用uwsgi启动django
<br/>
## 1、安装uwsgi
进入到cms的虚拟环境中
<br/>


    $ pip install uwsgi


<br/>
<br/>

## 2、在zhuiyinggu项目的根目录下创建uwsgi.ini文件，其配置内容如下：
<br/>


    [uwsgi]
    socket = 127.0.0.1:8034
    #http = 本机的外网IP:55555
    chdir = /home/webpy/zhuiyinggu/
    wsgi-file = zhuiyinggu/wsgi.py
    processes = 4
    threads = 2
    master = True
    pidfile = uwsgi.pid
    daemonize = uwsgi.log


+ socket:    标识被代理转发，当我们使用nginx做负载均衡时，使用此功能。
+ http:      标识自己作为web服务器，使用uwsgi直接提供服务时，使用此功能。
+ chdir:     项目的根目录。
+ wsgi-file: 项目的管理目录，相对于uwsgi.ini文件路径的相对路径即可。
+ processes: 开启的进程数
+ threads:   每个进程开启的线程数
+ master:    是否开启主进程
+ pidfile:   指定保存uwsgi主进程的进程号的文件
+ deamonize: 配置日志文件路径，注销此选项，默认为调试模式


<br/>
<br/>

## 3、关闭django的调试模式，添加静态文件路径：
<br/>

编辑settings.py文件，修改或添加下面的选项：


    DEBUG = False  # 关闭调试模式

    ALLOWED_HOSTS = ['*',]  # 允许所有的主机访问

    # 确认django.contrib.staticfiles 包含在你的INSTALLED_APPS 中。
    STATIC_URL = '/static/'  # 指定静态资源的URL路径
    STATIC_ROOT='/home/webpy/static_data/'  # 指定我们存储的静态资源文件路径


    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )  # 指定其他存放静态资源文件的路径



<br/>
<br/>

# 4、部署静态文件
<br/>


    $ python manage.py collectstatic


<br/>
<br/>

## 5、使用uwsgi启动django


    $ uwsgi --ini uwsgi.ini
    [uWSGI] getting INI configuration from uwsgi.ini



#### uwsgi的相关命令：


    启动： uwsgi --ini uwsgi.ini
    重新读取配置文件： uwsgi --reload uwsgi.ini
    停止服务： uwsgi --stop uwsgi.pid


<br/>
<br/>

# 二、安装并配置Nginx
<br/>

## 1、安装nginx：


    # yum install nginx
    # nginx -v  # 查看Nginx版本
    nginx version: nginx/1.10.2


<br/>
<br/>

## 2、修改Nginx的配置文件
<br/>

我们在Nginx的配置文件中添加server模块。由于不同操作系统不同Linux版本的配置文件位置可能不同，此处我们修改的文件位置为/etc/nginx/conf.d/default.d，你也可以直接在nginx.conf配置文件的http模块中添加一个server模块。


    # vim /etc/nginx/conf.d/default.conf
    #
    # The default server
    #

    server {
        listen       80 default_server;  # 指定我们要监听的端口 80
        server_name  www.zhuiyinggu.com;  # 指定我们的虚拟机的名字，当我们使用www.zhuiyinggu.com域名访问的使用，匹配到此虚拟机来处理请求。
        root         /usr/share/nginx/html; 

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            include /etc/nginx/uwsgi_params;
            uwsgi_pass 127.0.0.1:8034;  # 指定我们uwsgi启动的IP和Port
        }     
             
        location /static/ {  # 指定静态资源的URL路径，为Django中 STATIC_URL配置信息。
            alias /home/webpy/static_data/;  # 指定静态资源的文件路径，为Django中STATIC_ROOT配置信息。
        }   

        location /status/ { 
            stub_status;
        }

        error_page 404 /404.html;
            location = /40x.html { 
        }
        
        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }

    }


<br/>
<br/>

## 3、 启动Nginx
<br/>


    # service nginx start


#### nginx 的相关命令：


    # service nginx start  # 启动Nginx
    # service nginx status  # 查看Nginx的运行状态
    nginx (pid  10835) is running...
    # service nginx stop  # 停止Nginx
    # nginx -t  # 检查Nginx的配置文件的正确性
    # nginx -s reload  # 重新加载配置文件

