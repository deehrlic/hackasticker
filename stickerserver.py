from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("sticker.html")

@app.route("/parse",methods=['GET', 'POST'])
def gen():
    return 1;

if __name__ == "__main__":
    app.run(debug=True)
