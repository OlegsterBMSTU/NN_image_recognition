import numpy as np
from main import Point
from main import newPoint
from random import randrange


coordinate = newPoint()
p = Point()

options = {
    0: "1_r.txt",
    1: "1_r.txt",
    2: "1_g.txt",
    3: "1_g.txt",
    4: "1_b.txt",
    5: "1_b.txt",
}

def choiseFile(i,j):   # Выбирает конкретный файл для объекта
    if (i==0):         # Если это самая первая свертка то выбираем входной файл
        fileName = options[j]
    else:
        fileName = "matrixWork"+str(i-1)+str(j)+".txt"  # иначе выбираем рабочие файлы
    return fileName

def takeSigma(value):  # Берем нужную сигму
    fileName = "__inputMlp.txt"
    with open(fileName, 'r') as f:
        sigmaSet = np.asfarray(f.readlines(), float)
    f.close()
    return sigmaSet[value]

def work(coordinate1,coordinate2):
    text = str(coordinate1)+str(coordinate2)+".txt"
    fileName = "matrixWork"+text
    with open(fileName,'r') as f:
        outputArray = np.asfarray(f.readlines(),float)  # filling array of output data
    # transform 1d to 2d array, where 1 side is  equality square root from length of array
    outputArray = np.reshape(outputArray,(-1,int(len(outputArray)**(1/2))))
    f.close()
    fileName = "exitConvolution"+text
    with open(fileName,'r') as f:
        middleArray = np.asfarray(f.readlines(),float)
    middleArray = np.reshape(middleArray,(-1,int((len(middleArray)**(1/2)))))
    f.close()
    fileName = choiseFile(coordinate1,coordinate2)  # Выбираем либо файл r,g,b, либо matrixWork
    with open(fileName,'r') as f:
        inputArray = np.asfarray(f.readlines(),float)
    inputArray = np.reshape(inputArray,(-1,int((len(inputArray)**(1/2)))))
    f.close()

# Выбираем 2 массива на вход и исходя из рандомного выбора номера ячейки мы ищем координаты в среднем массиве
# Рандомом берем из outputArray ячейку и владея информацией о ней находим ее положение в middleArray а за тем в inputArray;
    coordinate = newPoint()
    number = randrange(0, (len(outputArray) ** 2))
    p.i = number // len(outputArray)
    p.j = number % len(outputArray)
    for i in range(p.i * 4, p.i * 4 + 4):
        for j in range(p.j * 4, p.j * 4 + 4):
            if outputArray[p.i][p.j] == middleArray[i][j]:  # Подумать. Возможно надо middle & input
                coordinate.i = i
                coordinate.j = j
                coordinate.value = number
    print(coordinate.value)
    # Берем нужный набор весов
    fileName = "Core"+text      # Выбираем нужный набор весов
    with open(fileName,'r') as f:
        weightArray = np.asfarray(f.readlines(),float)
    f.close()

    sigma = takeSigma(coordinate.value)

    newWeightArray = []
    print(inputArray)
    for i in range(coordinate.i,coordinate.i+5):
        for j in range(coordinate.j,coordinate.j+5):
            newWeightArray.append(weightArray[i]+1*sigma*inputArray[i][j])
    fileName = "__Core"+text
    with open(fileName,'w') as f:
        for i in str(newWeightArray):
            f.write("%0.17f\n" % fileName)
    f.close()


