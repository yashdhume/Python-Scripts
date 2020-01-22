import os
import shutil

path = input("Enter Path: ")
os.chdir(path)
listDir = os.listdir()
listDirRmFile = []
for x in listDir:
    if '.' in x:
        listDirRmFile.append(x)
print(listDirRmFile)
files = sorted(listDirRmFile, key=lambda x: os.path.splitext(x)[1])
listExt = []
for x in files:
    listExt.append(os.path.splitext(x)[1])
listExt = list(dict.fromkeys(listExt))
for x in listExt:
    if not os.path.exists(x):
        try:
            os.makedirs(x[1:])
        except:
            continue
for x in files:
    temp = os.path.splitext(x)[1]
    shutil.move(x, temp[1:])
