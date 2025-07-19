income = float(input("Enter your monthly income in USD: "))

if income < 2000:
    print("You are in a low-income range.")
elif income < 5000:
    print("You are in a middle-income range.")
else:
    print("You are in a high-income range.")
