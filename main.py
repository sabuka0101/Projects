from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
cards = []
messages = []
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"
questions = []

@app.route('/')
def website():
    return render_template("website.html", cards=cards)

@app.route('/sign_in', methods=['GET', 'POST'])
def admin_login():
 email = request.form.get('email')
 password = request.form.get('password')

 if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
     return redirect(url_for('admin'))
 return render_template("admin_login.html")

@app.route('/admin')
def admin():
    return render_template("admin.html", messages=messages)

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

@app.route('/login')
def profile():
 return render_template("login.html")

@app.route('/posts')
def posts():
    main_posts = []
    conn = sqlite3.connect('webd.db')
    c = conn.cursor()

    search = request.args.get('search-value')
    print(search)
    if search:
        c.execute("SELECT * FROM posts WHERE title LIKE ?", ('%' + search + '%',))
    else:
        c.execute("SELECT * FROM posts")

    rows = c.fetchall()

    # Convert tuples to dictionaries
    for row in rows:
        main_posts.append(
            {'id': row[0], 'title': row[1], 'description': row[2], 'author': row[3], 'short_description': row[4]})

    return render_template('posts.html', posts = main_posts)


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
    return render_template('register.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    comment = request.form.get('comment')

    conn = sqlite3.connect('webd.db')
    conn.execute('''
                    INSERT INTO contacts (name, email, comment) VALUES (?, ?, ?)
                ''', (name, email, comment))

    conn.commit()
    conn.close()
  return render_template('contact.html')

@app.route('/admin/admin_contacts')
def admin_contacts():
    conn = sqlite3.connect('webd.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    rows = c.fetchall()
    conn.close()

    # Convert database records as dictionary
    for row in rows:
        questions.append({'id': row[0], 'name': row[1], 'email': row[2], 'question': row[3]})

    print(questions)
    return render_template('admin.html', questions=questions)

@app.route('/admin', methods = ["POST", 'GET'])
def add_item():
    print(request.method)
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        image = request.form.get('image')

        cards.append({'title': title, 'description':description, 'image':image})
        conn = sqlite3.connect('webd.db')
        c = conn.cursor()
        c.execute('SELECT * FROM contacts')
        rows = c.fetchall()
        conn.close()

        for row in rows:
            messages.append({'id': row[0], 'name': row[1], 'email': row[2], 'comment': row[3]})
        print(messages)
    return render_template("admin.html", messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
