from Classes.MyComplex import Complex


class Calculator(object):

    def parseDoubleInput(self):
        a = Complex(*(input("Enter first Complex number: ").split()))
        print(a)
        b = Complex(*(input("Enter second Complex number: ").split()))
        print(b)
        return a, b

    def parseSingleInput(self):
        a = Complex(*(input("Enter Complex number: ").split()))
        return a

    def calculate(self):
        print("Add - 1")
        print("Sub - 2")
        print("Mul - 3")
        print("Div - 4")
        print("Abs - 5")
        option = input("Chose one operation: ")
        option = int(option)
        if option == 1:
            a, b = self.parseDoubleInput()
            print("Sum: {}".format(a + b))
        if option == 2:
            a, b = self.parseDoubleInput()
            print("Sub: {}".format(a - b))
        if option == 3:
            a, b = self.parseDoubleInput()
            print("Mul: {}".format(a * b))
        if option == 4:
            a, b = self.parseDoubleInput()
            print("Div: {}".format(a / b))
        if option == 5:
            a = self.parseSingleInput()
            print("Abs: {}".format(a.__abs__()))

if __name__ == '__main__':
    Calculator().calculate()