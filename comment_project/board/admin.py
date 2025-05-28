from django.contrib import admin
from .models import Comment

# 將 Comment 模型註冊到 Django 後台，讓你可以在管理介面管理留言資料
admin.site.register(Comment)


