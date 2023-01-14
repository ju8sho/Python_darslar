import datetime as dt

bugun = dt.date.today()
ramazon = dt.date(2023, 3, 23)
qurbonhayt = dt.date(2023, 6, 28)
kun_ramazon = ramazon - bugun
kun_hayt = qurbonhayt - bugun

print(f"\nRamazonga {kun_ramazon.days} kun qoldi,\nQurbon haytga {kun_hayt.days} kun qoldi\n")


tyil = dt.date(1997, 2, 14)
bugun = dt.date.today()
a = bugun - tyil
n = a.strftime("%d-%m-%y")
def kunutgan():
    return 
    
