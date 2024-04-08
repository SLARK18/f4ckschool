from flask import Flask, render_template, url_for
import os
import glob
from function import transliterate, papki


MENU_LIST = papki('templates')
inv_MENU_LIST = {value: key for key, value in MENU_LIST.items()}


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("base_text_info.html", html_stat=open(r'templates\История развития\Первые компьютерные сети.html', encoding='utf-8').read(), menu_list=MENU_LIST)

@app.route('/<chapter>/')
def show_chapter(chapter):
    return render_template("base_text_info.html", html_stat=open(f'templates\{list(inv_MENU_LIST.keys()).index(chapter) + 1}.html', encoding='utf-8').read(), menu_list=MENU_LIST)

"""
@app.route('/<chapter>/<page>')
def show_page(chapter, page):
    html_files = glob.glob(os.path.join(f'templates/{chapter}', '*.html'))
    file_names = []
    for file_path in html_files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_names.append(file_name)
    return render_template("base_text_info.html", menu_list=MENU_LIST)
"""

if __name__ == '__main__':
    app.run(debug=True)