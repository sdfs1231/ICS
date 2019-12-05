import datetime
import calendar
MONTHS={1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
DAYS={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}
reco=[]
def timeprocess(d,m,y):
    date=d
    months=m
    years=y
    if calendar.isleap(y):
        DAYS['feb']=29
    if d>DAYS[MONTHS[m]]:
        if m==12:
            years=y+1
            months=1
            date = d - DAYS[MONTHS[m]]
        else:
            date=d-DAYS[MONTHS[m]]
            months=m+1
    if d<1:
        months=m-1
        if months<1:
            months=12
            years=y-1
        date=DAYS[MONTHS[months]]
    if date<10:
        return '0'+str(date)+str(MONTHS[months])+str(years-2000)
    return str(date)+str(MONTHS[months])+str(years-2000)





