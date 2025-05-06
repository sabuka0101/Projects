from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
cards = []
messages = []

@app.route('/')
def website():
    return render_template("website.html", cards=cards)

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

@app.route('/login')
def profile():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('webd.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO website (username, email, password) VALUES (?, ?, ?)
            ''', (username, email, password))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    comment = request.form.get('comment')

    messages.append({'name': name, 'email': email, 'comment': comment})
    return redirect(url_for('add_item'))
  return render_template('contact.html')

@app.route('/admin', methods = ["POST", 'GET'])
def add_item():
    if request.method == 'POST':
        print(request.form)
        title = request.form.get('title')
        description = request.form.get('description')
        image = request.form.get('image')

        cards.append({'title': title, 'description':description, 'image':image})
        print(cards)
        return redirect(url_for('website'))
    return render_template("admin.html", messages=messages)

if __name__ == '__main__':
    app.run(debug=True)