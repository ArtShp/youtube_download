from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable

import eel

from datetime import datetime


@eel.expose
def download(url, path):
    def progress_function(chunk, file_handle, bytes_remaining):
        print(round((1 - bytes_remaining / vid.filesize) * 100, 3), '% done...')

    try:
        yt = YouTube(url, on_progress_callback=progress_function)
    except VideoUnavailable:
        print(f'Видео {url} недоступно, пропускаю')
    except:
        print(f'Ошибка для видео {url}, пропускаю')
    else:
        vid = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
        #print(f'Видео {i+1} из {len(url)}')
        #print('--------------------')
        print(f'Ссылка: {url}')
        for s in yt.streams:
            print(s)
        print(f'Автор: {yt.author}')
        print(f'Название: {yt.title}')
        print(f'Длительность: {yt.length}с')
        print(f'Разрешение: {vid.resolution}')
        print(f'Размер: {round(vid.filesize/(2**20))}MB')
        print('--------------------')
        print('Начало загрузки')
        video_start = datetime.now()
        vid.download(path)
        print(f'Конец загрузки(Время: {datetime.now()-video_start})')
        print('--------------------')

    return 'Done!'

"""
urls = []

data = open('yt.txt', 'r+', encoding='utf-8')
n_data = data.readlines()
for i in range(0, len(n_data)-1):
    print(n_data[i][-1])
    if 'playlist' in n_data[i]:
        p = Playlist(n_data[i][:-1])
        for u in p.video_urls:
            urls.append(u)
    else:
        urls.append(n_data[i][:-1])
else:
    if 'playlist' in n_data[0]:
        p = Playlist(n_data[0])
        for u in p.video_urls:
            urls.append(u)
    else:
        urls.append(n_data[0])


print(f'Скачать: {len(urls)} видео')
print('--------------------')
program_start = datetime.now()

for i in range(len(urls)):
    

print(f'Конец работы(Время: {datetime.now()-program_start})')

"""

eel.init('web')
eel.start('main.html', size=(700, 700))
