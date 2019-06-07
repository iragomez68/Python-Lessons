#Create variables
name = "Iraldo"
country = "Canada" 
age = 51
hourly_wage = 15
daily_wage = hourly_wage * 8
satisfied = True

print("********Using concatenation************")
print("Employee name: " + name)
print("Country: " + country)
print("Age: " + str(age))
print("Hourly wage: " + str(hourly_wage))

#An f-string accels all data types
print("")
print("**********Using f_string**************")
print(f"Daily wage : ${daily_wage} \nWeekly wage: ${daily_wage * 5}")
print(f"Employee satisfaction: {satisfied}")

s1 = "hello python world , i'm a beginner "
s2 = "world"
print(s1[0:s1.find(" ")])

#for i in range(len(s1)-1):
 #   print(str(s1.index(i))