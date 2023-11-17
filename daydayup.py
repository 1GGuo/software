#题目一：天天向上的力量
def dayUp(df):#定义函数求每天的能力值
  dayup=1.0#定义第一天的基础能力值为1.0
  for i in range(365):#循环，开始求能力值
    if i%7 in [6,0]:#取余，判断是否是周末
     dayup=dayup*(1-0.01)#是周末则水平下降0.01
    else:
     dayup=dayup*(1+df)#否则则每天上升dayfactor
  return dayup#返回能力值
 
dayfactor=0.01#基础dayfactor

while(dayUp(dayfactor) <37.78):#循环判断是否能达到每天上升0.01的水平
  dayfactor+=0.001#dayfactor上升
print("每天的努力参数是:{:.3f}.".format(dayfactor))#输出可到达需要水平的dayfactor