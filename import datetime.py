import datetime
import pytz

d = datetime.date(2023, 3, 30)
# print(d)
tday = datetime.date.today()
# print(tday.year)
# print(tday.day)
# print(tday.month)
# print(tday)
# print(tday.weekday())
# print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
# print(tday - tdelta)
# print(tday + tdelta)

# date2 = date1 + time_delta
# time_delta = date1 + date2
bday = datetime.date(2023,6, 30)
till_bday = bday - tday
# print(till_bday)
# print(till_bday.total_seconds())

t = datetime.time(7, 55, 35)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t)

dt = datetime.datetime(2023, 3, 30, 6, 55, 50, 100000)
# print(dt.date())
# print(dt.time())
time_delta = datetime.timedelta(hours=12)
# print(dt + time_delta)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt2 = datetime.datetime(2023,3,30,6,55,30, tzinfo=pytz.UTC)
# print(dt2)
dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo= pytz.UTC)
# print(dt_utcnow)
dt_mtn = dt_now.astimezone(pytz.timezone("Indian/Reunion"))
# print(dt_mtn)
#
# for tz in pytz.all_timezones:
#     print(tz)

local_time = datetime.datetime.now()
print(local_time)

# print(local_time.strftime("%B %d, %Y"))

dt_str = "March 30, 2023"
dt4 = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt4)
# strftime = Datetime to String
# strptime = String to Datetime









