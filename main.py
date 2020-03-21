from pytube import YouTube

def progress_function(chunk, file_handle, bytes_remaining):
  print(round((1-bytes_remaining/vid.filesize)*100, 3), '% done...')

path = 'https://www.youtube.com/watch?v=R3AKlscrjmQ'
yt = YouTube(path)
print(yt.streams.all)

vid = yt.streams.get_highest_resolution()
print('Начало скачивания.')
vid.download('C:/Users/Admin/Downloads')
print('Файл скачан.')
