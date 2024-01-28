# FA1

# 1. How many seconds are there in 42 minutes 42 seconds?
minutes = 42
seconds = 42
converted_seconds = round((minutes * 60) + seconds, 5)
print("Total seconds:", converted_seconds)

# 2. How many miles are there in 10 kilometers?
kilometer = 10
miles_per_kilometer = 1.61
converted_miles = round(kilometer / miles_per_kilometer, 2)
print(f"There are {converted_miles} miles in {kilometer} kilometers.")

# 3. If you run a 10-kilometer race in 42 minutes 42 seconds, what is your average pace and speed?

per_mile = converted_seconds / converted_miles
minutes_seconds_pace = int(per_mile // 60)
pace_seconds = round(per_mile % 60)

# Calculate average speed in miles per hour
speed_mph = round(converted_miles / (converted_seconds / 3600), 2)

print("Average pace:", minutes_seconds_pace, "minutes", pace_seconds, "seconds per mile")
print("Average speed:", speed_mph, "miles per hour")