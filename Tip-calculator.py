#If the bill was $240.00, split between 6 persons, with 15% tip.
#Each person should pay (240.00/6) * 1.15 = 46.00
#Round the result to 2 decimal places = 46.00
print("Welcome to the tip calculator app!")
bill = float(input("what was the total bill? $"))
tip= int(input("How much tip would you linke to give? 10, 13 or 15?"))
persons = int(input("how many persons to split the bill?"))
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill /persons
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
