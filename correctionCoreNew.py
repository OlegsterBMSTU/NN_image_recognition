import numpy as np
from main import Point
from random import randrange
from main import Stop
#from mlp import getFileOfObjects

step = 0.5

"""
1. Для каждой ячейки outputArray определить где она находится в middleArray - Ok
2. Для каждой найденной ячейки в middleArray найти набор из inputArray с помощью которых она была образована - Ok
3. Зная положение определим сигмы для каждой ячейки в middleArray. Желательно использовать ООП.
4. После получения всех сигм переопределить веса  CoreXX.txt
5. Повоторить все это для кадой ячейки в outputArray, при этом использовать новые значения CoreXX.txt
"""

class forCoreWeight(Point):
    sigma:float
    value:float
    coord_i:int
    coord_j:int



listData = []
coordinates = forCoreWeight()

options = {
    0: "1_r.txt",
    1: "1_r.txt",
    2: "1_g.txt",
    3: "1_g.txt",
    4: "1_b.txt",
    5: "1_b.txt",
}



def choiseFile(i,j):   # Выбирает конкретный файл для объекта
    if (j==0):         # Если это самая первая свертка то выбираем входной файл
        fileName = options[i]
    else:
        fileName = "matrixWork"+str(i)+str(j-1)+".txt"  # иначе выбираем рабочие файлы
    return fileName

def transferArray(array = []):
    return array

def fillingArray(index1,index2):
    global inputArray
    global middleArray
    global outputArray
    fileName = "matrixWork"+str(index1)+str(index2)+".txt"
    with open(fileName,'r') as f:
        outputArray = np.asfarray(f.readlines(),float)
        outputArray = np.reshape(outputArray,(-1,int(len(outputArray)**(1/2))))    # квадратая матрица
    f.close()
    fileName = "exitConvolution" + str(index1)+str(index2) + '.txt'
    with open(fileName,'r') as f:
        middleArray = np.asfarray(f.readlines(),float)
        middleArray = np.reshape(middleArray,(-1,int(len(middleArray)**(1/2))))
    f.close()
    fileName = choiseFile(index1, index2)  # Выбираем либо файл r,g,b, либо matrixWork
    with open(fileName,'r') as f:
        inputArray = np.asfarray(f.readlines(),float)
        #inputArray = np.reshape(inputArray,(-1,int(len(inputArray)**(1/2))))   will be using 1d array This is simpler
    f.close()
    print("filling inputArray.len=", inputArray.__len__(), inputArray.__sizeof__(), len(inputArray))
    print("filling middleArray.len=", middleArray.__len__(), middleArray.__sizeof__(), len(middleArray))
    print("filling outputArray.len=",outputArray.__len__(),outputArray.__sizeof__(),len(outputArray))

def choiseCoordinateInTheMiddleArray():
    print("choiseFunction inputArray.len=", inputArray.__len__(), inputArray.__sizeof__(), len(inputArray))
    print("choiseFunction middleArray.len=", middleArray.__len__(), middleArray.__sizeof__(), len(middleArray))
    print("choiseFunction outputArray.len=",outputArray.__len__(),outputArray.__sizeof__(),len(outputArray))
    print()
    #for i in range(0,outputArray.__len__()): listData.append(Point())     # create array of objects
    lenListArray = int(len(outputArray)**2)
    for i in range(0,lenListArray):listData.append(forCoreWeight())
    for i in range(0,lenListArray): listData[i].value = outputArray[int(i//len(outputArray))][int(i%len(outputArray))]     # Заполнили даннми
    for k in range(0,lenListArray):
        key = True
        listData[k].i = k // len(outputArray)       # Write i coordinate
        listData[k].j = k % len(outputArray)        # Write j coordinate
        for i in range(listData[k].i*4, listData[k].i*4+4):
            for j in range(listData[k].j*4,listData[k].j*4+4):
                if (outputArray[k // len(outputArray)][k % len(outputArray)] == middleArray[i][j]) and (key == True):
                    listData[k].coord_i = i
                    listData[k].coord_j = j
                    key = False







def correctionCore(index1,index2):
    print("indexes:",index1,index2)
    fillingArray(index1,index2)
    choiseCoordinateInTheMiddleArray()
    return 0