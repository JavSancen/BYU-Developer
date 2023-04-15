print ("""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
""")

age = int(input("Please enter your age: "))
heart_rate = int(input("Please enter your actual rate per minute: "))
max_heart_rate = 220 - age
rate_percent = heart_rate / max_heart_rate * 100

print(f"Your heart rate % is {rate_porcent:.2f}% of your max heart rate per minute.")

