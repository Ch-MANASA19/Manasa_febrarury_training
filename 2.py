customer_name = input("Enter customer name: ")
price = float(input("Enter product price: "))
is_premium = input("Is the customer a premium member? (True/False): ")
coupon = input("Enter coupon code: ")
is_premium = True if is_premium == "True" else False
discount = 0
if price > 5000 and is_premium:
    discount = 0.20
elif coupon == "SAVE10" or is_premium:
    discount = 0.10
discount_amount = price * discount
final_price = price - discount_amount
print("\n--- Billing Details ---")
print(f"Customer Name: {customer_name}")
print(f"Original Price: {price}")
print(f"Discount Applied: {discount_amount}")
print(f"Final Price: {final_price}")
if is_premium:
    print("Premium benefits applied")
