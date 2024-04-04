"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""
while True:
  p = input("please input the initial investment: ")
  try:
    float(p)
  except:
    print("\nthat wasnt a number, try again") 
  else:
    break

while True:
  r = input("\nplease input annual interest rate as a percentage: ")
  try:
    float(r)
  except:
    print("\nthat wasnt a number, try again") 
  else:
    break

while True: 
  l = input("\nare you inputting time in years, months or days?: ")
  if l == "years":
    t = input("please input the lenth of time in years: ")
    y = "years"
    try:
      float(t)
    except:
      print("that wasnt a number, try again") 
    else:
      break
  elif l == "months":
    t = input("please input the lenth of time in months: ")
    y = "months"
    try:
      float(t)
    except:
      print("that wasnt a number, try again") 
    else:
      break
  elif l == "days":
    t = input("\nplease input the lenth of time in days: ")
    y = "days"
    try:
      float(t)
    except:
      print("\nthat wasnt a number, try again") 
    else:
      break
  else:
    print("please type only 'years', 'months', or 'days'")

p = float(p)
r = float(r)
t = float(t)

r2 = r / 100

answer = p * r2 * t
print(f"your interest will be {answer}")