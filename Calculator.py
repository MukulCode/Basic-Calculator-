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

def pow(num1, num2):
    print(num1**num2)


while True:

    # printing a formatted menu for the calculator
    print("\t\t WELCOME TO MUKUL'S BASIC CALCULATOR")
    print('\tMENU')
    print('\t1:ADDITION OF TWO NUMBERS')
    print('\t2:SUBTRACTION OF TWO NUMBERS')
    print('\t3:DIVISION OF TWO NUMBERS')
    print('\t4:MULTIPLICATION OF TWO NUMBERS')
    print('\t5:POWER OF A NUMBER (FIRST^SECOND)')


    # take input from the user
    choice = input('ENTER CHOICES BETWEEN 1 AND 5')
    # take two numbers from the user to operate upon them
    print('ENTER TWO NUMBERS')
    num1 = int(input('ENTER FIRST NUMBER'))
    num2 = int(input('ENTER SECOND NUMBER'))

    # if choice is one then the add function will be called
    if choice == '1':
        add(num1, num2)

    # if choice is two then the sub function will be called

    elif choice == '2':
        sub(num1, num2)

    # if choice is one then the div function will be called
    elif choice == '3':
        div(num1, num2)

    # if choice is one then the mul function will be called
    elif choice == '4':
        mul(num1, num2)

    elif choice == '5':
        num1**num2

    # if choice does not lies between 1 and 5 then there is an error message
    else:
        print('!!!!!!!WRONG INPUT!!!!!!!')
    print('want to calculate more?')
    dec = input('yes or no ')
    if dec.lower() == 'yes':
        continue
    else:
        break
