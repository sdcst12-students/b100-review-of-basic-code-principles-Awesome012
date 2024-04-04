"""
### Assignment 4
#### Calculation of a debt repayment with recurring payments
This is the reverse of assignments 2 and 3

Calculate how long it will take to completely pay off a debt if regular payments are made.  Note that each year, the debt will increase by the amount of loan interest, but will decrease with youre recurring payment. 

Criteria:
Your program should ask the user for
* an initial debt
* the annual interest rate
* the annual payment
* the program will state how long it will take for the debt to be repaid.
* extra: Calculate the total amount of interest that is paid along with the debt repayment

Sample:
Joey takes a car loan to buy a new Tesla for $62000
The loan has an annual interest rate of .75% per month.  He makes monthly payments of $1000.
How many months will it take him to pay off the car.  How much interest has he paid in that time?

84 months
He will have paid 21711.60 in interest
"""

while True:
  d = input("please input the initial debt: ")
  try:
    float(d)
  except:
    print("\nthat wasnt a number, try again") 
  else:
    break

while True:
  r = input("please input the annual interest rate (as a percentage): ")
  try:
    float(r)
  except:
    print("\nthat wasnt a number, try again") 
  else:
    break

while True:
  p = input("please input the annual payment: ")
  try:
    float(p)
  except:
    print("\nthat wasnt a number, try again") 
  else:
    break

p = float(p)
r = float(r)
d = float(d)
r2 = r / 100
t = 0
check = 0
while True:
    t = t + 1
    interest = d * r2
    d = d + interest
    d = d - p
    check = check + interest
    d = round(d,2)
    if d <= 0:
        check = round(check,2)
        print(f"you have to pay an interest of {check}")
        print(f"it took {t} months to pay it")
        break