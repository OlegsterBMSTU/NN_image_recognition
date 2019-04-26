"""
This file is not worked. It was corrected and rewrite to new file: mlp.py
This file needs to delete
"""



#Здесь будет находиться MLP сеть с двумя скрытыми слоями и одним выходом. Входной слой inputMLP бует содержать
# количество нейронов равное количетву выходных данных второй половины matrixWork. Далее inputMLP будет передаваться
# в первый скрытый слой по связи 1 к 1, следовательно в первом скрытом слое будет столько же элементов.
# Первый и второй скрытые слои будут связаны по приципу каждый-с-каждым, при этом количество элементов второго
# скрытого слоя будет равным количеству элементов первого скрытого слоя. Второй скрытый слой будет взаимодействовать с
# выходным слоем, состоящим из 1 элемента, по принципу каждый-к-одному.

import numpy as np
from classSystem import Neurons
from math import exp
import backPropogation
from main import Stop
from main import contollerOfError
global key

step = 1.0      # learning speed

options = {
    30: 0.3,
    70: 0.7,
}

def activation(arg):
    return  (1/ (1+exp(-arg)))  # f(x) = 1 / (1+exp(-x))    f'(x) = f(x)*(1-f(x))
def derivative(func):
    return func*(1-func)

global weightMlp0
global weightMlp1
global weightMlp2
global inputNeurons



def dropObjectToFile(obj, fileName):
    with open(fileName,'w') as f:
        for i in range(obj.__len__()):
            f.write("%0.15f\n" % obj[i].value)
            f.write("%0.15f\n" % obj[i].sigma)
    f.close()

def copyObject(obj):
    return obj;


def getFileOfObjects(filename):
    with open(filename,'r') as f:
        arr = np.asfarray(f.readlines(),float)
    f.close()
    listOfObjects = []
    k=0
    for i in range(0,len(arr),2):
        listOfObjects.append(Neurons(arr[i]))
        listOfObjects[k].sigma = arr[i+1]
        k=+1
    return listOfObjects

def rewriteObjetFile(fileName):
    with open(fileName,'w') as f:
        return 0





def readDataForInputMlp():
    key = False
    inputMlpArray = []
    arr = []
    for i in range(6):      #читываем все рабочие матрицы
        fileName = "matrixWork"+str(i)+"1.txt"
        with open(fileName,'r') as f:
            arr = f.readlines() # чтение
            arr = np.asfarray(arr,float)    # преобразование во loat
        inputMlpArray.extend(arr)   #Собрали 6 по 196 массивов в одном
    inputNeurons = []
    for i in range(len(inputMlpArray)):
        inputNeurons.append(Neurons(inputMlpArray[i]))  #создали мноество объектов
    for i in range(len(inputMlpArray)):
        inputNeurons[i].value = activation(inputNeurons[i].value)   # рогнали через функцию активации
    dropObjectToFile(inputNeurons, "__inputMlp_before.txt")
    # записали все массивы в файл
    fileName = "weight_mlp0.txt"
    with open(fileName,'r') as f:
        weightMlp0 = np.asfarray(f.readlines(),float)   # Массив весов от входногодо 1 скрытого
    weightMlp0 = np.reshape(weightMlp0,(-1,1176))   # сделали двумерный массив для организации связи каждый с каждым
    print("in the MLP function weightMlp0 size is:", weightMlp0.size,weightMlp0.__len__(),len(weightMlp0),weightMlp0.shape)
    f.close()
    fileName = "weight_mlp1.txt"
    with open(fileName, 'r') as f:
        weightMlp1 = np.asfarray(f.readlines(),float)   # Массив весов 1 скрытого до 2 скрытого
    weightMlp1 = np.reshape(weightMlp1,(-1,2000))       # преобразовали в двумерный массив 1176 х 2000
    f.close()
    fileName = "weight_mlp2.txt"
    with open(fileName, 'r') as f:
        weightMlp2 = np.asfarray(f.readlines(),float)   # Массив весов 2 скрытого до выходного
    f.close()
    hidden1 = []                                        # Массив объектов нейронов 1 скрытого слоя
    hidden2 = []         # Массив объектов нейронов 2 скрытого слоя
    for i in range(weightMlp0.__len__()): hidden1.append(Neurons(0))
    #print("hidden1_len=",hidden1.__len__(),hidden1.__sizeof__(),len(hidden1))
    for i in range(2000): hidden2.append(Neurons(0))  # Создаем 2000 объектов класса Нейронов с начальным значением переменной =0
    #print("hidden2_len=",hidden2.__len__(),hidden2.__sizeof__(),len(hidden2))
    #print("inputNeurons_len=",inputNeurons.__len__())
    #print("weightMlp0_len=",weightMlp0.size)
    #print("hidden_len=",hidden1.__len__())
    print("hidden1_len = ",hidden1.__len__(),hidden1.__sizeof__())
    print("weightMlp0_len=",weightMlp0.size, weightMlp0.__len__(),weightMlp0.shape)
    print("inputNeuron is len=",inputNeurons.__len__())
    for i in range(0,inputNeurons.__len__()):
        for j in range(0,weightMlp0.__len__()):
            hidden1[j].value+= weightMlp0[i][j] * inputNeurons[i].value #Связь каждый с каждым. Не важно сколько данных на входе, нейронов один черт 1176
    for i in range(hidden1.__len__()):
        hidden1[i].value = activation(hidden1[i].value) # прогоняем через функцию активации для получения знаячения
    print("hidden1_len=", hidden1.__len__(), len(hidden1))
    for i in range(hidden1.__len__()):
        for j in range(2000):
            hidden2[j].value += weightMlp1[i][j] * hidden1[i].value # Расчитываем переменную в скрытом слое
    for i in range(2000):
        hidden2[i].value = activation(hidden2[i].value)  # Через функцию активации гоним нейронв 2 скрытого слоя
    print("hidden2_len=", hidden2.__len__(), len(hidden2))
    outputNeuron = Neurons(0)
    for i in range(len(hidden2)):
        outputNeuron.value += weightMlp2[i]*hidden2[i].value
    outputNeuron.value = activation(outputNeuron.value)

    dropObjectToFile(inputNeurons,"__inputMlp.txt")
    dropObjectToFile(hidden1, "__hidden1.txt")
    dropObjectToFile(hidden2, "__hidden2.txt")

    control = contollerOfError(outputNeuron.value, 2)
    outputNeuron.sigma = (1-outputNeuron.value) if int(control[0])==1 else (-(1-outputNeuron.value))
    print("output=", outputNeuron.value)
    print("sigma=" , outputNeuron.sigma)
    with open("__outputNeuron.txt", 'w') as f:
        f.write("%0.17f\n" % outputNeuron.value)
        f.write("%0.17f\n" % outputNeuron.sigma)
    f.close()
    fileName = "__inputMlp.txt"
    newList = getFileOfObjects(fileName)
    #Stop()

    print(outputNeuron.value, "outputNeuron.value<0.7" if int(control[0])==1 else "outputNeuron.value>0.3")
    if (outputNeuron.value<0.7) if int(control[0])==1 else (outputNeuron.value>0.3):    # If the face then 1st condition and else 2nd condition
        print(int(control[0])==1)
        print("condition +")
        backPropogation(weightMlp0, weightMlp1, weightMlp2) #
        key = True

    else:
        key = False
        #Stop()
        print("condition -")

