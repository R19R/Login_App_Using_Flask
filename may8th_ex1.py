'''creating a form using flask to get username and password using html
and displaying success on submitting'''


from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/success", methods = ['POST', "GET"])
def success():
    if request.method == 'POST':
        result = request.form
        uname = request.form['username']
        return render_template("success.html", result= result, username=uname)


if __name__ == '__main__':
    app.run(debug=True)