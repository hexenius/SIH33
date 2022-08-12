# mongodb+srv://Hex:Hex@0987@hex.w5llgcr.mongodb.net/?retryWrites=true&w=majority
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/industry')
def industry():
    return render_template('industry.html')


@app.route('/university')
def university():
    return render_template('university.html')


@app.route('/contactus')
def contactus():
    return render_template('contactus.html')


@app.route('/university_in')
def university_in():
    return render_template('university_in.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.secret_key = 'secretive'
    app.run(debug=True)

