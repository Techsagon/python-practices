print("########################################")
print("###                                  ###")
print("###    Welcome to Tip Calculator!    ###")
print("###                                  ###")
print("########################################\n")

bill_total = float(input("Please enter your bill total: $"))
tip_percentage = str(input("Please enter your tip percentage ( 10% , 12%, 15% ): "))
tip_percentage = float((tip_percentage[0] + tip_percentage[1]))
ppl = int(input("How many people to split the bill? "))

# total = round( bill_total * ( 1 + tip_percentage / 100 ) / ppl, 2)
total = round((bill_total + (bill_total * ( tip_percentage / 100 ))) / ppl, 2)

print(f"\nEach person has to pay ${total}")