from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from webapp import app
from .forms import ContactForm




app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config['MAIL_USERNAME'] = 'moonutside@gmail.com'
app.config['MAIL_PASSWORD'] = 'moonut2016HOME'


@app.route("/")
def home():
    return render_template('home.html', title='Главная')


@app.route("/sbornik-ot-raskata-do-prosveta")
def sbornik_ot_raskata_do_prosveta():
    return render_template('sbornik-ot-raskata-do-prosveta.html', title='Сборник «От раската до просвета»')


@app.route("/layout")
def layout():
    return render_template('layout.html')


@app.route("/about")
def about():
    return render_template('about.html', title='О сайте')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('Заполните все поля.')
            return render_template('contact.html', title='Для связи', form=form)

        else:
            msg = Message(form.subject.data, sender='moonutside@gmail.com', recipients=['slavaspetsyian@gmail.com'])
            msg.body = """
                  From: %s <%s>
                  %s
                  """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', title='Сообщение доставлено', form=form, success=True)

    if request.method == 'GET':
        return render_template('contact.html', title='Для связи', form=form)

@app.route("/terms")
def terms():
    return render_template('terms.html', title='Пользовательское соглашение')

@app.route("/faq")
def faq():
    return render_template('faq.html', title='FAQ')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html', title='Политика конфиденциальности')


# Страницы ошибок
#
# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html'), 404
#
# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'), 500


# Страницы стихов

@app.route("/sbornik-ot-raskata-do-prosveta/dorozhki")
def dorozhki():
    return render_template('./s_dorozhki.html', title='Стих «Асфальтовые дорожки»')


@app.route("/sbornik-ot-raskata-do-prosveta/otrazhenie")
def otrazhenie():
    return render_template('./s_otrazhenie.html', title='Стих «Отражение невыспаных лиц»')


@app.route("/sbornik-ot-raskata-do-prosveta/oslablo")
def oslablo():
    return render_template('./s_oslablo.html', title='Стих «Ослабло нашей страсти пламя»')


@app.route("/sbornik-ot-raskata-do-prosveta/zamok")
def zamok():
    return render_template('./s_zamok.html', title='Стих «Оставлен навеки у моря утес»')


@app.route("/sbornik-ot-raskata-do-prosveta/vpopyat")
def vpopyat():
    return render_template('./s_vpopyat.html', title='Стих «Впопят к минулому»')


@app.route("/sbornik-ot-raskata-do-prosveta/chto-yest-chelovek")
def chto_yest_chelovek():
    return render_template('./s_chto-yest-chelovek.html', title='Стих «Что есть человек?»')


@app.route("/sbornik-ot-raskata-do-prosveta/chudnyi-son")
def chudnyi_son():
    return render_template('./s_chudnyi-son.html', title='Стих «Чудный сон!»')


@app.route("/sbornik-ot-raskata-do-prosveta/dym")
def dym():
    return render_template('./s_dym.html', title='Стих «Дым кудрявый»')


@app.route("/sbornik-ot-raskata-do-prosveta/korabli")
def korabli():
    return render_template('./s_korabli.html', title='Стих «Корабли»')


@app.route("/sbornik-ot-raskata-do-prosveta/mig")
def mig():
    return render_template('./s_mig.html', title='Стих «Прекрасный миг»')


@app.route("/sbornik-ot-raskata-do-prosveta/nebo")
def nebo():
    return render_template('./s_nebo.html', title='Стих «Небо тень заволокла»')


@app.route("/sbornik-ot-raskata-do-prosveta/posvyatite")
def posvyatite():
    return render_template('./s_posvyatite.html', title='Стих «Посвятите хотя бы минутку»')


mail = Mail(app)