days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",
"Sunday")
completed = ("Yes","Yes","No","Yes","No","Yes","Yes")
habit = input("Enter your habit: ")
print("WEEKLY HABIT TRACKER")
print("Habit:", habit)
for day, result in zip(days, completed):
    print(day, "-", result)
#I used the len command to find the length of the tuple
print("Number of days:", len(days))
#I used the square brackets to give the place number
print("First day:", days[0])
print("First day's result:", completed[0])
print("Last day:", days[-1])
print("Last day's result:", completed[-1])
#I sliced data from weekends and weekdays separatly
print("Weekdays:", days[0:5])
print("Weekend:", days[5:7])
total = completed.count("Yes")
#I used the .count command to show how many habits were completed
print("Habit completed:", total, "days")