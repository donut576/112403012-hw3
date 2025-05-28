from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('board.urls')),  # 引入 board 的 URL 路由（含首頁與 API）
    path('admin/', admin.site.urls),
]
