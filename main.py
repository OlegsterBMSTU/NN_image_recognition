
import allInit
import readImage
#import convolutionCalculate
#import subConvolutionLayerCalculate as sclc
from dataclasses import dataclass
import mlp as mlps
import classSystem
import backPropogation
import sys
import os, glob

class typeImages:   # Класс для массива картинок
    def __init__(self):
        self.type1 = ""
        self.type2= ""
    def getArrays(self):
        path = os.getcwd() + "\__image/faces/"
        self.type1 = [f for f in os.listdir(path) if f.endswith('.bmp')]
        path = os.getcwd() + "\__image/kitchen/"
        self.type2 = [f for f in os.listdir(path) if f.endswith('.bmp')]

class tImages:
    def __init__(self,name,path,face):
        self.name = name
        self.path = path
        self.face = face
        self.used = False

class Point:    #Будем передавать в функции для записи координат
    def __init__(self):
        self.i = 0
        self.j = 0
        self.value=0
    #i: int
    #j: int
    #value: int


def imageArray():
    setOfImages = []
    path = os.getcwd() + "\__image/faces/"
    for f in os.listdir(path):
        image= tImages(f,path,True)
        setOfImages.append(image)
    path = os.getcwd() + "\__image/kitchen/"
    for f in os.listdir(path):
        image = tImages(f, path, False)
        setOfImages.append(image)
    return setOfImages


def concotanationAndSordArray(func, path):
    path = os.getcwd() + "\__image/faces/"
    setOfImages = func

def howMuchFaces(list = []):       # для сортировки. Сколько объектом с признаком лицо
    counter =0
    for i in range(len(list)):
        if list[i].face == True: counter+=1
    return counter

def sortImagesArray(count, listOfObjects = []):
    for i in range(count):
        if (i%2!=0):
            middle = listOfObjects[i]
            listOfObjects[i] = listOfObjects[i+count+1]
            listOfObjects[i+count+1] = middle
    return  listOfObjects

def contollerOfError(obj,control):  #1 - write, 2 - read
    name = "__controlError.ini"
    f = (open(name,'w') if control==1 else open(name,'r'))
    if control == 1:
        if obj.face == True:
            f.write("1")
        else:
            f.write("0")
    else:
        result = f.readlines()
        f.close()
        return result



def Stop():
    print("Ya vse")
    #sys.exit()

key = False

def conditionForLearning(method,condition):   #write or read
    fileName = "conditionForLearning.ini"
    if condition == True: 0




if __name__ == '__main__':
    name = "Abba.bmp"

    #allInit.initConversationWeight()
    #allInit.initCoreWeight()
    #allInit.initMlpWeight()
    setOfImages = imageArray()  # создаем массив объектов
    #counter = howMuchFaces(setOfImages)
    setOfImages = sortImagesArray(howMuchFaces(setOfImages),setOfImages)  # сделали ортировку массива. Каждый второй это не лицо

    for i in range(setOfImages.__len__()):
        name = setOfImages[i].path + setOfImages[i].name
        key = True
        print(name)
        contollerOfError(setOfImages[i],1)
        readImage.readImage(name)
        while (key == True):
            #Это все работает
            valueList = []      # Здесь будет список объектов
            i,j = 0,0           # НА всякий случай сброс
            for j in range(0,2):
                for i in range(0,6): # Создаем список объектов
                    value = classSystem.Image(i,j)    # передаем индекс для создания объекта с нужным индексом
                    valueList.append(value)         # создаем объект с нужным индексом

            """
            for i in range(len(valueList)):
                valueList[i].convCalculate()
                valueList[i].subCalculate()
            mlps.readDataForInputMlp()
            for i in reversed(valueList):
                i.correction()
            control = contollerOfError(valueList[0].number2,2)
            outputNeuron = mlps.getFileOfObjects("__outputNeuron.txt")
            condition = (outputNeuron[0].value < 0.7) if int(control[0]) == 1 else (outputNeuron[0].value > 0.3)
            if (condition):
                key = True
            else:
                key = False
            """
            valueList[10].correction()
    # Надо продумать логику как индексы передавать в объекты чтобы правильно вызывать файлы.
    # Так же надо продумать как именно хватать первые файлы и как именно вторые


    Stop()
