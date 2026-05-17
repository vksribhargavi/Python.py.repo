#1. Check whether employee age is above 21 and salary is above 30000
'''age=int(input())
salary=int(input())
if age>21 and salary>30000:
    print ("Valid")
else:
    print("Invalid")'''


#2. Check whether student passed in two subjects
'''stu1marks=int(input())
stu2marks=int(input())
if stu1marks>=35 and stu2marks>=35:
    print ("Pass")
else:
    print("Fail")'''

#3. Check whether entered value is between two ranges
'''num=int(input())
min=15
max=20
if num>min and num<max:
    print('In the range')
else:
    print('Not in range')'''

#4. Check whether username and password are correct
'''username=str(input())
password=str(input())
if username=="sribhargavi" and password=="kaathyusha":
    print("correct")
else:
    print("incorrect")
'''
#5. Check whether temperature is within safe range
'''temp=int(input())
upper_limit=38
lower_limit=12
if temp>lower_limit and temp<upper_limit:
    print("safe")
else:
    print("not safe")'''

#6. Check whether both entered numbers are even
'''num1=int(input())
num2=int(input())
if num1 %2==0 and num2%2==0:
     print("Both are even")
else:
     print("not even")'''

#7. Check whether both entered numbers are positive
'''num1=int(input())
num2=int(input())
if num1>=0 and num2>=0:
     print("positive")
else:
     print("not positive")'''

#8. Check whether person is eligible for driving
'''age=int(input())
lisence_num=str(input())
if age>=18 and lisence_num=="valid":
     print("Eligible")
else:
     print("Not eligible")'''

#9. Check whether project progress meets deadline condition
'''days=int(input())
percentage=int(input())
if days>=4 and percentage>=95:
     print("project progress meets deadline condition")
else:
     print("project progress does not meets deadline condition")'''

#10. Check whether attendance and marks satisfy eligibility
'''ttendance=int(input())
marks=int(input())
if attendance>=75 and marks>=36:
     print("Eligible")
else:
     print("not eligible")'''

#11. Check whether entered role is Admin or Manager
'''role = input()
if role == "Admin" or role == "Manager":
    print("Access Granted")
else:
    print("Access Denied")'''

#12. Check whether student scored distinction in any one subject
'''marks1=int(input())
marks2=int(input())
distinction = 75
if marks1>distinction or marks2>distinction:
     print("True")
else:
     print("False")'''

#13. Check whether entered day is weekend
'''days=str(input())
if days=="saturday" or days == "sunday":
    print("weekend")
else:
    print("not weekend")'''

#14. Check whether selected category matches two possible values
'''category=str(input())
if category=="Accesesories" or category=="clothing":
    print("found")
else:
    print("not found")'''

#15. Check whether salary or experience satisfies requirement
'''salary=int(input())
experience=int(input())
if salary>=45000 or experience>=5:
    print("Satisfied")
else:
    print("not satisfied")'''

#16. Check whether temperature is extremely low or high
'''temp=int(input())
lower_limit=20
higher_limit=42
if temp<lower_limit or temp<higher_limit:
     print("lower")
else:
     print("higher")
'''

#17)Check whether entered username matches predefined values
'''username = input("Enter username: ")
if username == "sri" or username == "bhargavi":
    print("Valid Username")
else:
    print("Invalid Username")'''

#18.Check whether selected option belongs to given choices
'''choice = input("Enter username: ")
if choice == "sri" or choice == "bhargavi":
    print("belongs")
else:
    print("not belongs")'''

#19. Check whether entered city matches allowed cities
'''city=input("enter city:")
if city=="Vijaynagaram" or city=="Srikakulam" or city=="tarnaka":
     print("allowed")
else:
     print("not allowed")'''

#20. Check whether entered number matches predefined values
'''num=int(input())
if num==10 or num==20:
    print("Matched")
else:
    print("not matched")'''

#21. Check whether user is not admin
'''admin=str(input())
if not admin=="manager":
     print("Admin")
else:
     print("not admin")'''

#22. Check whether entered number is not positive
'''num=int(input())
if not num>0:
    print("True")
else:
    print("False")'''

#23. Check whether entered value is not empty
'''value=int(input())
print(not value=="")'''

#24. Check whether file is not available
'''fileAvailable=input()
print(not fileAvailable)'''

#25. Check whether employee is not active
'''employee = input("Enter employee status: ")
if employee != "active":
    print("Employee is not active")
else:
    print("Employee is active")'''

#26. Check whether project status is not completed
'''project = input("Enter project status: ")
if project != "completed":
    print("Project is not completed")
else:
    print("Project completed")'''

#27. Check whether password is not correct
'''password = input("Enter password: ")
if password != "admin123":
    print("Password is not correct")
else:
    print("Correct password")'''

#28. Check whether temperature is not safe
'''temperature = int(input("Enter temperature: "))
if temperature != 25:
    print("Temperature is not safe")
else:
    print("Temperature is safe")'''

#29. Check whether selected option is not allowed
'''option = input("Enter option: ")
if option != "yes":
    print("Selected option is not allowed")
else:
    print("Option allowed")'''

#30. Check whether marks are not passing marks
'''marks = int(input("Enter marks: "))
if marks < 35:
    print("Marks are not passing marks")
else:
    print("Pass")'''