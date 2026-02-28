principle = int(input("Enter principle amount (>Rs.0): "))

while principle <= 0:
    print("principle amount was not valid!\n")
    principle = int(input("Enter a principle amount (>Rs.0): "))

rate = float(input("Enter Interest rate (>0%): "))
while rate <= 0:
    print("Interest rate was not valid!\n")
    rate = float(input("Enter Interest rate (>0%): "))

time = int(input("Enter the Time duration of investment (>1 month): "))
while time <= 0:
    print("Time duration was not valid!\n")
    time = int(input("Enter the Time duration of investment (>1 month): "))


final_Amount = principle*pow(1+(rate/100), time)
print(f"Principle: Rs.{principle:,.2f}\nInterest Rate: {rate:.2f}%\nTime Duration: {time} months\n\nFinal amount after compund interest would be Rs.{final_Amount:,.2f}")