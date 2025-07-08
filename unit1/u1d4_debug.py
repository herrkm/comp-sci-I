# Date 

# To quickly comment and uncomment blocks of code, select the code
# you want to comment/uncomment and press CTRL + /. 
# This helps to keep code from running when you don't want it to.
# The "Price of Trip" section below has code commented out; you will
# need to uncomment it before attempting to debug.


# This code should:
  # take user input for today's day, date, month, and year
  # print the result out in two formats:
  # American format: Monday, August 1, 2022
  # European format: Monday 1 August 2022

  # Check for compile-time errors and runtime errors first,
  # but there may be logic errors as well.

# fails to assign results of input to a variable causing compile-time errors below
# input("Please enter the day of the week.\n")
# input("Please enter today's numeric date.\n")
# input("Please enter the current month.\n")
# input("Please enter the current four-digit year.\n")

day = input("Please enter the day of the week.\n")
date = input("Please enter today's numeric date.\n")
month = input("Please enter the current month.\n")
year = input("Please enter the current four-digit year.\n")

# logic errors from missing spaces
date_amer = day + ", " + month + " " + date + ", " + year
date_euro = day + " " + date + " " + month + " " + year

print("American format of today's date:")
print(date_amer)

# logic error from use of date_amer instead of date_euro
print("European format of today's date:")
print(date_euro)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Price of Trip

# This code should:
  # Take user input for number of miles, cost of gas, and car's mpg
  # Calculate the cost of the trip
  # Display the cost, including a dollar sign

distance = input("Please enter the length of your trip in miles.\n")
gas_price = input("Please enter the current price of gas.\n")
mpg = input("Please enter your car's fuel efficiency in miles per gallon.\n")

# can't calculate with strings - convert to float
gallons = float(distance) / float(mpg)
price = gallons * float(gas_price)

# can't add float to strings - convert to string
print("The trip will cost $" + str(price))



# Extra challenge, if time allows!
  # Google search "format float to 2 decimal places in python"
  # and read one or two results.
  # See if you can modify the working code above to display 
  # the price to the correct level of precision.
