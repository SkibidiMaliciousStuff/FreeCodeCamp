def extract(time):
    flag=0
    number='0123456789'
    index=0
    hour=minute=deter=''
    while index< len(time):
        if flag==0:
            if number.find(time[index])!=-1:
                hour+=time[index]
            else: flag+=1;
        elif flag==1:
            if number.find(time[index])!=-1:
                minute+=time[index]
            else: flag+=1;
        else:
            deter+=time[index]
        index+=1
    return int(hour),int(minute),deter

def exchange(day,reverse=0): 
    checker={'sunday':1,'monday':2,'tuesday':3,'wednesday':4,'thursday':5,'friday':6,'saturday':7}
    rchecker={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
    if reverse==0:
        return checker[day]
    else: 
        return rchecker[day]

def add_time(start, duration, cld=''):
    hour,minute,deter=extract(start)
    
    if deter=='PM':
        hour+=12
        if hour==24: hour=0
    
    nhour,nminute,_=extract(duration)
    nhour+=(minute+nminute)//60
    minute=(minute+nminute)%60
    
    day=nhour//24
    nhour%=24
    day+=(nhour+hour)//24
    hour=(hour+nhour)%24
    
    if hour==0:
        hour=str(12)
        deter='AM'
    elif hour==12:
        hour=str(hour)
        deter='PM'
    elif hour>12:
        hour=str(hour-12)
        deter='PM'
    else: 
        hour=str(hour)
        deter='AM'

    minute=str(minute) if minute>=10 else '0'+str(minute)
    
    if day==1:
        quote="(next day)"
    elif day==0: quote=''
    else:
        quote=f'({day} days later)'
    
    if cld:
        cld=cld.lower()
        cld=', '+exchange((exchange(cld)+day)%7,1)

    result=hour+':'+minute+' '+deter+cld+' '+quote  
    return result.strip()
print(add_time('3:30 PM', '2:12'))