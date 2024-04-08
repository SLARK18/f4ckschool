from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("base_text_info.html", html_stat=open(r'C:\Users\User\Desktop\Новая папка (5)\f4ckschool1\templates\ГЛАВА 1\Что такое инетрнет.html', encoding='utf-8').read())

if __name__ == '__main__':
    app.run(debug=True)