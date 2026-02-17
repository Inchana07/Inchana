import pandas as pd
a=[2,3,7,9,10]
var=pd.Series(a,index=['a','d','i','o','l'])
print(var)
print(type(var))
print(var)
di={"name":["py",1,"cpp"],7:[12,45,78,],"rank":[1,4,7,3]}
print(di)
va2=pd.Series(di)
print(va2)
print(type(va2))
q=pd.Series("ae",index=[1,43,6,8])
print(q)
q=pd.Series(23,index=[1,43,6,8])
q2=pd.Series(23,index=[1,43,6,8,67,45])
print(q+q2)
print("statistical Summary:\n",q2.describe())
