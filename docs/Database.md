# 增加数据库

#### 修改 `users`数据模型
```python
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    """自定义用户模型"""
    nickname = models.CharField(null=True, blank=True, max_length=255, verbose_name='昵称')
    job_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='职称')
    introduction = models.TextField(blank=True, null=True, verbose_name='简介')
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='头像')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='城市')
    personal_url = models.URLField(max_length=255, null=True, blank=True, verbose_name='个人链接')
    weibo = models.URLField(max_length=255, null=True, blank=True, verbose_name='微博链接')
    zhihu = models.URLField(max_length=255, null=True, blank=True, verbose_name='知乎链接')
    github = models.URLField(max_length=255, null=True, blank=True, verbose_name='GitHub链接')
    linkedin = models.URLField(max_length=255, null=True, blank=True, verbose_name='LinkedIn链接')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_profile_name(self):
        if self.nickname:
            return self.nickname
        return self.username

```
#### 连接数据库 `config/settings/base.py`
```python  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 提示连接mysql数据库
        'NAME': env.str('DATABASE_NAME'),  # 数据库名为test，要自己创建
        'USER': env.str('DATABASE_USERNAME'),  # 用户名
        'PASSWORD': env.str('DATABASE_PASSWORD'),  # 密码
        'HOST': env.str('DATABASE_HOST'),  # 连接的主机
        'PORT': env.str('DATABASE_PORT'),  # 对应的端口号
    }
}

AUTH_USER_MODEL = 'users.User'

```
#### 环境变量 `.env`

```bash  
# MySQL 连接配置
DATABASE_NAME=django
DATABASE_USERNAME=root
DATABASE_PASSWORD=123456
DATABASE_HOST=192.168.5.160
DATABASE_PORT=3306
```

#### 安装 `mysql`数据驱动
```bash
pipenv install mysqlclient
```
### 数模模型 `ImageField`需要的图片包扩展
```bash
pipenv install pillow
```
#### 同步数据模型
```python  
./manage.py makemigrations 
```

#### 同步数据表结构和数据迁移
```python 
./manage.py migrate
```