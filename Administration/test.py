import os, flask, SQLAlchemy, Bcrypt, MySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'sqlpassword'
app.config['MYSQL_DB'] = 'face_recognition'

mysql = MySQL(app)

