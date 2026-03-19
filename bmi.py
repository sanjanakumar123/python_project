# 1) Ask the user to enter their height in centimeters and store it in `height`.

# 2) Ask the user to enter their weight in kilograms and store it in `weight`.

# 3) Calculate BMI using the formula:
#    BMI = weight ÷ (height in meters)²
#    (Convert height from cm to meters by dividing by 100.)
#    Store the result in `BMI`.

# 4) Print the BMI value.

# 5) Use if–elif–else to decide the BMI category:
#    - If BMI is 18.4 or less → print "underweight"
#    - Else if BMI is 24.9 or less → print "healthy"
#    - Else if BMI is 29.9 or less → print "over weight"
#    - Else if BMI is 34.9 or less → print "severely over weight"
#    - Else if BMI is 39.9 or less → print "obese"
#    - Else → print "severely obese"


a = int(input("height: "))
b = int(input("weight: "))
c = b / (a)**2
print(c)
if (c <= 18.4) :
    print("underweight")
elif (c <= 24.9) :
    print("healthy")
elif (c <= 29.9) :
    print("over weight")
elif (c <= 34.9) :
    print("severly overweight")
else : 
    print("severly obese")
