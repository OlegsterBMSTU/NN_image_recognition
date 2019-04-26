import convolutionCalculate
import subConvolutionLayerCalculate as sclc
#from correctionCore import correctionCore
from correctionCoreNew import correctionCore
from main import Point

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
        self.sigma =0.00
        self.value = v
    """
    def activation(self):
    if self.value > 30:
        return 0.999999
    elif self.value<-30:
        return 0.000001
    else:return (1/ (1+exp(-self)))  # f(x) = 1 / (1+exp(-x))    f'(x) = f(x)*(1-f(x))
    def derivative(self,func):
        return func*(1-func)
        """

