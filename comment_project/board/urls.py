from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),                     # 首頁
    path('api/comments/', views.get_comments),    # GET：取得留言列表
    path('api/post/', views.post_comment),        # POST：新增留言
]
