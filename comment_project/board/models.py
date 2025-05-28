from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)   # 留言者姓名，最長 50 字元
    message = models.TextField()    # 留言內容，無長度限制
    created_at = models.DateTimeField(auto_now_add=True)    # 留言建立時間，自動填入目前時間