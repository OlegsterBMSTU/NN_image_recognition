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
from common import Stop
global key

step = 0.7      # learning speed

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
            f.write("%0.17f\n" % obj[i].value)
            f.write("%0.17f\n" % obj[i].sigma)

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
    for i in range(6):
        fileName = "matrixWork"+str(i)+"1.txt"
        with open(fileName,'r') as f:
            arr = f.readlines()
            arr = np.asfarray(arr,float)
        inputMlpArray.extend(arr)   #Собрали 6 по 196 массивов в одном
    inputNeurons = []
    for i in range(len(inputMlpArray)):
        inputNeurons.append(Neurons(inputMlpArray[i]))
    for i in range(len(inputMlpArray)):
        inputNeurons[i].value = activation(inputNeurons[i].value)

    # записали все массивы в файл
    fileName = "weight_mlp0.txt"
    with open(fileName,'r') as f:
        weightMlp0 = np.asfarray(f.readlines(),float)   # Массив весов от входногодо 1 скрытого
    print(len(weightMlp0))
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

    for i in range(weightMlp0.size):
        #hidden1.append(Neurons(1/(1+exp(weightMlp0[i]*inputNeurons[i].value))))
        hidden1.append(Neurons(activation(inputNeurons[i].value)))  # Создаем объекты 1 скрытого слоя, прогоняя через сигмоиду сразу

    for i in range(2000) : hidden2.append(Neurons(0))   #Создаем 2000 объектов класса Нейронов с начальным значением переменной =0
    for i in range(len(weightMlp1)):
        for j in range(2000):
            hidden2[j].value += weightMlp1[i][j] * hidden1[i].value # Расчитываем переменную в скрытом слое
    for i in range(2000):
        hidden2[i].value = activation(hidden2[i].value)  # Через функцию активации гоним нейронв 2 скрытого слоя

    outputNeuron = Neurons(0)
    for i in range(len(hidden2)):
        outputNeuron.value += weightMlp2[i]*hidden2[i].value
    outputNeuron.value = activation(outputNeuron.value)

    dropObjectToFile(inputNeurons,"__inputMlp.txt")
    dropObjectToFile(hidden1, "__hidden1.txt")
    dropObjectToFile(hidden2, "__hidden2.txt")
    print("Objects have dropped")

    outputNeuron.sigma = 1-outputNeuron.value
    print("output=", outputNeuron.value)
    print("sigma=" , outputNeuron.sigma)
    with open("__outputNeuron.txt", 'w') as f:
        f.write("%0.17f\n" % outputNeuron.value)
        f.write("%0.17f\n" % outputNeuron.sigma)
    f.close()
    fileName = "__inputMlp.txt"
    newList = getFileOfObjects(fileName)
    print(len(newList))
    Stop()
    if outputNeuron.value < 0.7:
        backPropogation(weightMlp0, weightMlp1, weightMlp2)
        key = True
    else:
        key = False
        #Stop()

def backPropogation(weightMlp0 = [], weightMlp1 = [], weightMlp2 = []):
    print(backPropogation.__name__,"is began")
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
    print("outputNeuron[0].value=",outputNeuron[0].value)
    print("outputNeuron[0].sigma=", outputNeuron[0].sigma)
    for i in range(len(hidden2)):   # От выхода ко второму скрытому
        hidden2[i].sigma = weightMlp2[i]*outputNeuron[0].sigma
    for i in range(len(hidden1)):
        hidden1[i].sigma =0.0  # обнулили сигмы перед началом новго прохода
    # От второго скрытого к первому скрытому
    for i in range(len(hidden1)):   # От второго скрытого к первому скрытому
        for j in range(len(hidden2)):
            hidden1[i].sigma += weightMlp1[i][j] * outputNeuron[0].sigma
    # От первого скрытого к входным данным
    for i in range(len(hidden1)):
        inputNeurons[i].sigma = weightMlp0[i]*outputNeuron[0].sigma
    #Переопределяем веса в массивах. Для этого идем од входного к выходному
    file = open("weight_mlp0.txt",'w')
    #от входного до первого скрытого определяем набор весов
    for i in range(len(weightMlp0)):
        weightMlp0[i] += step*hidden1[i].sigma*derivative(activation(hidden1[i].value))*inputNeurons[i].value
        file.write("%0.17f\n"%weightMlp0[i])
    file.close()
    file = open("weight_mlp1.txt", 'w')
    for i in range(len(weightMlp1)):
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
    print("Objects have dropped")
    print(backPropogation.__name__, "is finished")


