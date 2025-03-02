from flask import Flask, render_template, url_for
import os
import glob
from function import transliterate, papki, htmli


MENU_LIST = papki('templates')
inv_MENU_LIST = {value: key for key, value in MENU_LIST.items()}


application = Flask(__name__)

@application.route('/')
def hello():
    return render_template("base_text_info.html", html_stat=open(r'templates\История развития\Первые компьютерные сети.html', encoding='utf-8').read(), menu_list=MENU_LIST)

@application.route('/proverka')
def rtest():
    return render_template("base_text_info.html", html_stat=open(r'templates\История развития\Первые компьютерные сети.html', encoding='utf-8').read(), menu_list=MENU_LIST)


@application.route('/<chapter>/')
def show_chapter(chapter):
    page_dict = htmli(f'templates\{inv_MENU_LIST[chapter]}')
    inv_page_dict = {value: key for key, value in page_dict.items()}
    return render_template("base_text_info.html", html_stat=open(f'templates\{list(inv_MENU_LIST.keys()).index(chapter) + 1}.html', encoding='utf-8').read(), menu_list=MENU_LIST, left_menu=page_dict, chapter=chapter)

@application.route('/<chapter>/<page>/')
def show_pages(chapter, page):
    page_dict = htmli(f'templates\{inv_MENU_LIST[chapter]}')
    inv_page_dict = {value: key for key, value in page_dict.items()}
    return render_template("base_text_info.html", html_stat=open(f'templates\{inv_MENU_LIST[chapter]}\{inv_page_dict[page]}.html', encoding='utf-8').read(), menu_list=MENU_LIST, left_menu=page_dict, chapter=chapter)


"""
@application.route('/<chapter>/<page>')
def show_page(chapter, page):
    html_files = glob.glob(os.path.join(f'templates/{chapter}', '*.html'))
    file_names = []
    for file_path in html_files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_names.append(file_name)
    return render_template("base_text_info.html", menu_list=MENU_LIST)
"""

if __name__ == '__main__':
    application.run(debug=True)