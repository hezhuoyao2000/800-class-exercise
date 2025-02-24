from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')
@app.route('/to_second_page')
def to_second_page():
    return render_template('secondpage.html')

@app.route('/to_third_page')
def to_third_page():
    return render_template('thirdpage.html')

if __name__ == '__main__':
    app.run(debug=True)
