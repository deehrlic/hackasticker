from flask import Flask, render_template, request, send_file

import render_sticker



app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("sticker.html")

@app.route("/parse",methods=['GET', 'POST'])
def gen():
    if request.method == "POST":
        name = request.form['user_i']

    render_sticker.addText(name)
    return send_file('tmp.png', mimetype='image/gif')


if __name__ == "__main__":
    app.run(debug=True)

#gs://stickermaker-62751.appspot.com/
