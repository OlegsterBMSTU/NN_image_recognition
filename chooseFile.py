
def file_red(): return "1_r.txt"
def file_green(): return "1_g.txt"
def file_blue(): return "1_b.txt"
def weight_conv0(): return "weight_conv0.txt"
def weight_conv1(): return "weight_conv1.txt"
def weight_conv2(): return "weight_conv2.txt"

optionsOfColorFile = {
    0: file_red,
    1: file_red,
    2: file_green,
    3: file_green,
    4: file_blue,
    5: file_blue,
}

optionsOfWeightConversationFile = {
    0: weight_conv0,
    1: weight_conv0,
    2: weight_conv1,
    3: weight_conv1,
    4: weight_conv2,
    5: weight_conv2,

}

def createArrayOfWatrixWorkNames(arr):
    for i in range(6):
        arr.append("matrixWork"+str(i)+"0.txt")

def choiseOfMatrixWorks(index):
    arr = []
    createArrayOfWatrixWorkNames(arr)
    return arr[index]