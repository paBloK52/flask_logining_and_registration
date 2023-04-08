from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, UserMixin
from app import exm
from app import login_manager


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


users = {
    "1": User("1", "admin", "password"),
    "2": User("2", "user", "password")
}


@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


@exm.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = str(len(users) + 1)
        user = User(user_id, username, password)
        users[user_id] = user
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


@exm.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = None
        for u in users.values():
            if u.username == username and u.password == password:
                user = u
                break
        if not user:
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))
    return render_template('login.html')


@exm.route('/')
@login_required
def home():
    return render_template('home.html')
