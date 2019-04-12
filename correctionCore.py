import numpy as np
from common import Point
from random import randrange
from common import Stop


coordinate = Point()
p = Point()
outputArray = []
middleArray = []
inputArray = []

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

def getArrays(i,j): # Заполняем массивы данных. Переменные глобальны
    fileName = "matrixWork"+str(i)+str(j)+".txt"
    print(fileName)
    with open(fileName,'r') as f:
        outputArray = np.asfarray(f.readlines(),float)  # filling array of output data
    # transform 1d to 2d array, where 1 side is  equality square root from length of array
    outputArray = np.reshape(outputArray,(-1,int(len(outputArray)**(1/2))))
    f.close()
    fileName = "exitConvolution"+str(i)+str(j)+'.txt'
    print(fileName)
    with open(fileName,'r') as f:
        middleArray = np.asfarray(f.readlines(),float)
    middleArray = np.reshape(middleArray,(-1,int((len(middleArray)**(1/2)))))
    f.close()
    fileName = choiseFile(i,j)  # Выбираем либо файл r,g,b, либо matrixWork
    print(fileName)
    with open(fileName,'r') as f:
        inputArray = np.asfarray(f.readlines(),float)
#    inputArray = np.reshape(inputArray,(-1,int(len(inputArray)**(1/2)))) #надо продумать обрезку краты.
    f.close()
    choiseCoordinate(outputArray,middleArray)
    writeNewCore(i,j,inputArray)



# Выбираем 2 массива на вход и исходя из рандомного выбора номера ячейки мы ищем координаты в среднем массиве
# Рандомом берем из outputArray ячейку и владея информацией о ней находим ее положение в middleArray а за тем в inputArray;
def choiseCoordinate(outputArray = [], middleArray = []):
    number = randrange(0,len(outputArray))
    p.i = number//len(outputArray)
    p.j = number % len(outputArray)
    for i in range(p.i*4,p.i*4+4):
        for j in range(p.j*4,p.j*4+4):
            if outputArray[p.i][p.j] == middleArray[i][j]: # Подумать. Возможно надо middle & input
                coordinate.i = i
                coordinate.j = j
                coordinate.value = number
    #return coordinate

def takeSigma(value):    #Берем нужную сигму
    fileName = "__inputMlp.txt"
    with open(fileName,'r') as f:
        sigmaSet = np.asfarray(f.readlines(),float)
    f.close()
    return sigmaSet[value]

def takeWeightArray(i,j):                       # Берем нужный набор весов
    fileName = "Core"+str(i)+str(j)+".txt"      # Выбираем нужный набор весов
    with open(fileName,'r') as f:
        array = np.asfarray(f.readlines(),float)
    f.close()
    return array   # возвращаем массив

def writeNewCore(i,j,inputArray = []):
    adder = str(i)+str(j)
    sigma = takeSigma(coordinate.value)
    weightArray = takeWeightArray(i,j)
    newWeightArray = []
    k=0
    for i in range(coordinate.i,coordinate.i+5):
        for j in range(coordinate.j,coordinate.j+5):
            #1dsize = i * size + j
            newWeightArray.append(weightArray[k]+1*sigma*inputArray[i*int(len(inputArray)**(1/2))+j])
            k+=1
    fileName = "Core"+adder+".txt"
    with open(fileName,'w') as f:
        for i in range(len(newWeightArray)):
            f.write("%0.17f\n" % newWeightArray[i])
    f.close()

def correctionCore(i,j):
    getArrays(i,j)



