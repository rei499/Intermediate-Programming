# Learning Assessment #1
# Write a Python script that takes a numerical input representing years.
print("Year to Seconds Converter \n")
year = int(input("Type the number of year: "))

# Assume 1 year = 365 years
# Convert the years to seconds

output = ((((year * 365)* 24)* 60)* 60)

# Display the result

print(f"There are {output} seconds in {year} year/s.")
