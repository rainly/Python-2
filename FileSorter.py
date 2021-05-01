import os
import shutil
src_folder = input('输入你想整理的文件夹的绝对路径：')   #'/Users/jackeroo/Downloads/'
des_folder = input('输入整理后文件放置的文件夹绝对位置：')  #'/Users/jackeroo/Downloads/sorted/'
files = os.listdir(src_folder)
print('文件整理中...')
for file in files:
    src_path = src_folder + file
    if os.path.isfile(src_path):
        des_path = des_folder + file.split('.')[-1]
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        shutil.move(src_path,des_path)
print('文件整理完毕！')
