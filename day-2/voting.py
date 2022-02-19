# Q3. Write a program to check whether a person is eligible for voting or not. (accept age from user)

age = int(input("enter age: "))

if age >= 18:
    print(age, "Eligible for voting")

else:
    print(age, "Not-Eligible for voting.")