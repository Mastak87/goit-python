import re

def normalize(string):
    symbols_cur = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    symbols_lat = "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"
    ord_map = {}

    for i in range(len(symbols_cur)):
        ord_map[ord(symbols_cur[i])] = ord(symbols_lat[i])

    article = re.sub(r'[\W]', '_', string)
    return article.translate(ord_map)

if __name__ == '__main__':
    print(normalize(string))