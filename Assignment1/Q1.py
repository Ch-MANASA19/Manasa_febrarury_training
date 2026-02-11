name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
income = float(input("Enter family income: "))
is_rural = input("Is the student from a rural area? (True/False): ")
is_rural = True 
if is_rural == "True" :
    True
else :
    False
eligible = (percentage > 85 and income < 300000) or (percentage > 90)
print("\n--- Student Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}")
print(f"Family Income: {income}")
print(f"Rural Area: {is_rural}")
if eligible:
    print("\nEligible for scholarship")
else:
    print("\nNot eligible")
