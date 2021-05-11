import time
from re import *
def input_data():
    while True:
        try:
            number_police=input("Введите номер полиса: ")
            if not(number_police.isdigit() and len(number_police.strip())==16):
                raise ValueError("invalid data")
            dob=input("Введите дату рождения в формате xx.xx.xx 'день.месяц.год': ")
            if not(dob.strip()): raise ValueError("Invalid data")
            dob=time.strftime('%d.%m.%Y',time.strptime(dob, '%d.%m.%Y'))
            surname_doctor = input("Введите фамилию врача: ").title()
            if (surname_doctor.isalpha() == False): raise ValueError("invalid data")
            step=abs(int(input("Введите, через сколько минут производить проверку на запись: ")))
            date = input("Введите нежелательные даты через запятую в формате xx.xx 'день.месяц' : ")
            unwanted_date=[]
            if date.strip():
                date=date.split(',');
                for i in date:
                    unwanted_date.append(time.strftime('%d.%m',time.strptime(i, '%d.%m')))               
            else:
                unwanted_date=''
            print(unwanted_date)
            
            interval_time=input("Введите инт ервал времени для посещения врача в формате (с какого часа)-(по какой час): ")
            if(interval_time!=''):
                interval_time=interval_time.split('-')
                if(len(interval_time)!=2 or interval_time[0]>interval_time[1]):raise ValueError("invalid data")
            mail=input("Введите email для получения уведомления о записи: ")
            if(mail.strip()!=''):
                mail_pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
                if(mail_pattern.match(mail) is None) :raise ValueError("invalid data")
            break
        except ValueError:
            print("Неверно введены данные!")
    return number_police,dob,surname_doctor,step,unwanted_date,interval_time,mail
