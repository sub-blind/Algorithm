from datetime import datetime, timezone, timedelta

utc_now = datetime.now(timezone.utc)

utc_offset = timedelta(hours=9)

kst_now = utc_now + utc_offset

print(kst_now.strftime('%Y-%m-%d'))
