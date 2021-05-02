from pathlib import Path
import pprint
import re
import shutil
import os


image_files = set()
video_files = set()
documents_files = set()
music_files = set()
archive_files = set()
folder_names = set()
unknown_extensions = set()
all_extensions = set()

image_extensions = {'.jpg', '.png', '.jpeg', '.svg'}
video_extensions = {'.avi', '.mp4', '.mov', '.mkv'}
documents_extensions = {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'}
music_extensions = {'.mp3', '.ogg', '.wav', '.amr'}
archive_extensions = {'.rar', '.zip', '.gz', '.tar'}


def normalize(string):
    symbols = ("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

    tr = {ord(a): ord(b) for a, b in zip(*symbols)}

    article = re.sub(r'[\W]', '_', string)
    return article.translate(tr)


def garbage(path):

    for i in path.iterdir():

        if i.is_dir():
            garbage(Path(path.home(),i))

        elif i.suffix in image_extensions:
            image_files.add(f'{normalize(i.stem)}{i.suffix}')
            all_extensions.add(i.suffix)
            if not os.path.exists(os.path.join('C:\garbage', 'images')):
                os.mkdir(os.path.join('C:\garbage', 'images'))
            if not os.path.exists('C:\\garbage\\images\\'+ i.name):
                shutil.move(i, r'C:\garbage\images')
                os.rename(r'C:\\garbage\\images\\' + i.name, f'C:\\garbage\\images\\{normalize(i.stem)}{i.suffix}')



        elif i.suffix in video_extensions:
            video_files.add(f'{normalize(i.stem)}{i.suffix}')
            all_extensions.add(i.suffix)
            if not os.path.exists(os.path.join('C:\garbage', 'video')):
                os.mkdir(os.path.join('C:\garbage', 'video'))
            if not os.path.exists('C:\\garbage\\video\\' + i.name):
                shutil.move(i, r'C:\garbage\video')
                os.rename(r'C:\\garbage\\video\\' + i.name, f'C:\\garbage\\video\\{normalize(i.stem)}{i.suffix}')

        elif i.suffix in documents_extensions:
            documents_files.add(f'{normalize(i.stem)}{i.suffix}')
            all_extensions.add(i.suffix)
            if not os.path.exists(os.path.join('C:\garbage', 'documents')):
                os.mkdir(os.path.join('C:\garbage', 'documents'))
            if not os.path.exists('C:\\garbage\\documents\\' + i.name):
                shutil.move(i, r'C:\garbage\documents')
                os.rename(r'C:\\garbage\\documents\\' + i.name, f'C:\\garbage\\documents\\{normalize(i.stem)}{i.suffix}')

        elif i.suffix in music_extensions:
            music_files.add(f'{normalize(i.stem)}{i.suffix}')
            all_extensions.add(i.suffix)
            if not os.path.exists(os.path.join('C:\garbage', 'audio')):
                os.mkdir(os.path.join('C:\garbage', 'audio'))
            if not os.path.exists('C:\\garbage\\audio\\' + i.name):
                shutil.move(i, r'C:\garbage\audio')
                os.rename(r'C:\\garbage\\audio\\' + i.name, f'C:\\garbage\\audio\\{normalize(i.stem)}{i.suffix}')

        elif i.suffix in archive_extensions:
            archive_files.add(f'{normalize(i.stem)}{i.suffix}')
            all_extensions.add(i.suffix)
            if not os.path.exists(os.path.join('C:\garbage', 'archives')):
                os.mkdir(os.path.join('C:\garbage', 'archives'))
            if not os.path.exists('C:\\garbage\\archives\\'+ i.stem):
                shutil.move(i, r'C:\garbage\archives')
                shutil.unpack_archive(r'C:\\garbage\\archives\\' + i.name, f'C:\\garbage\\archives\\{i.stem}')


        else:
            unknown_extensions.add(i.suffix)

def del_folder(path):

    for del_folder in path.iterdir():
        try:
            Path.rmdir(del_folder)
        finally:
            continue

def rename_folder(path):

    for rename_folder in path.iterdir():

        if rename_folder.is_dir():
            try:
                os.rename(rename_folder, f'{rename_folder.parent}\\{normalize(rename_folder.name)}')
            finally:
                continue


if __name__ == '__main__':
    print(garbage(Path('C:\garbage')))
    print(del_folder(Path('C:\garbage')))
    print(rename_folder(Path('C:\garbage')))

    pprint.pprint(image_files)
    pprint.pprint(video_files)
    pprint.pprint(documents_files)
    pprint.pprint(music_files)
    pprint.pprint(archive_files)

    print(unknown_extensions)
    print(all_extensions)