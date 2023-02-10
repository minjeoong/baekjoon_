import datetime 
x, y = map(int,input().split())
day = ['MON','TUE','WED','THU', 'FRI', 'SAT','SUN']
a = day[datetime.date(2007,x, y).weekday()]
print(a)