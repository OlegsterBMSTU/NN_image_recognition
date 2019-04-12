import convolutionCalculate
import subConvolutionLayerCalculate as sclc
from correctionCore import correctionCore

class Image:
    def __init__(self, index1, index2):
        self.number1 = index1     #инициализация с определеным номером
        self.number2 = index2
    def convCalculate(self):
        convolutionCalculate.convolution(self.number1, self.number2)       #вызываем функцию для формирования exitConvolution
    def subCalculate(self):                                 #вызываем функцию для формирования subConvolution
        sclc.complete(self.number1, self.number2)
    def correction(self):
        correctionCore(self.number1,self.number2)


class Neurons():
    def __init__(self,v):
        self.sigma =0.0
        self.value = v