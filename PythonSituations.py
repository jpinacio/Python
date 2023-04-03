(FOOTBALL TEAM)



age = int(input("Enter your age: "))

if age >= 5 and age <= 10 :

  print ("Category: Children")

elif age >= 11 and age <= 15 :

  print ("Category: Juvenile")

elif age >= 16 and age <= 20 :

  print ("Category: Junior")

elif age >= 21 and age <= 25 :

  print ("Category: Professional")

else :

  print("Invalid age, does not fit categories.")



---------------------------------------------------------------------------

(BRASIL PRODUCT ORIGINS)



cod = (input("Enter the product code, between 1 to 10: "))

if cod == "1" or cod == "2" :

  print ("Origin: SOUTH")

elif cod == "3" or cod == "4" :

  print ("Origin: SOUTHEAST")

elif cod == "5" or cod == "6" :

  print ("Origin: NORTH")

elif cod == "7" or cod == "8" :

  print ("Origin: NORTHEAST")

elif cod == "9" or cod == "10" :

  print ("Origin: MIDWEST")

else :

  print ("Invalid code")



-----------------------------------------------------------------------------

(VASCO X FLAMENGO)



gfla = int(input("Enter the number of Flamengo goals: "))

gvas = int(input("Enter the number of Vasco goals:"))

if gfla > gvas :

  print("Flamengo WIN")

elif gvas > gfla :

  print ("Vasco WIN")

else :

  print ("TIE")



--------------------------------------------------------------------------------------------------------------------
(PRODUCT CODE OPERATION)



num1 = int(input("Enter a number: "))

num2 = int(input("Enter another number: "))

cod = int(input("Enter the operation code from 1 to 4: \n 1. Average \n 2.Subtract larger from smaller \n 3. Multiply them \n 4. Division of the first by the second "))

if cod == 1 :

  average = (num1 + num2) / 2

  print("The average between the numbers: ", average)

elif cod == 2 :

  if num1 > num2 :

    dif = num1 - num2

  else:

    dif = num2 - num1

  print("Difference from largest to smallest: ", dif)

elif cod == 3 :

  prod = num1 * num2 

  print ("Product between numbers: ", prod)

elif cod == 4 :

  div = num1 / num2

  print ("Division of the first by the second: ", div)

else : 

  print ("Invalid code")



-------------------------------------------------------------------------------------------------------------------

(SALARY INCREASES)



salary = float(input("Enter your Salary: "))

if salary < 300:

  increase = salary * 1.45

  print("Your new salary is: ", increase)

elif salary >= 300 and salary <= 600 :

  increase2 = salary * 1.25

  print ("Your new salary is: ", increase2)

elif salary > 600 :

  increase3 = salary * 1.15

  print ("Your new salary is: ", inscrease3)

else :

  print ("ERROR, Salary Unchanged: ", salary)



----------------------------------------------------------------------------------------------------------------------------

(BIGGER AND SMALLER NUMBERS)



num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

cod = int(input("1 or 2. Inform the largest number \n 3 or 4. inform the smallest number \n Choose the operation code:"))

if cod == 1 or cod == 2 :

  if num1 > num2 :

    print ("The biggest number is: ", num1)

  elif num2 > num1 :

    print("The biggest number is: ", num2)

  else :

    print ("The numbers are the same")

elif cod == 3 or cod == 4 :

  if num1 < num2 :

    print ("The smallest number is: ", num1)

  elif num2 < num1 :

    print("The smallest number is: ", num2)

  else :

    print ("The numbers are the same")

else:

  print("Error, invalid code")
