from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/<name>')
def index(name):
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base_training.html', prof=prof)


@app.route('/list_prof/<list_type>')
def prof_list(list_type):
    return render_template('prof_list.html', list_type=list_type)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    dictionary = {
        'title': 'И на марсе будут яблони цвести',
        'surname': 'Musk',
        'name': 'Elon',
        'education': 'Высшее',
        'profession': 'Главный колонизатор марса',
        'sex': 'male',
        'motivation': 'Всегда мечтал стать президентом Марса!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', dictionary=dictionary)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
