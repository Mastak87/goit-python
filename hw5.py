<<<<<<< HEAD
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
=======
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
>>>>>>> 492d567535fd87630f4246a13d9c88d79e629be2
    print(normalize(string))