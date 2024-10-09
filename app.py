from app import create_app, db
from app.utils import check_db_connection

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        if check_db_connection():
            db.create_all()
            print("數據庫連接成功，並創建了所有表。")
        else:
            print("警告：無法連接到數據庫。請檢查你的數據庫設置。")
    app.run(debug=True)
