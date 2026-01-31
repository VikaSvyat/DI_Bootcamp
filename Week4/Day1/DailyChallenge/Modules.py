
import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()
in_15_hours = actual_datetime + datetime.timedelta(hours=15, minutes=10)


from datetime import datetime

string_date = "23/05/2026"

dt = datetime.strptime(string_date, "%d/%m/%Y")

print(f"Today is the {today_date.strftime("%d/%m")}")
print(f"In 15 hours and 10 minutes it will be the {in_15_hours.strftime("%d/%m")}")
print(f"{(dt-actual_datetime)}")