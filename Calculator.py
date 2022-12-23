#Simple Calculator in Python

#Function to Add Two Numbers
def addition (num1, num2):
  return num1 + num2

#Function to Subtract Two Numbers
def substraction (num1, num2):
  return num1 - num2

#Function to Multiply Two Numbers
def multiplication (num1, num2):
  return num1 * num2

#Function to Divide Two Numbers
def division (num1, num2):
  return num1 / num2

print("Please select operation -\n"\
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division \n")

#Take input from the Users

 
  
select = int(input("Select Operations from 1., 2., 3., 4. :"))
  
number_1 = int(input("Enter the First Number :"))
number_2 = int(input("Enter the Second Number :"))

if select == 1:
  print(number_1, "+", number_2, "=", addition(number_1, number_2))

elif select == 2:
  print(number_1, "-", number_2, "=", substraction(number_1, number_2))

elif select == 3:
  print(number_1, "*", number_2, "=", multiplication(number_1, number_2))

elif select == 4:
  print(number_1, "/", number_2, "=", division(number_1, number_2))
    
else:
   print("Exiting The Program")
