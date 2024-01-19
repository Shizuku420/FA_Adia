kilometers = 10
miles = kilometers / 1.61
print(f"There are {miles} miles in {kilometers} kilometers.")

rkm = 10
rtm = 42 + 42/60

ppmm = rtm / miles
pm = int(ppmm)
ps = int((ppmm - pm) * 60)

speed = miles / (rtm / 60)

print(f"If you run a {rkm} kilometer race in {rtm:.2f} minutes:")
print(f"Your average pace is {pm} minutes and {ps} seconds per mile.")
print(f"Your average speed is {speed:.2f} miles per hour.")
