import requests
hr="https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
r=requests.get(hr)
#print r.text
data=r.json()

print data[0]["ccy"]

s=""
s+=data[0]["ccy"]
s+=". "
s+=data[0]["buy"]
s+=" / "
s+=data[0]["sale"]
print s
s=""
for i in data:
    
    s+="{}:{}/{}\n".format(i["ccy"],i["buy"],i["sale"])
#https://ide.c9.io/mihailselezniov/genesis    
