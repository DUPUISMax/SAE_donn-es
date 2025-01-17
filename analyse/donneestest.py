import donnees
from random import randint
donnes=[5,8,9,4]
t1=[]
t2=[]
t3=[]
t4=[]
t5=[]
t6=[]
t7=[]
t8=[]
t9=[]
t10=[]
t11=[]
t12=[]

t1.append(randint(0,10))
for i in range(5):
    t2.append(randint(0,10)) 
for i in range(5):
    t3.append(randint(0,10))
for i in range(5):
    t4.append(randint(0,10))
for i in range(5):
    t5.append(randint(0,10)) 
for i in range(5):
    t6.append(randint(0,10))
for i in range(5):
    t7.append(randint(0,10))
for i in range(5):
    t8.append(randint(0,10)) 
for i in range(5):
    t9.append(randint(0,10))
for i in range(5):
    t10.append(randint(0,10))
for i in range(5):
    t11.append(randint(0,10)) 
for i in range(5):
    t12.append(randint(0,10))

tab=[]
tab.append(t1)
tab.append(t2)
tab.append(t3)
tab.append(t4)
tab.append(t5)
tab.append(t6)
tab.append(t7)
tab.append(t8)
tab.append(t9)
tab.append(t10)
tab.append(t11)
tab.append(t12)
print(donnees.moy(donnes))
print(donnees.mef(tab))