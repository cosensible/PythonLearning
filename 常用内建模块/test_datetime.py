from datetime import datetime
# datetime模块包含datetime类
# 获取当前日期和时间
time=datetime.now()
print(time,type(time))
# 获取指定日期和时间
mytime=datetime(2015,12,15,9,30)
print(mytime)
# datetime转换为timestamp
print(mytime.timestamp())
# timestamp转换为datetime
t=1450143000.0
print(datetime.fromtimestamp(t)) 	#本地时间
print(datetime.utcfromtimestamp(t))	# utc时间
# str转换为datetime
str_time=datetime.strptime('2015-6-1 18:30:50','%Y-%m-%d %H:%M:%S')
print(str_time)
# datetime转换为str
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))
# datetime加减
from datetime import timedelta
print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=12))
# 本地时间转UTC时间
from datetime import timezone
tz_utc_8=timezone(timedelta(hours=8)) #创建时区   UTC+8:00
dt_8=now.replace(tzinfo=tz_utc_8)	  #强制设置为 UTC+8：00
dt_9=dt_8.astimezone(timezone(timedelta(hours=9))) #将dt_8转换为UTC+9:00
print(dt_8,dt_9)
# 时区转换
# 获取当前UTC时间,并设置时区为UTC+0:00
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将utc_dt转换为北京时间
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 将utc_dt转换为东京时间
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 将bj_dt转换为东京时间
tokyo_dt_2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt_2)