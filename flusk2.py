from flask import Flask, request, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    astronautId = StringField('ID астронавта', validators=[DataRequired()])
    astronautPassword = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitanId = StringField('ID астронавта', validators=[DataRequired()])
    capitanPassword = PasswordField('Пароль астронавта', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Доступ')


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    spis = ['Нил Армстронг', 'Уоррен Баффетт', 'Иван Грозный', 'Тутанхамон', 'Леонардо да Винчи', 'Брюс Уэйн']
    return render_template('distribution.html', spis=spis)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
