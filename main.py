from flask import Flask, render_template, request

app = Flask(__name__)

questions = [{"name": "saba", "email":"sabashavbalakhashvili@gmail.com", "comment": "blablablu"}
]
@app.route('/')
def home():
    return render_template('website.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/add_question')
def add_question():
    name = request.form.get('name')
    email = request.form.get('email')
    comment = request.form.get('comment')
if __name__ == "__main__":
    app.run(debug = True)