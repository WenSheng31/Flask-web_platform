from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import User
from app.utils import check_db_connection

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if not check_db_connection():
        flash('無法連接到數據庫，請稍後再試。', 'danger')
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('登入成功！', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('登入失敗。請檢查您的用戶名和密碼。', 'danger')
    return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功登出。', 'success')
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if not check_db_connection():
        flash('無法連接到數據庫，請稍後再試。', 'danger')
        return render_template('register.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('該用戶名已被使用。', 'danger')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('註冊成功！請登入。', 'success')
            return redirect(url_for('main.login'))
    return render_template('register.html')
