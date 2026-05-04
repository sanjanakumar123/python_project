n = int(input("Enter a number whoose sum you want to find: "))
sum=0
for i in range(1,4):
    sum = sum+i
    print("\nsum =" , sum)

string = input("Please enter your own string: ")
string2 = ('')
for i in string:
    string2 = i + string2
print("\nThe orginal string = " , string)
print("The reversed string = " , string2)

n = int(input("Enter the value of n: "))
print (f"numbers from {n} to {1} are: ")
for i in range(n,0,-1):
    print (i)
