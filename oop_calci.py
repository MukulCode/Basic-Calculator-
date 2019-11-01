#Start of BLL

class calci:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.res = 0

    def sum(self):
        self.res = self.a + self.b

    def sub(self):
        self.res = self.a - self.b

    def mult(self):
        self.res = self.a * self.b

    def div(self):
        self.res = self.a / self.b

#BLL ended

#Start of PL

ob1 = calci()

while(1):
    print("\n\tINDEX"
          "\n1.ADDITION"
          "\n2.SUBTRACTION"
          "\n3.MULTIPLICATION"
          "\n4.DIVISION"
          "\n5.EXIT")
    ch = input("Enter ur choice:")

    if (ch != '5'):
        ob1.a = int(input("Enter first no:"))
        ob1.b = int(input("Enter second no:"))

        if (ch == '1'):
            ob1.sum()
            print("Addition of given nos:", ob1.res)

        elif (ch == '2'):
            ob1.sub()
            print("Subtraction of given nos:", ob1.res)

        elif (ch == '3'):
            ob1.mult()
            print("Multiplication of given nos:", ob1.res)

        elif (ch == '4'):
            if (ob1.b != 0):
                ob1.div()
                print("Division of given nos:", ob1.res)
            else:
                print("Result not defined.")
        else:
            print("Please enter correct choice.")

    else:
        exit(0)

#PL ended