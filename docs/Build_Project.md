# 创建项目

#### 创建项目文件夹
```bash
mkdir Course
```

#### 创建虚拟环境
```bash
cd Course
pipenv install
```

#### 激活虚拟环境
```bash
pipenv shell
```

#### 安装 `Django` 框架
```bash
pipenv install django
```

#### 创建项目
```bash
django-admin startproject config .
```
`config` 项目名称
`.` 当前目录下 

#### 创建应用`apps`
我这里把所有单个 `app`应用到放到了 `apps`文件夹下面
```bash
django-admin startapp users
```
1. 把 `users`模块文件夹移动到`apps`文件夹下面
2. 修改`users/apps.py`  
```python
from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = '用户'
```
3. 添加应用到 `DJANGO_APPS` 中
```python

# Django框架 自带的apps应用
DJANGO_APPS = [
    'django.contrib.admin',
]
# 第三方包或者应用
THIRD_PARTY_APPS = [
]
# 自己安装的应用
LOCAL_APPS = [
    # 第一个apps 代表 目录文件夹， 第二个 apps 表示 users 文件夹下面的apps.py
    'apps.users.apps.UsersConfig',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
```

