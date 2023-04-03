(NOTES AVERAGE)

note1 = float (input("Enter one note: "))
note2 = float (input("Enter another note: "))
note3 = float (input("Enter another note: "))
average = (note1 + note2 + note3) / 3
if average >= 5 :
 print ("Approved")
else:
 print ("Disapproved")

----------------------------------------------------------------
(PASSWORD RELEASED, DENIED)


password = int(input("Enter your password:"))
if password == 123456 :
 print ("Access released")
else :
 print ("Acess denied")

------------------------------------------------------------------
(Letters Value Comparation)

A = int(input("Enter the value of A:"))
B = int(input("Enter the value of B:"))
C = int(input("Enter the value of C:"))
if (A + B) < C :
 print ("A + B is less then C")
else :
 print ("A + B is equal to or bigger than C")

-----------------------------------------------------------------
(SALARY INCREASE)

salary = float (input("Enter the salary:"))
if salary <= 300 :
 increase1 = salary * 1.35
 print("Your new salary is: ", increase1)
else :
 increase2 = salary * 1.15
 print("Your new salary is: ", increase2)
  
 ------------------------------------------------------------------
(BIGGER NUMBER)

A = int(input("Enter the value of A:"))
B = int(input("Enter the value of B:"))
C = int(input("Enter the value of C:"))
if A == B == C :
 print ("Equal numbers")
elif A > B and A > C :
 print ("A is bigger")
elif B > A and B > C :
 print("B is bigger")
else :
 print("C is bigger")
--------------------------------------------------------------------
(Brazil Localization States)

state = input("Enter the state(PB, PE, RJ, SP): ").lower()
if state == "pb" or state == "pe" :
 print ("Belongs to the Northeast")
elif state == "rj" or state == "sp" :
 print ("Belongs to the Southeast")
else :
 print ("North or Center")

-----------------------------------------------------------------------
