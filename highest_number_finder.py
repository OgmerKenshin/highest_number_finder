#Since I can only use if statements then I can't use def

num1 = float(input("please enter the 1st number: "))
num2 = float(input("please enter the 2nd number: "))
num3 = float(input("please enter the 3rd number: "))
num4 = float(input("please enter the 4th number: "))
num5 = float(input("please enter the 5th number: "))

#I'm gonna assume the 1st number is the highest (not that it matters)

highest_num = num1

#Insert if statements then rinse and repeat

if num2 > highest_num:
    highest_num = num2

if num3 > highest_num:
    highest_num = num3

if num4 > highest_num:
    highest_num = num4

if num5 > highest_num:
    highest_num = num5

#last function is to print the highest function found
print(f"The highest number is: {highest_num}")