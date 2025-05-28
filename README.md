# 112403012-hw3 - Django 留言板專案

## 專案介紹（Description）
本專案是一個簡易的留言板後端，使用 Django 框架實作。  
目標：提供 API 讓前端可以**取得所有留言**與**新增留言**，留言資料會儲存在 SQLite 資料庫。  
本專案為「後端」作業，前端沿用 HW2 的 HTML/JS，或用 Postman 測試 API。

---

## 運行環境需求（Requirement）
- Python 3.8 以上
- Django 4.x 以上（建議使用最新版）
- 作業系統：Windows、Mac 或 Linux 皆可

---

## .env 設定（.env Setting）
本專案不需額外 .env 設定，資料庫預設為 SQLite。

---

## 安裝與運行步驟（Build Setup - Local）

1. **建立虛擬環境（建議）**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    # 或 source venv/bin/activate  # Mac/Linux
    ```

2. **安裝 Django**
    ```bash
    pip install django
    ```

3. **進入專案資料夾**
    ```bash
    cd comment_project
    ```

4. **資料庫遷移**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **啟動伺服器**
    ```bash
    python manage.py runserver
    ```

6. **API 測試方式**
    - 取得留言（GET）：  
      `http://127.0.0.1:8000/api/comments/`
    - 新增留言（POST）：  
      `http://127.0.0.1:8000/api/post/`  
      POST Body 範例（JSON）：
      ```json
      {
        "name": "你的名字",
        "message": "留言內容"
      }
      ```

## 專案結構說明
112403012-hw3/
├── comment_project/
│   ├── board/              # 留言板 app
│   ├── comment_project/    # Django 專案設定
│   ├── manage.py
├── README.md


## 注意事項（Warning）
- 本專案僅提供留言新增與查詢，不含刪除功能。
- 預設資料庫為 SQLite，若需更換請自行修改 settings.py。
- 若需整合前端，請將前端 HTML 放入 board/templates/board/ 並調整 view。