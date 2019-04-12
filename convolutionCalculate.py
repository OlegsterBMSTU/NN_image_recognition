import array
from common import Point
import numpy as np
from functools import reduce
import chooseFile as cf


def convolution(index1, index2):  #Create exitConvolution.txt


    filename = (cf.optionsOfColorFile[index1]() if index2 ==0 else cf.choiseOfMatrixWorks(index1))
    print(filename)
    #Подаем определенны файл на чтение ( один из трех  цветов либо
    with open(filename,'r') as f:   #Открываем файл
        matrix = f.readlines()      # Заполняем массив matrix, в котором весь файл
        matrix = np.asfarray(matrix,float)  #Преобразуем во float
    filename = cf.optionsOfWeightConversationFile[index1]()   #файл с набором весов для передачи в Convolution Layer и далее
    with open(filename,'r') as f:
        weightConv = f.readlines()  #запимываем файл в массив weightConv
        weightConv = np.asfarray(weightConv,float) #Преобразуем во float

    #Теперь прогоняем файл через массив
    # Так как массив одномерный а использовать хотелось бы двумерный, то будем придерживаться логики, что координата в
    # двумерном массиве есть по определению:
    # координата i = номер ячейки // длина массива**1/2
    # координата j = номер ячейки % длина массива**1/2
    # соответственно чтобы вычислить координату в одномерном массиве мы будем придерживаться следующей логике:
    # Координата в массиве = i*длину массива + j
    #Массив у нас 6х4 по этому длина массиву массива принимаем за 4

    p = Point()     #юда будем подавать координаты ячейки
    p.i=0
    p.j=0
    coordinate = p.i*4+p.j
    matrix = list(map((lambda x:x*weightConv[coordinate]),matrix))  #преобразовали весь массив, умножив на вес
                                                                    # в weightConvArray

    # Теперь надо пройтись картой 5х5 по всему массиву matrix
    filename = "Core"+str(index1)+str(index2)+".txt" #Продумать функцию прохода
    with open(filename,'r') as f:
        mapWeight = f.readlines()  #запимываем файл в массив weightConv
        mapWeight = np.asfarray(mapWeight,float) #Преобразуем во float
    f.close()
    coord = Point()
    newArray = []
    timeValue =0
    sizeArray = int(((len(matrix))**(1/2))/1)
    #(n = 10) if (index2==0) else (n = 4)
    n= (int(10) if index2==0 else int(4))
    for i in range(sizeArray-n):       # Обрезаем карту. Надо срезать по уму. Было до 10 и до 4
        for j in range(sizeArray-n):
            coord.i = i * sizeArray + j
            for x in range(5): #потому что карта 5х5
                for y in range(5):
                    coord.j = x * 5 + y
                    timeValue = timeValue + matrix[coord.i+ coord.j] * mapWeight[coord.j]   #Здесь идет наращивание значени при свертке
            newArray.append(timeValue)     # собираем массив
            timeValue=0

    filename = "exitConvolution"+str(index1)+str(index2)+".txt"
    with open(filename,'w') as f:
        f.writelines("%f\n" % z for z in newArray)
    f.close()