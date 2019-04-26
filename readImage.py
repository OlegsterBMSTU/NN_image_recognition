# Данная функция читает файл записывает его в файл в массив

from PIL import Image
from array import array
import numpy as np

b = []


def readImage(fileName):
    print(readImage.__name__,"is began")
    with open(fileName, "rb") as image:
        f = image.read()    # Читаем файл
        b = bytearray(f)    # Преобразуем все в байты в двоичную систему

    with open("testFile.txt",'w') as myFile:
        # b[18] - информация о ширине в пикселях
        # b[22] - информация о высоте в пикселях
        for i in range(len(b)):
            myFile.write("%s\n" % b[i])
    f1 = open("1_r.txt", 'w')
    f2 = open("1_g.txt", 'w')
    f3 = open("1_b.txt", 'w')
    i = b[10]   #Записываем номер индекса откуда начинается значимые
    dropSizeToFile(b)
    if (((len(b)-i) % 3) != 0): #Проверяем на кратность трем для работы и
        sizeArray = ((len(b)-i)) - ((len(b)-i) % 3) # если надо то обрезаем
    else:
        sizeArray = (len(b)-i)

    while (i < sizeArray):
        f1.write("%0.17s\n" % (b[i+0] / 255.0))
        f2.write("%0.17s\n" % (b[i+1] / 255.0))
        f3.write("%0.17s\n" % (b[i+2] / 255.0))
        i = i + 3
    f1.close()
    f2.close()
    f3.close()

    # Так как в 10 бите находится информация о стартовом бите значимой информации

def dropSizeToFile(b = []):
    with open("size.txt",'w') as f:
        f.write("%s\n" % b[18])
        f.write("%s\n" % b[22])
    f.close()