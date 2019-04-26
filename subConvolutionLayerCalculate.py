import numpy as np
from main import Point


def getSize():  #Возвращает значимые параметры bmp из файла с его размерами.
    with open("size.txt",'r') as f:
        arr = np.asfarray(f.readlines(),float)
    f.close()
    listOfObjects = Point()
    listOfObjects.i = arr[0]
    listOfObjects.j = arr[1]
    return listOfObjects



def test(i1,i2):
    size = getSize()
    fileName = "exitConvolution"+str(i1)+str(i2)+".txt"
    with open(fileName, 'r') as f:  #Заполняем массив из файла
        arr = f.readlines()
        arr = np.asfarray(arr, float) # Преобразовываем во float
    arr = list(arr) # преобразуем в список
    #del arr[int(size.i*(len(arr)//size.i)):]   # удаляем лишние элементы, чтобы сделать номальную прямоугольную матрицу и не добавлть лишнего
    f.close()


    global sizeArray
    sizeArray = int(len(arr)**(1/2))  # Размер массива сохраняем в переменную. Так как массив по определению у нас
    # должен быть квадратны то мы извлекаем квадратны корень из длины всего массива
    del arr[int(sizeArray*len(arr)//sizeArray):] #обрехаем под прямоуголькую матрицу. Лучше удалить крайние элементы, чем наращивать непонятно чем.
    global matrixWork
    matrixWork = np.reshape(arr,(-1,sizeArray)) #Преобразовали одномерный в двумерный массив размерностью sizeArray

def reLu(i1,i2):
    steps = int(sizeArray**2 / 16)  # это справедливо для квадратной матрицы
    #steps = (sizeArray//4+1) *  ((len(matrixWork)//sizeArray)+1)        # колисество секторов округляем в большую сторону, т.к. не все 4х4
    maximum =[]
    ai,aj,k,i,j=0,0,0,0,0
    numberString = 0
    numberColumn = 0

    key = True
    key0 = False
    key1 = False
    key2 = False

    while (k< steps):   # пока не набрали достаточное количество карт
        if (key == True):       # если запись разрешена. Для каждой новой первой карты 4х4 первый элемент записываем как максимальный
            maximum.append(matrixWork[i][j]) #Для каждой новой первой карты 4х4 первый элемент записываем как максимальный
            key = False # и сразу же блокируем ключ. Поднимаем когда всю карту 4х4 просмотрели.
        maximum[k] = max(matrixWork[i][j],maximum[k]) #Вернет максимум в переменнуюS

        if (((j+1)%4) == 0) or ((j+1) == sizeArray):  # Если дошли до конца строки в карте 4х4 или жо правой границы по горизонтали
            j=aj            #обнулить j
            numberString +=1   #посчитали номер строки в карте 4х4
            key0 = True #чтобы не проскочить элемент при проходе
            i+=1

        if (numberString == 4) and (((numberColumn+1) ==4) or ((j+1) == sizeArray)):  #//если находимся в ячейке 4-4, то есть прошли карту 4х4 до конца
            numberColumn=0  #сбрасываем счетчик столбцов
            numberString=0  #сбрасываем счетчик строк
            k+=1            #начали исследовать следующую карту
            aj+=4           #повысили индекс aj для дальнейшей работы
            key = True      #разрешили запись первого элемента для сравнения в массив максимальных
            i = ai          #сместили i на первую строчку карты 4х4
            j = aj          #сместили j на первый элемент первой строчки карты 4х4
            key1 = True     # реагирует на сброс

        # Когда достигли последнего элемента в проходе по "первой строке" шириной 4i массива.
        # То есть для первой строчки это будет array[3][array.length]


        if (j == sizeArray):
            ai+=4  #повысили индекс ai для дальнейшей работы
            i=ai    #Передвигаем i на следующую строку (вместо 0 стала 4)
            aj=0    #установили индекс aj в 0, так как строка начинается
            j=aj
            key1 = True

        if (key0 == True):
            key0 = False
            numberColumn =0
        else:
            j+=1
            numberColumn+=1







def maxPooling(index1, index2):
    size = 4
    maximum = np.zeros((matrixWork.size)//(size**2))       #Создали массив квадратной матрицы размером m*n, заполненны нулями
    maximum = np.asfarray(maximum,float)    # на всякий сучай преобразуем во float
    # индекс массива определяем как: количество строк по 4 матрицы * i // 4 + j // 4
    quantityOfString = (len(matrixWork)// size)
    for i in range(len(matrixWork)):
        for j in range(len(matrixWork)):
            if ((j+1)%size == 0) and ((i+1)%size == 0):
                maximum[quantityOfString*(i//size)+(j//size)] = matrixWork[i][j]


    for i in range(len(matrixWork)):
        for j in range(len(matrixWork)):
            maximum[quantityOfString*(i//size) + j//size] = max(matrixWork[i][j],maximum[quantityOfString*(i//size) + (j//size)])
    fileName = "matrixWork"+str(index1)+str(index2)+".txt"
    with open(fileName, 'w') as f:
        f.writelines("%f\n" % z for z in maximum)
    f.close()



def complete(index1, index2):
    test(index1, index2)
    maxPooling(index1,index2)

