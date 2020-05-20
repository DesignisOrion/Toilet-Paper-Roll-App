# this app was inspired by howmuchtoiletpaper.com
num_sheets_in_roll = 160
how_many_sheets_you_use = 6

num_rolls_you_have = input("How many toilet paper rolls do you have?")
num_bathroom_visits = input(
    "How many times do you visit the bathroom in a day?")

total_sheets = num_sheets_in_roll * int(num_rolls_you_have)
total_daily_sheets = how_many_sheets_you_use * int(num_bathroom_visits)
num_days = int(total_sheets / total_daily_sheets)

print("The number of days your toilet paper will last:", num_days)
