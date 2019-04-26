# Здесь будут расписаны разные функции mlp систпем

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

step = 0.5      # learning speed



def activation(arg):
    # воспользуемся свойством сигмоиды. Ее предел на - бесконечности =0, предел на + бесконечности = 1.
    # Так же, исходя из графика функции, она резко возрастает на участке (-5,5)
    # Предел при x->-30 справа = =>0.000000000000094 (15 нак после запятой)
    # Предел при x->+30 слева =  =>0.999999999999906 (15 нак после запятой)
    # Вполне уместо установить ограничение по аргументу функции чтобы избежать ресурсоемких вычислений, а именно
    # Если аргумент >30 -> значение = 0.999999999999999
    # Если аргумент <30 -> значение = 0.000000000000001
    if arg > 30:
        return 0.9999999995
    elif arg < (-30):
        return 0.0000000005
    else:
        return (1/ (1+exp(-arg)))  # f(x) = 1 / (1+exp(-x))    f'(x) = f(x)*(1-f(x))

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
    f.close()

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

def resetSigmaForObjects(object):       # На всякий случай обнуляем сигмы
    for i in range(object.__len__()):
        object[i].sigma = 0.00



def readDataForInputMlp():  # Рабочая функция для работы MLP system
    key = False
    inputMlpArray = []  # Массив объектов mlp
    arr = []    # промежуточный массив
    for i in range(6):                      # Собираем из 6 файлов данные для input_mlp
        fileName = "matrixWork" + str(i) + "1.txt"
        with open(fileName, 'r') as f:
            arr = f.readlines()  # чтение
            arr = np.asfarray(arr, float)  # преобразование во loat
        inputMlpArray.extend(arr)  # Собрали 6 по N массивов в одном
    inputNeurons = []

    for i in range(0,inputMlpArray.__len__()):     # заполняем массив объектов входного слоя
        inputNeurons.append(Neurons(inputMlpArray[i]))  # заполнили объект данными из matixWork
    for i in range(0,inputNeurons.__len__()):
        inputNeurons[i].value = activation(inputNeurons[i].value)   # Прогоняем сразу через функцию активации
    fileName = "weight_mlp0.txt"    # Работаем с первым набором весов между input_mlp & hidden1 layer
    with open(fileName,'r') as f:
        weightMlp0 = np.asfarray(f.readlines(),float)
    weightMlp0 = np.reshape(weightMlp0, (-1, 1176)) # Преобразовали в n x 1176 столбцов. Для организации связи каждый с каждым
    f.close()
    fileName = "weight_mlp1.txt"    # Работаем с первым набором весов между hidden1 & hidden 2 layers
    with open(fileName, 'r') as f:
        weightMlp1 = np.asfarray(f.readlines(), float)
    weightMlp1 = np.reshape(weightMlp1, (-1, 2000)) # Преобразовали в n x 2000 столбцов. Для организации связи каждый с каждым
    f.close()
    fileName = "weight_mlp2.txt"    # Работаем с первым набором весов между hidden2 and outputLayers(Связб 2000 - 1)
    with open(fileName, 'r') as f:
        weightMlp2 = np.asfarray(f.readlines(), float)
    #print("weight_mlp2_shape_is:", weightMlp2.shape, type(weightMlp2[10]))
    f.close()

    hidden1,hidden2 = [],[] # объявили объекты скрытых слоев 1 и 2
    for i in range(weightMlp0.__len__()): hidden1.append(Neurons(0.0))    # создали объекты 1 скрытого слоя
    #print("hidden1_len_after_create_is:",hidden1.__len__(),type(hidden1[10].value))
    for i in range((weightMlp1.size//weightMlp1.__len__())): hidden2.append(Neurons(0.0))    # создали объекты 2 скрытого слоя
    #print("hidden2_len_after_create_is:", hidden2.__len__(), type(hidden2[10].value))
    x = open("__test.txt",'w')
    for i in range(inputNeurons.__len__()):
        for j in range(weightMlp0.__len__()):
            hidden1[j].value += weightMlp0[i][j]*inputNeurons[i].value    # заполнили 1 скрытый слой значениями
            x.write("weight0[%i]" % i)
            x.write("[%i]" % j)
            x.write("= %f"%weightMlp0[i][j])
            x.write(" inputNeurons[%i]" % i)
            x.write("= %f\n" % inputNeurons[i].value)
    x.write("/n/n")
    for i in range(hidden1.__len__()):
        x.write("hidden[%i]"%i)
        x.write(".value = %f\n" %hidden1[i].value)
        hidden1[i].value = activation(hidden1[i].value)  # активация нейронов
    x.close()
    for i in range(hidden1.__len__()):
        for j in range(hidden2.__len__()):
            hidden2[j].value+= weightMlp1[i][j] * hidden1[i].value  # заполнили 2 скрытый слой значениями
    for i in range(0,hidden2.__len__()): hidden2[i].value = activation(hidden2[i].value)    # активация нейронов
    outputNeuron = []
    outputNeuron.append(Neurons(0.0)) # создали объект выходного нейрона, заполнили нулем
    for i in range(0,hidden2.__len__()):
        outputNeuron[0].value += (weightMlp2[i] * hidden2[i].value)# заполнили и активировали сразу
    outputNeuron[0].value = activation(outputNeuron[0].value)

    dropObjectToFile(inputNeurons,"__inputMlp.txt")     # передача объектов в txt
    dropObjectToFile(hidden1, "__hidden1.txt")          # передача объектов в txt
    dropObjectToFile(hidden2, "__hidden2.txt")          # передача объектов в txt


    # функция контроля лицо/не лицо. Решение что делать дальше
    control = contollerOfError(outputNeuron[0].value, 2)
    outputNeuron[0].sigma = (1 - outputNeuron[0].value) if int(control[0]) == 1 else (-(1 - outputNeuron[0].value)) # было -(1 - outputNeuron[0].value)
    print(outputNeuron[0].value, outputNeuron[0].sigma)
    print("outputNeuron[0].value < 0.7" if int(control[0]) == 1 else "outputNeuron[0].value > 0.3")
    dropObjectToFile(outputNeuron, "__outputNeuron.txt")  # передача объектов в txt
    condition = (outputNeuron[0].value < 0.7) if int(control[0]) == 1 else (outputNeuron[0].value > 0.3)
    print(condition)
    if (condition):
        print(int(control[0]) == 1)
        print("condition +")
        backPropogation(weightMlp0, weightMlp1, weightMlp2) # выполняем backPropogation
    else:
        print("condition - ")

def backPropogation(weightMlp0 = [], weightMlp1 = [], weightMlp2 = []):
    print("function PB is began")
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
    for i in range(0,hidden2.__len__()):   # От выхода ко второму скрытому
        hidden2[i].sigma = weightMlp2[i]*outputNeuron[0].sigma  # переопределяем сигма для объектов

    # От второго скрытого к первому скрытому
    resetSigmaForObjects(hidden1)
    for i in range(0,hidden1.__len__()):   # От второго скрытого к первому скрытому
        for j in range(0,hidden2.__len__()):
            hidden1[i].sigma += weightMlp1[i][j] * outputNeuron[0].sigma    # переопределяем сигма для объектов
    # От первого скрытого к входным данным
    resetSigmaForObjects(inputNeurons)
    for i in range(0,inputNeurons.__len__()):
        for j in range(0,hidden1.__len__()):
            inputNeurons[i].sigma += weightMlp0[i][j]*outputNeuron[0].sigma # переопределяем сигма для объектов
    #Переопределяем веса в массивах. Для этого идем од входного к выходному
    file = open("weight_mlp0.txt",'w')
    #от входного до первого скрытого определяем набор весов
    for i in range(inputNeurons.__len__()):
        for j in range(hidden1.__len__()):
            weightMlp0[i][j] +=  step*hidden1[j].sigma*derivative(activation(hidden1[j].value))*hidden1[j].value
            file.write("%0.15f\n"%weightMlp0[i][j])

    file.close()
    file = open("weight_mlp1.txt", 'w')
    for i in range(hidden1.__len__()):
        for j in range(hidden2.__len__()):
            weightMlp1[i][j]+= step * hidden2[j].sigma * derivative(activation(hidden2[j].value))*hidden2[j].value
            file.write("%0.15f\n" % weightMlp1[i][j])
    file.close()
    file = open("weight_mlp2.txt", 'w')
    for i in range(len(weightMlp2)):
        weightMlp2[i]+=step*outputNeuron[0].sigma * derivative(activation(outputNeuron[0].value))*outputNeuron[0].value
        file.write("%0.15f\n"%weightMlp2[i])
    file.close()
    dropObjectToFile(inputNeurons,"__inputMlp.txt")
    dropObjectToFile(hidden1, "__hidden1.txt")
    dropObjectToFile(hidden2, "__hidden2.txt")