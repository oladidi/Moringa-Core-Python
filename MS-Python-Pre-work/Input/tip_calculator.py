from sys import argv

bill = int(argv[1])
service = str(argv[2])

if service == "good":
    tip_percentage = 15
elif service == "great":
    tip_percentage = 20
else:
    tip_percentage = 0


tip = tip_percentage/100*bill
total_cost = int(bill+tip)

print(total_cost)