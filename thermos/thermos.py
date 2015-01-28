from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash

#from logging import DEBUG

app = Flask(__name__)
#app.logger.setLevel(DEBUG)
bookmarks = []
app.config['SECRET_KEY'] = 'l\xa9\x8e\xfc\xf0\x0b\x92\x07\x7f\x1e\xa5\xbd\xa3A\x00\x9c\x86\xde\xff+G\xee\x8f~'

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
        ))
    
class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = "Title passed from view to template", user = User("Shuyi", "Wang"))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
