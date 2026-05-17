#1. Check Employee promotion eligibility
'''age=int(input())
experience=int(input())
salary=int(input())
if age>25 and experience>5 and salary>50000:
    print("Eligible for promotion")
else:
    print("not eligible")'''

#2. Check student distinction category
'''maths_marks=int(input())
science_marks=int(input())
english_marks=int(input())
if maths_marks>75 and science_marks>75 and english_marks>75:
    print("Distinction")
elif maths_marks>35 and science_marks>35 and english_marks>35:
     print("pass")
else:
     print("Fail")'''

#3. Check website login system
'''username=str(input())
password=str(input())
otp=int(input())
if username=="sri" and password=="bhargavi" and otp==2345:
    print("Login")
else:
    print("invalid")'''

'''username = input()
password = input()
otp = int(input())
if username in ['Sri', 'bhargavi', 'swaroop'] and \
   password in ['deepika', 'jithya', 'swaroopasis'] and \
   otp in [2345, 4567, 8765]:
    print("Login")
else:
    print("invalid")'''

#4. Check internet package category
'''speed=int(input())
data_usage=int(input())
remaining_days=int(input())
if speed>100 and data_usage>500 and remaining_days>20:
    print("Premium plan")
elif speed>70 and data_usage>300 and remaining_days>10:
    print("Standard plan")
else:
    print("basic plan") '''

#5.check job eligibility
'''degree=str(input())
experience=int(input())
age=int(input())
if degree=="yes" and experience>=2 and age>21:
    print("Eligible for interview")
else:
    print ("not eligible")'''
#6. Check flight boarding eligibility
'''ticket=str(input())
passport=str(input())
luggage=int(input())
if ticket == "yes" and passport == "yes" and luggage < 30:
    print("Boarding Allowed")
else:
    print ("Boarding Denied")'''

#7. Check scholarship eligibility
'''marks=int(input())
attendance=int(input())
income=int(input())
if marks >= 85 and attendance >= 90 and income < 300000:
    print( "Scholarship Approved")
else:
    print("Scholarship Rejected")'''

#8. Check mobile unlock system
'''pin=int(input())
face=str(input())
fingerprint=str(input())
if pin == 12345678 and face == "yes" and fingerprint == "yes":
    print("Mobile Unlocked")
else:
    print("Access Denied")'''

#9. Check hotel booking eligibility
'''rooms=int(input())
days=int(input())
budget=int(input())
if rooms>=2 and days>=3 and budget>5000:
    print("luxury booking")
elif rooms==1 and days==1 and budget==3000:
    print("Standard booking")
else:
    print ("budget booking")'''

#10. Check exam topper category
'''sub1=int(input())
sub2=int(input())
sub3=int(input())
total=sub1+sub2+sub3
if total>=270:
     print("topper")
elif total>=200:
     print("Average")
else:
     print("Needs improvement")'''

#11. Check gym membership category
'''age=int(input())
weight=int(input())
height=float(input())
if age > 18 and weight > 50 and height > 5.5:
    print("Fitness Category A")
elif age > 15 and weight > 40 and height > 4.5:
    print("Fitness Category B")
else:
    print("Basic Category")'''

#12. Check traffic penalty system
'''helmet=str(input())
license=str(input())
speed=int(input())
if helmet=="yes" and license=="yes" and speed<80:
    print("No fine")
elif speed>=80:
    print("Fine")
else:
    print("complaint")'''

#13. Check movie ticket pricing
'''age=int(input())
day=str(input())
member=str(input())
if age < 18 and member=="yes" and day=="Sunday":
    print("50% Discount")
elif member=="yes":
    print("25% Discount")
else:
    print("no discount")'''

#14. Check weather alert system
'''temperature = int(input())
wind = int(input())
rain = input()
if temperature > 40 and wind > 50 and rain == "no":
     print("Heat Alert")
elif rain == "yes" and wind > 60:
     print("Storm Alert")
else:
     print("Normal Weather")'''

#15. Check online shopping offer
'''purchase=int(input())
coupon=str(input())
premium=str(input())
if purchase>10000 and coupon=="yes" and premium=="yes":
    print("Max discount")
elif purchase<=5000 and coupon=="no":
    print("med discount")
else:
    print("no discount")'''

#16. Check server room access
'''idcard = input()
fingerprint = input()
accesslevel = int(input())
if idcard == "yes" and fingerprint == "yes" and accesslevel > 5:
     print("Access Granted")
else:
     print("Access Restricted")'''

#17. Check sports team selection
'''speed = int(input("Speed Score : "))
fitness = int(input("Fitness Score : "))
discipline = int(input("Discipline Score : "))
if speed > 80 and fitness > 80 and discipline > 80:
     print("Selected")
elif speed > 60 and fitness > 60:
     print("Waiting List")
else:
     print("Rejected")'''

#18. Check laptop purchase recommendation
'''budget = int(input("budget : "))
ram = int(input("RAM: "))
storage = int(input("storage : "))
if budget > 100000 and ram >= 16 and storage >= 512:
     print("Gaming Laptop")
elif budget > 50000 and ram >= 8:
     print("Office Laptop")
else:
     print("Basic Laptop")'''

#19. Check bank loan approval
'''salary = int(input("salary: "))
creditscore = int(input("Score : "))
experience = int(input("Experience : "))
if salary > 50000 and creditscore > 750 and experience > 3:
     print("Loan Approved")
elif salary > 30000 and creditscore > 650:
     print("Loan Under Review")
else:
     print("Loan Rejected")
'''

#20. Check smart home security system
door = input("closed door: ")
camera = input("Active Camera: ")
alarm = input("Alarm Enabled : ")
if door == "yes" and camera == "yes" and alarm == "yes":
     print("Home Secure")
else:
     print("Security Warning")





