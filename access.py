##class Car:
##    def __init__(self,name,topSpeed):
##        self.__name=name
##        self.__topSpeed=topSpeed
##    def getName (self):
##        return self.__name
##    def setName(self,name):
##        self.__name=name
##            
##    def setTopSpeed(self,topSpeed):
##        self.__topSpeed=topSpeed
##
##    def getTopSpeed(self):
##        return self.__topSpeed
##
##    def getTopSpeedKPH(self):
##        kphSpeed= self.__topSpeed*3600/1000
##        return kphSpeed
##obj=Car("Jaguar",200)
##print(obj.getName())
##obj.setName("Ferrari")
##obj.setTopSpeed(300)
##print(obj.getTopSpeed())
##print(obj.getTopSpeedKPH())

class SimpleCalculator:
    def __init__(self,firstNumber,secondNumber):
        self.__firstNumber=firstNumber
        self.__secondNumber=secondNumber
    def getFirstNumber(self):
        return self.__firstNumber
    def getSecondNumber(self):
        return self.__secondNumber
    def setFirstNumber(self,firstNumber):
        self.__firstNumber=firstNumber
    def setSecondNumber(self,secondNumber):
        self.__secondNumber=secondNumber
    def getAdditionResult(self):
        add=self.__firstNumber + self.__secondNumber
        return add
    def getSubtractionResult(self):
        sub=self.__firstNumber - self.__secondNumber
        return sub
    def getMultiplicationResult(self):
        mul=self.__firstNumber*self.__secondNumber
        return mul
    def getDivisionResult(self):
        div=self.__firstNumber//self.__secondNumber
        return div
results=SimpleCalculator(30,20)
print(results.getFirstNumber())
results.setFirstNumber(20)
print(results.getSecondNumber())
results.setSecondNumber(20)
print(results.getAdditionResult())
print(results.getSubtractionResult())
print(results.getMultiplicationResult())
print(results.getDivisionResult())
        
