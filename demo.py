from datetime import date #导入datetime的date 对象
week=['一','二','三','四','五','六','日']
sample_today = date.today()#用today的方法获取今天的样本

print ('{}年'.format (sample_today.year)) 
print ('{}月'.format (sample_today.month))
print ('{}日'.format (sample_today.day))
print (sample_today.strftime('%Y/%m/%d')) #指定格式
# %Y 2026 %y 26 %m月份 %d日 %H小时 %M分钟 %S %A星期几（英文）
print ('今天是星期{}'.format (week[sample_today.weekday()])) #用weekday的方法

from datetime import time 
sample_time = time (3,34,36) 
print ('{}时{}分{}秒'.format (
    sample_time.hour,
    sample_time.minute,
    sample_time.second))
    
from datetime import timedelta #计算相差的天数
sample_timedelta = timedelta(days=234)
later=sample_today +sample_timedelta
print ('今天234天后是{}年{}月{}日'.format (later.year,later.month,later.day))
new_year=date(2027,3,23)
diff=new_year-sample_today
print ('2027/3/23和今天相差{}天'.format(diff.days))