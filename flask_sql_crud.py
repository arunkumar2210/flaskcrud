from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER']='sql6406402'
app.config['MYSQL_PASSWORD']='E6FYnzyHHE'
app.config['MYSQL_HOST']='sql6.freemysqlhosting.net'
app.config['MYSQL_DB']='sql6406402'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql=MySQL(app)

@app.route('/')
def Index():
    return render_template('index_sql.html')
    cur = mysql.connection.cursor()
#    cur.execute('''CREATE TABLE students2 (id INTEGER, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255)''')

@app.route('/insert',methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO students2 (name,email,phone) VALUES (%s, %s, %s)",(name,email,phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)