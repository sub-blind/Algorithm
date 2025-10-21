from datetime import datetime, timedelta

a = datetime.now() - timedelta(hours=9)
print(a.year)
print(a.month)
print(a.day)