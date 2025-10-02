welcome_text = "Welcome to the tip calculator!"
bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))
output = (bill * (1+(tip*.01))) / split
rounded_output = round(output, 2)

print(f"Each person should pay {rounded_output}")

