print("            Hello there, Im Mustafa Mandor i hope you are enjoying my repository.")
print("May i ask you about which of the following do you want to know about me:")
print("1- My Bio")
print("2- My Education")
print("3- My Skills")
print("4- My Personal Projects")
print("5- My Interests")
print("6- My Email Address")
print("0- End Program")
x= input("Choose the number: ")
x= int(x)
while x>0:
    if x==3:
        print("My Skils are; Quick Learner, Communication, Teamwork, Research and self learning.")
    elif x==2:
        print("My Education is; Bachelor of Science in Mechanical Engineering (Department of Mechatronics), Higher Technological Institute, Tenth of Ramadan Branch. 09/2017 - 07/2022, Very Good -GPA of 3.24- and currently learning machine learning and AI at AMIT Learning.")
    elif x==5:
        print("My Interests are: learning more about CS and Engineering technologies.")
    elif x==1:
        print("Mechatronics engineer who is passionate to increase his knowledge and very motivated to learn more. -Willing to success-")
    elif x==4:
        print("My Personal Projects are: Floating Waste Collecting Robot. and Electric Racing Car Chassis.")
    elif x==6:
        print("My Email Address is: mustafa.mandor@yahoo.com")
    x= input("Choose the number: ")
    x= int(x)