def backPropogation(weightMlp0 = [], weightMlp1 = [], weightMlp2 = []):
    fileName = "__outputNeuron.txt"
    outputNeuron = getFileOfObjects(fileName)
    fileName = "__inputMlp.txt"
    inputNeurons = getFileOfObjects(fileName)
    fileName = "__hidden1.txt"
    hidden1 = getFileOfObjects(fileName)
    fileName = "__hidden2.txt"
    hidden2 = getFileOfObjects(fileName)
    #Переопределяем сигмы для каждого нейров на каждом слое
    # correct = 1 - output.result
    # sigma_new = sum(weight[i][j]*correct)
    for i in range(0,len(hidden2)):   # От выхода ко второму скрытому
        hidden2[i].sigma = weightMlp2[i]*outputNeuron[0].sigma
    for i in range(0,len(hidden1)):
        hidden1[i].sigma =0.0  # обнулили сигмы перед началом новго прохода
    # От второго скрытого к первому скрытому
    for i in range(0,hidden1.__len__()):   # От второго скрытого к первому скрытому
        for j in range(0,weightMlp1.__len__()):
            hidden1[i].sigma += weightMlp1[i][j] * outputNeuron[0].sigma
    # От первого скрытого к входным данным
    for i in range(0,inputNeurons.__len__()):
        for j in range(0,weightMlp0.__len__()):
            inputNeurons[i].sigma += weightMlp0[i][j]*outputNeuron[0].sigma
    #Переопределяем веса в массивах. Для этого идем од входного к выходному
    file = open("weight_mlp0.txt",'w')
    #от входного до первого скрытого определяем набор весов
    for i in range(inputNeurons.__len__()):
        for j in range(hidden1.__len__()):
            weightMlp0[i][j] += step*hidden1[i].sigma*derivative(activation(hidden1[i].value))*inputNeurons[i].value
        file.write("%0.17f\n"%weightMlp0[i][j])
    file.close()
    file = open("weight_mlp1.txt", 'w')
    for i in range(hidden1.__len__()):
        for j in range(2000):
            weightMlp1[i][j]+= step * hidden2[j].sigma * derivative(activation(hidden2[i].value))*hidden1[i].value
            file.write("%0.17f\n" % weightMlp1[i][j])
    file.close()
    file = open("weight_mlp2.txt", 'w')
    for i in range(len(weightMlp2)):
        weightMlp2[i]+=step*outputNeuron[0].sigma * derivative(activation(outputNeuron[0].value))*hidden2[i].value
        file.write("%0.17f\n"%weightMlp2[i])
    file.close()
    dropObjectToFile(inputNeurons,"__inputMlp.txt")
    dropObjectToFile(hidden1, "__hidden1.txt")
    dropObjectToFile(hidden2, "__hidden2.txt")
    print(backPropogation.__name__+"is completed")

