#TIP CALCULATOR

price = int(input("How much was the bill? "))
tip = int(input("How much tip 10, 15, 20? ")) / 100

no_of_ppl = int(input("How many ppl split the bill? "))

price_with_tip = price + (price * tip) 
total = price_with_tip / no_of_ppl

print(f"You each have to pay ${total}")

