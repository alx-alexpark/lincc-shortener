from flask import Flask, render_template, request, redirect
from replit import db


app = Flask(__name__)

db["test"] = "https://youtube.com"
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("POST")
        keyword = request.form.get("keyword")
        link = request.form.get("link")
        if "https://" not in link:
            link = "https://" + link
        db[keyword] = str(link)
        print(f"{keyword}:{link}")
    
    return render_template("index.html")

@app.route("/<e>")
def lonklink(e):
    return redirect(db[e], code=302)





app.run(host='0.0.0.0')