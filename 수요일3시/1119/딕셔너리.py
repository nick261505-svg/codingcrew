data={'a':1,'b':10,'a':10}
#key 는 중복되지 않는다.-set
#print(data['a'])

for k in data.keys():
    print(k," : ",data[k])

for v in data.values():
    print(v)

dataList=[1,2,3,4]
data2={
    "count": len(dataList),
    'list': dataList
}
#print(data2["cou"])
if data2.get("coun")!=None:
    print(data2["coun"])
print(data2["list"][-1])