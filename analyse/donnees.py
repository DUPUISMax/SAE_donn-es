from math import *
from random import *
import matplotlib.pyplot as plot
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

for i in range(5):
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

def moy(t):
    moyenne =0
    for i in range(len(t)):
        moyenne+=t[i]
    moyenne =moyenne/len(t)
    return moyenne

def variance(t):
    moyenne = moy (t)
    var = 0
    for i in range (len(t)):
        var+=(t[i]-moyenne)**2
    var=var/len(t)
    return var
   

def ecarttype (t):
    return sqrt(variance(t))

def covariance(t1,t2):
    cov=0
    moy1=moy(t1)
    moy2=moy(t2)
    for i in range (len(t1)):
        cov+=(t1[i]-moy1)*(t2[i]-moy2)
    cov=cov/len(t1)
    return cov

def correlation(t1,t2):
    varian=variance(t1)*variance(t2)
    ecart=sqrt(varian)
    corre=abs(covariance(t1,t2)/ecart)
    return corre
print(correlation(t1,t2))

def correlationmatrice (t):
    tab1=[]
    tableau=[]
    for j in range (len(t)):
        for k in range(len(t)):
            tab1.append(round(correlation(t[j],t[k]),6))
        tableau.append(tab1)
        tab1=[]
    return tableau


def MEF (t):
    tableau=correlationmatrice(t)
    plot.imshow(tableau, cmap='Blues')
    plot.colorbar()
    tab=[]
    nom="t"
    for i in range (len(t)):
        nom+=str(i+1)
        tab.append(nom)
        nom="t"
    for i, col_name in enumerate(tab):
        plot.text(0.04+i*0.08,1.01, col_name, transform=plot.gca().transAxes)
    
    for j, lig_name in enumerate(tab):
        plot.text(1.01,0.92-j*0.08,lig_name,transform=plot.gca().transAxes)
    plot.show()
print(mef(tab))

    









