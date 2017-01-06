# 1、安装python3.4 (CentOS6.5)
这里我们选择python3.4版本，首先是因为python3是python发展的趋势，拥有更好更简洁的语言设计，同时也是因为后期我们的Django项目1.9.5适用于python3.4

** 1.1 首先我们先安装以下Python的依赖包: **


    # yum groupinstall "Development tools"
    # yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make


** 1.2 我们将 python3.4.5 的源文件下载到 `/usr/local/src` 目录下：**


    # wget https://www.python.org/ftp/python/3.4.5/Python-3.4.5.tar.xz


** 1.3 解压缩并安装 **


    # tar Jxvf Python-3.4.5.tar.xz
    # cd Python-3.4.5
    # ./configure --prefix=/usr/local/python34  （指定安装路径）
    # make -j8 && make install   （指定使用8核cpu进行编译安装，-j后面的参数根据你的cpu核数设定）



** 1.4 修改 `/usr/bin/` 目录下的python相关文件 **
默认系统使用的 `python` , `pip` 等相关命令使用的是Python2.6，我们修改为我们新安装的python3.4

将 `/usr/local/python34/bin/` 下面的可执行文件都考到 `/usr/bin/` 目录下，进行修改：


    # cp /usr/local/python34/bin/* /usr/bin/
    # mv python python.bak
    # ln -s python3 python
    # mv pip pip.bak
    # ln -s pip3 pip
    # mv easy_install easy_install.bak
    # ln -s easy_install-3.4 easy_install
 

** 1.5 查看python等安装情况 **


    # python --version
    Python 3.4.5
    # pip --version
    pip 8.1.1 from /usr/local/python34/lib/python3.4/site-packages (python 3.4)
    # easy_install --version
    setuptools 20.10.1 from /usr/local/python34/lib/python3.4/site-packages (Python 3.4)



# 2、Python虚拟环境安装


    $ sudo pip install virtualenv
    $ sudo pip install virtualenvwrapper


# 3、上述工具装好后找不到mkvirtualenv命令，需要执行以下环境变量设置


    1.创建目录用来存放虚拟环境
    $ mkdir $HOME/.virtualenvs
    2.在~/.bashrc中添加行：
    $ export WORKON_HOME=$HOME/.virtualenvs
    3.在~/.bashrc中添加行：
    $ source /usr/local/python34/bin/virtualenvwrapper.sh
    4.运行:
    $ source ~/.bashrc
    5.添加virtualenv 可执行文件到/usr/bin中
    $ cp /usr/local/python34/bin/virtualenv /usr/bin/


如果设置完环境变量后还是不行，每次在workon 之前，先执行


   $  source /usr/local/python34/bin/virtualenvwrapper.sh


# 4、虚拟环境相关操作


    mkvirtualenv [虚拟环境名称]
    workon [虚拟环境名称]
    离开 deactivate
    rmvirtualenv [虚拟环境名称]













