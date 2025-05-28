from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment
import json

# 首頁 view（顯示 index.html）
def homepage(request):
    # 回傳首頁模板
    return render(request, 'index.html')

# GET API：取得所有留言
def get_comments(request):
    # 從資料庫取得所有留言，依建立時間由新到舊排序
    comments = Comment.objects.all().order_by('-created_at')
    # 將留言資料轉成 list of dict
    data = [
        {
            'name': c.name,
            'message': c.message,
            'created_at': c.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for c in comments
    ]
    # 回傳 JSON 格式的留言資料
    return JsonResponse(data, safe=False)

# POST API：新增一則留言
@csrf_exempt  # 關閉 CSRF 驗證，方便前端直接呼叫
def post_comment(request):
    if request.method == 'POST':
        try:
            # 解析前端傳來的 JSON 資料
            body = json.loads(request.body)
            name = body.get('name')
            message = body.get('message')
            # 檢查資料是否齊全
            if name and message:
                # 新增留言到資料庫
                Comment.objects.create(name=name, message=message)
                return JsonResponse({'status': 'success'})
        except Exception as e:
            # 可以加上錯誤訊息方便除錯
            return JsonResponse({'status': 'error', 'msg': str(e)}, status=400)
    # 若資料不正確或發生錯誤，回傳錯誤訊息
    return JsonResponse({'status': 'error'}, status=400)