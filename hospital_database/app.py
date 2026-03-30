from flask import Flask, render_template, request, redirect, session
import MySQLdb
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY

db = MySQLdb.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    passwd=MYSQL_PASSWORD,
    db=MYSQL_DB
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
        result = cur.fetchone()

        if result:
            session['user'] = user
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    cur = db.cursor()
    cur.execute("SELECT * FROM medicines")
    medicines = cur.fetchall()

    return render_template('dashboard.html', medicines=medicines)


@app.route('/add', methods=['GET', 'POST'])
def add_medicine():
    if 'user' not in session:
        return redirect('/')

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        expiry = request.form['expiry']

        cur = db.cursor()
        cur.execute(
            "INSERT INTO medicines (name, quantity, price, expiry_date) VALUES (%s, %s, %s, %s)",
            (name, quantity, price, expiry)
        )
        db.commit()

        return redirect('/dashboard')

    return render_template('add_medicine.html')


@app.route('/delete/<int:id>')
def delete_medicine(id):
    if 'user' not in session:
        return redirect('/')

    cur = db.cursor()
    cur.execute("DELETE FROM medicines WHERE id=%s", (id,))
    db.commit()
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)