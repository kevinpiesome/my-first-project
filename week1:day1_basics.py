#week 1 day 1 basics

# 1) basic types and printing
an_int = 7
a_float = 3.14
a_string = "hello, python!"
a_bool = True

print(an_int)
print(a_float)
print(a_string)
print(a_bool)

# 2) f-strings (formatted strings)
name = "Alex"
age = 25
print(f"{name} is {age} years old.")

# 3) Simple expressions
sum_result = an_int + int(a_float) # converts it to an int by casting it
print("Sum (an_int + int(a_float)):",sum_result)

# 4) interactive input: greeting
user_name = input("what is your name?")
print(f"Nice to meet you {user_name}!")

# 5) tiny calculator: add two numbers from input
x = input("enter first number: ")
y = input("enter second number: ")

# safely convert to float; handle empty or invalid input by defaulting to 0
try: 
    x_val = float(x)
except:
    x_val = 0.0
try:
    y_val = float(y)
except:
    y_val = 0.0

print(f"{x_val} + {y_val} = {x_val + y_val}")