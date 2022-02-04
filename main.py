from flask import Flask, render_template, request, redirect, send_from_directory
from replit import db
import os
import random
import string
import pickledb

piccle = pickledb.load('database.db', True)

def getString(length):
    return ''.join(random.choices(string.ascii_letters+string.digits, k=length))


app = Flask(__name__)

db["test"] = "https://youtube.com"
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("POST")
        keyword = getString(1900) + "=="
        link = request.form.get("link")
        if "https://" not in link:
            link = "https://" + link
        piccle.set(keyword, link)
        #db[keyword] = str(link)
        print(f"{keyword}:{link}")
        return render_template("index.html", keyword=keyword)
    
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/<e>")
def lonklink(e):
    return redirect(piccle.get(e), code=302)

@app.route("/lincc", methods=['GET', 'POST'])
def lincc():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        return redirect(db[keyword], code=302)
    return render_template("lincc.html")

@app.route("/api")
def api():
    link = request.args.get("lincc")
    if "https://" not in link:
        link = "https://" + link
    keyword = getString(500)
    db[keyword] = str(link)
    return keyword


# print(getString(500))
app.run(host='0.0.0.0')