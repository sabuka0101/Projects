from flask import Flask, render_template, request

app = Flask(__name__)
cards = []

@app.route('/')
def home():
    return render_template("website.html")

@app.route('/admin/add_item', methods = ["POST", 'GET'])
def add_item():
    if request.method == 'POST':
        print(request.form)
        title = request.form.get('title')
        description = request.form.get('description')
        image = request.form.get('image')

        cards.append({'title': title, 'description':description, 'image': image})
        print(cards)
        return render_template("website.html", cards=cards)
    return render_template("admin.html")


if __name__ == '__main__':
    app.run(debug=True)
