import os, flask, SQLAlchemy, Bcrypt, MySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'sqluser'
app.config['MYSQL_PASSWORD'] = 'sqlpassword'
app.config['MYSQL_DB'] = 'face_recognition'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cur = mysql.connection.cursor()
    teacher = cur.fetchone()
    cur.close()

    if teacher and bcrypt.check_password_hash(teacher[2], password):
        sessions['teacher_id'] = teacher[0]
        return redirect(url_for('dashboard'))
    else:
        return "Invalid username or password"

@app.route('/dashboard')
def dashboard():
    if 'teacher_id' not in session:
        return redirect(url_for('home'))
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()

    return render_template('dashboard.html', students=students)
