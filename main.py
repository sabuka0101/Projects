from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cards = []
messages = []

@app.route('/')
def website():
    return render_template("website.html", cards=cards)

@app.route('/profile')
def profile():
    return render_template("profile.html")


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