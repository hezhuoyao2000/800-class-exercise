from flask import Flask, render_template
app = Flask(__name__) 
@app.route("/")
def hello_flask():
    return "<p>This is the third page!</p>"

@app.route('/to_home_page')
def home():
    return render_template('homepage.html')

@app.route('/to_third_page')
def to_third_page():
    return render_template('thirdpage.html')