Question 1)

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))
soma = A + B
if C > soma :
    print ("C is bigger than A + B")
elif C < soma :
    print ("C is less than A + B")
else :
    print ("C equals A+B")

-------------------------------------------------------------------------------------------------

Question 2)

A = int(input("Enter a Number: "))
test = A / 2
result = test % 1
if result == 0.0 :
    print("Even Number")
else :
    print("Odd Number")
--------------------------------------------------------------------------------------------------

Question 3)

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
if A == B :
    C = A + B
    print ("Result: ", C)
else :
    C = A * B
    print ("Result: ", C)

-------------------------------------------------------------------------------------------------
Question 4)

A = int(input("Enter a Number: "))
double = A * 2
triple = A * 3
if A <= -1 :
    print ("The number is negative, result: ", triple)
else :
    print ("The number is positive, result: ", double)

-----------------------------------------------------------------------------------------------------

Question 5)

num = int(input("Enter a number: "))
test = num / 2
end = test % 1 
if end == 0.0 :
    result = num + 5
    print ("The number is even, we add 5, result: ", result)
else :
    result2 = num + 8
    print ("The number is odd, we add 8, result: ", result2)

-----------------------------------------------------------------------------------------------------

Question 6)

A = int(input("Enter a number: "))
B = int(input("Enter another different number: "))
C = int(input("Enter another different number: "))
if A > B and A > C and B > C :
    print ("the order is: ", A, B, C)
elif A > B and A > C and C > B :
    print ("the order is: ", A, C, B)
elif C > A and C > B and B > A :
    print ("the order is: ", C, B, A)
elif C > A and C > B and A > B :
    print ("the order is: ", C, A, B)
elif B > A and B > C and A > C :
    print ("the order is: ", B, A, C)
elif B > A and B > C and C > A :
    print ("the order is: ", B, C, A)

------------------------------------------------------------------------------------------------------------

Question 7)

h = float(input("Enter your height:"))
g = (input("Enter your gender (Man or Woman): ")).lower()
if g == "man" :
    kg = (72.7 * h) - 58 
    print("Your ideal weight is: ", kg)
elif g == "woman" :
    kg = (62.1 * h) - 44.7
    print("Your ideal weight is: ", kg)
else :
    print ("Error, Genre not identified")

--------------------------------------------------------------------------------------------------------------

Question 8)

h = float(input("Enter your height: "))
kg = float(input("Enter your weight: "))
imc = kg / (h)**2
if imc < 18.5 :
    print ("You are underweight")
elif imc >= 18.5 and imc <= 25 :
    print ("You are at normal weight")
elif imc >= 25 and imc <= 30 :
    print ("Are you overweight")
else:
    print ("You are obese")

---------------------------------------------------------------------------------------------------------------

Question 9)

preco = int(input("Enter product price: "))
modo = (input("Payment methods:\n 1. Money\n 2. Check\n 3. Credit Card\n 4. Installments in 2x\n 5. Installments in 2x with interest \n Escolha uma opção de 1 a 5 : ")).lower()
op1and2 = preco * 0.9
op3 = preco * 0.85
op4 = preco
op5 = preco * 1.10
portion = op5 / 2
if modo == "1" or modo == "2" :
    print ("At sight, receive a 10% discount, final price: ", op1and2)
elif modo == "3" :
    print ("On credit card, 15% discount is received, final price: ", op3)
elif modo == "4" :
    print ("Interest-free installments, final price: ", op4)
elif modo == "5" :
    print ("In two installments we put an interest rate of 10%, final price: ", op5 )
    print ("Leaving two installments of: ", portion)
else :
    print("Invalid payment method")

------------------------------------------------------------------------------------------------------------------------------

Question 10)

idstudent = input ("Enter your verification code: ")
note1 = float (input("Enter your first note: "))
note2 = float (input("Enter your second note: "))
note3 = float (input("Enter your third note: "))
gpm = (note1 + note2 + note3) / 3
gpa = (note1 + note2 * 2 + note3 * 3 + gpm)/7
if(gpa >= 9.0) :
    finalgrade ="A"
elif (ma >= 7.5 and ma <9.0) :
    finalgrade = "B"
elif (ma >= 6.0 and ma <7.5) :
    finalgrade = "C"
elif (ma >= 4.0 and ma <6.0) :
    finalgrade = "D"
elif(ma < 7.0) :
    finalgrade = "E"
print( "Student ID: ", idstudent)
print("Notes", note1,note2,note3)
print("Average of the exercises :", gpm)
print("Exploitation",gpa)
print("Final grade:", finalgrade)
if ( finalgrade == "A" or finalgrade == "B" or finalgrade== "C" ):
     print("Student: Passed")
else :
    print ("Student: Failed")


