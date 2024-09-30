import os
import time

dirctory = os.getcwd()
os.chdir('/Users/Mauzer33/UrbanProjects/pythonProject1/Module_8')

files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]

for root, dirs, files in os.walk(dirctory):
  for file in files:
    filepath = os.path.join(dirctory,file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')