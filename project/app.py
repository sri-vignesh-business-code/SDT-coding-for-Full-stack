from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secretkey'

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@$$w0rd",  # CHANGE THIS
    database="pharmacy_system"
)

cursor = db.cursor(dictionary=True)

# LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            session['user'] = username
            return redirect('/dashboard')
        else:
            return "Invalid credentials"

    return render_template('login.html')


# DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()

    # stats
    total_meds = len(medicines)
    total_stock = sum(m['quantity'] for m in medicines)
    low_stock = len([m for m in medicines if m['quantity'] <= m['threshold']])

    return render_template('dashboard.html',
                           medicines=medicines,
                           total_meds=total_meds,
                           total_stock=total_stock,
                           low_stock=low_stock)


# ADD MEDICINE
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    qty = request.form['quantity']
    threshold = request.form['threshold']

    cursor.execute(
        "INSERT INTO medicines (name, quantity, threshold) VALUES (%s, %s, %s)",
        (name, qty, threshold)
    )
    db.commit()

    return redirect('/dashboard')


# LOW STOCK API
@app.route('/low_stock')
def low_stock_api():
    cursor.execute("SELECT * FROM medicines WHERE quantity <= threshold")
    data = cursor.fetchall()
    return jsonify(data)


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)