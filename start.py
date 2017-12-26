#! /usr/bin/env python

import os

print("******************** 开始启动django项目！***********************")
val = os.system("python manage.py runserver 192.168.8.23:9081")
print(val)
