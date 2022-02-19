# 07. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on


def print_month_name(x):
     if (x==1):
         print ("January")
         print("daysinMonth = 31")

     if (x==2):
         print ("February")
         year = int(input("Enter the present year: "))
         if year % 4 == 0:
             print ("Leap year. daysinMonth = 29")
         else:
             print("Not leap year. daysinMonth = 28")
             
     if (x==3):
         print("March")
         print("daysinMonth = 31")
     if (x==4):
         print("April")
         print("daysinMonth = 30")
     if (x==5):
         print("May")
         print("daysinMonth = 31")
     if (x==6):
         print("June")
         print("daysinMonth = 30")
     if (x==7):
         print("July")
         print("daysinMonth = 31")
     if (x==8):
         print("August")
         print("daysinMonth = 31")
     if(x==9):
         print("September")
         print("daysinMonth = 30")
     if(x==10):
         print("October")
         print("daysinMonth = 31")
     if(x==11):
         print("November")
         print("daysinMonth = 30")
     if(x==12):
         print("December")
         print("daysinMonth = 31")
     if(x<1 or x>12):
         print("Invalid input")
month = int(input("Enter the month number: "))
print_month_name(month)