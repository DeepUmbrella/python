# coding=utf8 

# this is single line comments

'''
this is Multi-line comments
'''

#===================  programming  start =====================
# please enter height and weight 

height = float(input("enter your height: "));
weight = float(input("enter your weight: "));

# calculate bmi

bmi = weight / (height * height);

print("your bmi is: " + str(bmi));



#Determine whether the figure is healthy or not

if bmi < 18.5:
	print("you are underweight")
if bmi >= 18.5 and bmi < 25:
	print("you are healthy")
if bmi >= 25 and bmi < 30:
	 print("you are overweight")
   
if bmi >= 30:
	print("you are obese")


#===================  programming  end =====================



