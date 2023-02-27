print("Welcome to the tip calculator! by Lunita\n")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
percertage = tip / 100 + 1
people = int(input("How many people to split the bill? "))
price = round((bill / people) * percertage , 2)
print(f"Each person should pay then ${price} with the tip included!")