# |||||||||||||||||||||||||||||||||||||
# ||    ||\      //||     ||   //    ||
# ||    ||\\    // ||     ||  //     ||
# ||    || \\  //  ||     || //      ||
# ||    ||  \\//   ||     ||//       ||
# ||    ||   \/    ||     ||\\       ||
# ||    ||         ||     || \\      ||
# ||    ||         ||     ||  \\     ||
# ||    ||         ||     ||   \\    ||
# |||||||||||||||||||||||||||||||||||||

# function for the addition of two numbers
import math ;
def add(num1, num2):
    print(num1 + num2)

# function for the subtraction of two numbers
def sub(num1, num2):
    print(num1 - num2)


# function for the division of two numbers
def div(num1, num2):
    print(num1 / num2)


# function for the multiplication of two numbers
def mul(num1, num2):
    print(num1 * num2)


# function for power of a number
def pow(num1, num2):
    print(num1**num2)

# function for Sin of a number
def sin(num1):
    print(math.sin(num1))

# function for Cos of a number
def cos(num1):
    print(math.cos(num1))

# function for Tan of a number
def tan(num1):
    print(math.tan(num1))


while True:

    # printing a formatted menu for the calculator
    print("\t\t WELCOME TO MUKUL'S BASIC CALCULATOR")
    print('\tMENU')
    print('\t1:ADDITION OF TWO NUMBERS')
    print('\t2:SUBTRACTION OF TWO NUMBERS')
    print('\t3:DIVISION OF TWO NUMBERS')
    print('\t4:MULTIPLICATION OF TWO NUMBERS')
    print('\t5:POWER OF A NUMBER (FIRST^SECOND)')
    print('\t6:SIN OF A NUMBER')
    print('\t7:COS OF A NUMBER')
    print('\t8:TAN OF A NUMBER')

    # take input from the user
    choice = input('ENTER CHOICES BETWEEN 1 AND 8 ')
 
    # take one numbers from the user to operate upon them
    if choice == '6' or choice == '7' or choice == '8' :
        print('ENTER ONE NUMBER')
        num1 = float(input('ENTER A NUMBER '))
     # take two numbers from the user to operate upon them
    else:
        print('ENTER TWO NUMBERS')
        num1 = int(input('ENTER FIRST NUMBER '))
        num2 = int(input('ENTER SECOND NUMBER '))
      
    # if choice is one then the add function will be called
    if choice == '1':
        add(num1, num2)

    # if choice is two then the sub function will be called

    elif choice == '2':
        sub(num1, num2)

    # if choice is three then the div function will be called
    elif choice == '3':
        div(num1, num2)

    # if choice is four then the mul function will be called
    elif choice == '4':
        mul(num1, num2)

    # if choice is five the pow function will be called
    elif choice == '5':
        pow(num1, num2)
    # if choice is 6 the sin function will be called
    elif choice == '6':
        sin(num1)
    # if choice is 7 the cos function will be called
    elif choice == '7':
        cos(num1)
    # if choice is 8 the tan function will be called
    elif choice == '8':
        tan(num1)

    # if choice does not lies between 1 and 5 then there is an error message
    else:
        print('!!!!!!!WRONG INPUT!!!!!!!')
    print('want to calculate more?')
    dec = input('yes or no ')
    if dec.lower() == 'yes':
        continue
    else:
        break
