from datetime import date, timedelta

yesterday = date.today() - timedelta(1)
today = date.today()
tomorrow = date.today() + timedelta(1)
print("yesterday was:", yesterday)
print("today is:", today)
print("tomorrow is:", tomorrow)