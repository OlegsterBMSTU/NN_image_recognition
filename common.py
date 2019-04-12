
import allInit
import readImage
#import convolutionCalculate
#import subConvolutionLayerCalculate as sclc
from dataclasses import dataclass
import MLP_system as mlps
import classSystem
import backPropogation
import sys
import os, glob

class Point:    #Будем передавать в функции для записи координат
    def __init__(self):
        self.i = 0
        self.j = 0
        self.value=0;
    #i: int
    #j: int
    #value: int

def Stop():
    print("Ya vse")
    #sys.exit()

key = False



if __name__ == '__main__':
    name = "Abba.bmp"
    """
    readImage.array(name)
    writeFile()
    print(len(bmpFile))
    
    """
    #allInit.initConversationWeight()
    #allInit.initCoreWeight()
    #allInit.initMlpWeight()

    print(os.getcwd())
    path = os.getcwd() + "\__image/"
    print(path)
    listOfFiles= [f for f in os.listdir(path) if f.endswith('.bmp')]
    print (listOfFiles)
    print(listOfFiles[0])
    print(len(listOfFiles))
    i=0
    for i in listOfFiles:
        name = "__image/"
        key = True
        name += i
        print(name)
        while (key == True):
            readImage.readImage(name)
            #Это все работает
            valueList = []      # Здесь будет список объектов
            for j in range(0,2):
                for i in range(0,6): # Создаем список объектов
                    value = classSystem.Image(i,j)    # передаем индекс для создания объекта с нужным индексом
                    valueList.append(value)         # создаем объект с нужным индексом


            for i in range(len(valueList)):
                print(i,valueList[i].number1,valueList[i].number2)
                valueList[i].convCalculate()
                valueList[i].subCalculate()
            print("1==")
            mlps.readDataForInputMlp()
            print("2==")

            for i in reversed(valueList):
                print(i.number1,i.number2)
                i.correction()
            var = mlps.getFileOfObjects("__outputNeuron.txt")
            if var[0].value > 0.7:
                key = False
            else:
                key = True

    # Надо продумать логику как индексы передавать в объекты чтобы правильно вызывать файлы.
    # Так же надо продумать как именно хватать первые файлы и как именно вторые


    #print(bmpFile[10])

    Stop()
