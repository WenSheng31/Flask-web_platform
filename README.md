# 基於Flask的登入系統

## 專案概述

這是一個使用 Flask 框架開發的 web 應用模板，集成了用戶認證系統和響應式設計。本專案旨在提供一個穩固的起點，可以快速開發具有用戶管理功能的網站。
當然這只是一個練習專案，仍有許多不完整的部分，我會在學習過程中逐漸完善功能。

### 主要特點

- 使用 Flask 框架
- Bootstrap 響應式前端設計
- 用戶認證系統（註冊、登入、登出）
- MySQL 數據庫集成
- 環境變量配置管理

## 使用技術

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- MySQL
- Bootstrap 5

## 安裝指南

1. Clone儲存庫：
   ```
   git clone https://github.com/WenSheng31/Flask-web_platform.git
   cd Flask-web_platform
   ```

2. 創建並啟動虛擬環境：
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. 安裝依賴：
   ```
   pip install -r requirements.txt
   ```

4. 設置環境變量：(這個步驟跳過，直接編輯config.py內容即可使用)
   - 複製 `.env.example` 到 `.env`
   - 編輯 `.env` 文件，設置你的環境變量

5. 初始化數據庫：
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. 運行應用：
   ```
   flask run
   ```

## 項目結構

```
Flask-web_platform/
├── app/
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── index.html
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── utils.py
├── .env
├── .env.example
├── config.py
├── requirements.txt
├── .gitignore
├── README.md
└── run.py
```

## 使用指南

- 訪問 `http://localhost:5000` 來查看首頁
- 使用 `/register` 路徑來註冊新用戶
- 使用 `/login` 路徑來登入
- 使用 `/logout` 路徑來登出

## 開發

- 遵循 PEP 8 編碼規範
- 使用有意義的提交信息
- 定期更新 `requirements.txt`

## 待辦事項

- [ ] 實現密碼重置功能
- [ ] 添加用戶個人資料頁面
- [ ] 實現電子郵件驗證
- [ ] 添加單元測試
- [ ] 設置 CI/CD 管道
