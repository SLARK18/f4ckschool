import os

def transliterate(string, reverse=False):
    # Словарь для транслитерации
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'i', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '_',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
        'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'I', 'Ь': '',
        'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }

    # Если нужно преобразовать обратно, меняем ключи и значения местами
    if reverse:
        translit_dict = {v: k for k, v in translit_dict.items()}

    # Проходим по каждому символу в строке и транслитерируем его
    translit_string = ''
    for char in string:
        # Если символ есть в словаре, добавляем его транслитерированное значение
        translit_string += translit_dict.get(char, char)

    return translit_string

def papki(way):
    all_items = os.listdir(way)

    # Фильтруем только папки
    folders = [item for item in all_items if os.path.isdir(os.path.join(way, item))]

    # Сортируем список папок по времени создания
    folders.sort(key=lambda x: os.path.getctime(os.path.join(way, x)))
    return dict(zip(folders, [transliterate(i) for i in folders]))


def htmli(way):
    all_items = os.listdir(way)

    # Фильтруем только HTML-документы
    html_files = [item for item in all_items if item.endswith('.html')]

    # Сортируем список HTML-документов по времени создания
    html_files.sort(key=lambda x: os.path.getctime(os.path.join(way, x)))

    return {file_name: transliterate(file_name) for file_name in html_files}

print(htmli('templates\История развития'))