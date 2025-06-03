from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    items = []
    conn = sqlite3.connect('my_blogs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()

    # Convert tuples to dictionaries
    for row in rows:
        items.append({'id': row[0], 'title': row[1], 'description': row[2], 'author': row[3], 'short_description': row[4]})

    return render_template('index.html', items=items)


@app.route('/add_question', methods=['POST'])
def add_question():
    name = request.form.get('name')
    mail = request.form.get('mail')
    question = request.form.get('question')

    # Create record to database
    conn = sqlite3.connect('my_blogs.db')

    conn.execute('''
                 INSERT INTO contacts (name, email, question)
                 VALUES (?, ?, ?)
                 ''', (name, mail, question))
    conn.commit()
    conn.close()
    return render_template('contact.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts')
def posts():
    main_posts = []
    conn = sqlite3.connect('my_blogs.db')
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


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        conn = sqlite3.connect('my_blogs.db')
        c = conn.cursor()
        c.execute("SELECT email, password FROM users WHERE email = ?", (user_email,))
        rows = c.fetchall()
        print(rows)
        if rows:
            database_password = rows[0][1]

            if database_password == user_password:
                return redirect(url_for('admin'))
        conn.close()

    return render_template('sign_in.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/admin/admin_contacts')
def admin_contacts():
    conn = sqlite3.connect('my_blogs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    rows = c.fetchall()
    conn.close()

    # Convert database records as dictionary
    questions = []
    for row in rows:
        questions.append({'id': row[0], 'name': row[1], 'email': row[2], 'question': row[3]})

    print(questions)
    return render_template('admin_contacts.html', questions=questions)


@app.route('/admin/create_items', methods=['GET', 'POST'])
def create_items():
    conn = sqlite3.connect('my_blogs.db')
    if request.method == 'POST':
        title = request.form.get('title')
        short_description = request.form.get('short_description')
        description = request.form.get('description')
        author = request.form.get('author')

        conn.execute('''
                     INSERT INTO posts (title, short_description, description, author)
                     VALUES (?, ?, ?, ?)
                     ''', (title, short_description, description, author))
        conn.commit()

    posts = []
    c = conn.cursor()
    c.execute("SELECT * FROM posts")
    rows = c.fetchall()
    conn.close()

    # Convert tuples as dictionaries
    for row in rows:
        posts.append({'id': row[0], 'title': row[1], 'description': row[2], 'author': row[3], 'short_description': row[4]})

    return render_template('create_items.html', posts=posts)

@app.route('/admin/delete_item/<int:id>')
def delete_item(id):
    conn = sqlite3.connect('my_blogs.db')
    conn.execute('''
        DELETE FROM posts WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('create_items'))

@app.route('/admin/update_item/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    posts = []
    conn = sqlite3.connect('my_blogs.db')

    if request.method == 'GET':
        c = conn.cursor()
        c.execute(''' SELECT * FROM posts WHERE id = ? ''', (id,))
        rows = c.fetchall()
        conn.close()

        # Convert tuples as dictionaries
        for row in rows:
            posts.append(
                {'id': row[0], 'title': row[1], 'description': row[2], 'author': row[3], 'short_description': row[4]})

        return render_template('update_item.html', post = posts[0])
    else:
        title = request.form.get('title')
        short_description = request.form.get('short_description')
        description = request.form.get('description')
        author = request.form.get('author')

        conn.execute(''' UPDATE posts SET title = ?, short_description = ?, description = ?, author = ? WHERE id = ? ''',
                     (title, short_description, description, author, id))
        conn.commit()
        conn.close()

        return redirect(url_for('create_items'))

@app.route('/posts/<int:id>')
def show_post(id):
    post = []

    conn = sqlite3.connect('my_blogs.db')
    c = conn.cursor()
    c.execute(''' SELECT * FROM posts WHERE id = ? ''', (id,))
    rows = c.fetchall()

    for row in rows:
        post.append(
            {'id': row[0], 'title': row[1], 'description': row[2], 'author': row[3], 'short_description': row[4]})
    return render_template('show_post.html', post = post[0])

if __name__ == '__main__':
    app.run(debug=True)