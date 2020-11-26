from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),

    # 用户管理
    path('users/', include('apps.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/profile/',
    #      TemplateView.as_view(template_name='profile.html')),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # 开发的应用
    path('news/', include('apps.news.urls', namespace='news')),
]
