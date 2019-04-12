import random
def initCoreWeight():
    print("initCoreWeight function is began")
    #name = "Core" + str(1)+str(0)+".txt"
    # Инициализируем начальные веса кар 5х5
    for i in range(6):
        for j in range(2):
            name = "Core" + str(i)+str(j)+".txt"
            with open(name,'w') as myFile:
                for z in range(25):
                    myFile.write("%f\n" % random.triangular(-1,1))
            myFile.close()
    print("initCoreWeight function is completed")
    # Инициализируем веса в mlp слое

def initMlpWeight():
    print("initMlpWeight function is began")
    with open("weight_mlp0.txt",'w') as myFile:
        for i in range(196*6):  #196 выходных данных от imput_mlp до 1 hidden layer
            myFile.write("%f\n" % random.triangular(-1,1))
        print(myFile.name, "is completed")
        myFile.close()

    with open("weight_mlp1.txt",'w') as myFile:
        for i in range(196*6*2000): # between first and second hidden layers
            myFile.write("%f\n" % random.triangular(-1,1))
        print(myFile.name, "is completed")
        myFile.close()
    with open("weight_mlp2.txt",'w') as myFile:
        for i in range(2000):   #from last hidden layer to outpu neuron
            myFile.write("%f\n" % random.triangular(-1,1))
        print(myFile.name, "is completed")
        myFile.close()
    print("initMlpWeight function is completed\n")

def initConversationWeight():
    print("initConversationWeight function is began")
    for i in range(3):
        name = "weight_conv"+str(i)+".txt"
        with open(name,'w') as myFile:
            for i in range(24):  #
                myFile.write("%f\n" % random.triangular(-1, 1))
        print(myFile.name, "is completed")
        myFile.close()
    print("initConversationWeight function is completed")




