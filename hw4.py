from pathlib import Path
import pprint


image_files = []
video_files = []
documents_files = []
music_files = []
archive_files = []
unknown_extensions = set()
all_extensions = set()

image_extensions = {'.jpg', '.png', '.jpeg', '.svg'}
video_extensions = {'.avi', '.mp4', '.mov', '.mkv'}
documents_extensions = {'.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'}
music_extensions = {'.mp3', '.ogg', '.wav', '.amr'}
archive_extensions = {'.rar', '.zip', '.gz', '.tar'}


def garbage(path):

    for i in path.iterdir():

        if i.is_dir():
            garbage(Path(path.home(),i))

        elif i.suffix in image_extensions:
            image_files.append(i.name)
            all_extensions.add(i.suffix)

        elif i.suffix in video_extensions:
            video_files.append(i.name)
            all_extensions.add(i.suffix)

        elif i.suffix in documents_extensions:
            documents_files.append(i.name)
            all_extensions.add(i.suffix)

        elif i.suffix in music_extensions:
            music_files.append(i.name)
            all_extensions.add(i.suffix)

        elif i.suffix in archive_extensions:
            archive_files.append(i.name)
            all_extensions.add(i.suffix)
        else:
            unknown_extensions.add(i.suffix)

    return path


if __name__ == '__main__':
    print(garbage(Path('C:\garbage')))
    pprint.pprint(image_files)
    pprint.pprint(video_files)
    pprint.pprint(documents_files)
    pprint.pprint(music_files)
    pprint.pprint(archive_files)
    print(unknown_extensions)
    print(all_extensions)
