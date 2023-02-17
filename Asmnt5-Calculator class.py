 #Implement a Calculator Class

class Calculator:

    def __int__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        print(self.num1 / self.num2)

Calculator = Calculator(10,94)
Calculator.add()
Calculator.subtract()
Calculator.multiply()
Calculator.divide()
