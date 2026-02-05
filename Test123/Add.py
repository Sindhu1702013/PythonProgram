# Author: OMKAR PATHAK
# This program prints the entered message

def justPrint(text):
    '''This function prints the text passed as argument to this function'''
    print(text)
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    increment_value = a + b
    print("The sum of the two numbers is:", increment_value)

if __name__ == '__main__':
    justPrint('Hello Sindhuja')


