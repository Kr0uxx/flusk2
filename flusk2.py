from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<name>')
def index(name):
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base_training.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
