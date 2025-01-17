from math import *
import matplotlib.pyplot as plot

#fonction pour faire la moyenne d'un tableau
def moyenne(t):
    moyenne=0
    for i in range(len(t)):
        moyenne+=t[i]
    return moyenne/len(t)

#fonction pour faire la variance d'un tableau en réutilisant la fonction moyenne
def variance(t):
    moy = moyenne(t)
    var = 0
    for i in range (len(t)):
        var+=(t[i]-moy)**2
    return var/len(t)

#fonction pour faire l'écart type d'un tableau en réutilisant la fonction variance
def ecarttype (t):
    return sqrt(variance(t))

#fonction pour faire la covariance entre deux tableauxen réutilisant la fonction moyenne
def covariance(t1,t2):
    cov=0
    moy1=moyenne(t1)
    moy2=moyenne(t2)
    for i in range (len(t1)):
        cov+=(t1[i]-moy1)*(t2[i]-moy2)
    return cov/len(t1)

#fonction pour faire la corrélation entre deux tableaux en réutilisant les fonctions covariance et variance
def correlation(t1,t2):
    varian=variance(t1)*variance(t2)
    ecart=sqrt(varian)
    corre=abs(covariance(t1,t2)/ecart)
    return corre

#fonction pour faire la matrice de corrélation d'un tableau de tableaux en réutilisant la fonction correlation sans mise en forme (un tableau de tableaux)
def correlationmatrice (t):
    tab1=[]
    tableau=[]
    for j in range (len(t)):
        for k in range(len(t)):
            tab1.append(round(correlation(t[j],t[k]),6))
        tableau.append(tab1)
        tab1=[]
    return tableau

#fonction de mise en forme de la matrice de corrélation (je n'ai pas utilisé d'heatmap mais imshow)
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

#fonction pour faire une courbe de suivi d'une donnée
def courbe(x,y):
    plot.plot(x,y)
    plot.xlabel('Temps')
    plot.ylabel('Temperature')  
    plot.show()


#Test des fonctions
T=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
L1=[3,3,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,8,7,4] 
L2=[103,203,4,3,2,5,8,9,13,16,18,18,19,21,22,22,21,17,17,12,10,-92,-93,-96]

print(moyenne(L1))
print(variance(L1))
print(ecarttype(L1))
print(moyenne(L2))
print(variance(L2))
print(ecarttype(L2))
print(covariance(L1,L2))
print(correlation(L1,L2))
print(correlationmatrice([L1,L2]))
MEF([L1,L2])
courbe(T,L1)
courbe(T,L2)